import asyncio
import os
from contextlib import asynccontextmanager
from typing import Dict, Any

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from mcp_client import MCPClient
from api_models import (
    ToolCallRequest, StockQuoteRequest, CompanyOverviewRequest,
    TimeSeriesRequest, IntradayRequest, AskOpenAIRequest,
    APIResponse, ToolsListResponse, ToolInfo
)

# Global MCP client
mcp_client: MCPClient = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage MCP server lifecycle"""
    global mcp_client
    
    # Get environment variables
    env_vars = {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "ALPHA_VANTAGE_API_KEY": os.getenv("ALPHA_VANTAGE_API_KEY"),
    }
    
    # Validate required environment variables
    if not env_vars["OPENAI_API_KEY"]:
        raise ValueError("OPENAI_API_KEY environment variable is required")
    if not env_vars["ALPHA_VANTAGE_API_KEY"]:
        raise ValueError("ALPHA_VANTAGE_API_KEY environment variable is required")
    
    # Start MCP server
    try:
        mcp_client = MCPClient("main.py", env_vars)
        await mcp_client.start_server()
        print("✅ MCP server started successfully")
    except Exception as e:
        print(f"⚠️  Warning: MCP server failed to start: {e}")
        print("   Using mock responses for now...")
        mcp_client = None
    
    yield
    
    # Cleanup
    if mcp_client:
        await mcp_client.stop_server()

# Create FastAPI app
app = FastAPI(
    title="Financial MCP API",
    description="REST API wrapper for Financial MCP Server",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_mcp_client() -> MCPClient:
    """Dependency to get MCP client"""
    if not mcp_client:
        raise HTTPException(status_code=500, detail="MCP server not initialized")
    return mcp_client

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Financial MCP API Server", "version": "1.0.0"}

# Health check
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    mcp_status = "running" if mcp_client else "stopped"
    return {
        "status": "healthy", 
        "mcp_server": mcp_status,
        "message": "API server is running" + (" (using mock responses)" if not mcp_client else "")
    }

# List available tools
@app.get("/tools", response_model=ToolsListResponse)
async def list_tools(client: MCPClient = Depends(get_mcp_client)):
    """List all available MCP tools"""
    response = await client.list_tools()
    
    if not response.success:
        return ToolsListResponse(success=False, error=response.error)
    
    print(f"Available MCP Tools: {response}")
    tools = []
    if response.data:
        for tool_data in response.data["tools"]:
            tools.append(ToolInfo(
                name=tool_data.get("name", ""),
                description=tool_data.get("description", ""),
                parameters=tool_data.get("inputSchema", {})
            ))
    
    return ToolsListResponse(success=True, tools=tools)

# Generic tool call endpoint
@app.post("/tools/call", response_model=APIResponse)
async def call_tool(
    request: ToolCallRequest,
    client: MCPClient = Depends(get_mcp_client)
):
    """Call any MCP tool with custom arguments"""
    response = await client.call_tool(request.tool_name, request.arguments)
    
    if not response.success:
        raise HTTPException(status_code=400, detail=response.error)
    
    return APIResponse(success=True, data=response.data)

# Specific endpoints for each tool
@app.post("/stock/quote", response_model=APIResponse)
async def get_stock_quote(
    request: StockQuoteRequest,
    client: MCPClient = Depends(get_mcp_client)
):
    """Get current stock quote"""
    response = await client.call_tool("get_stock_quote", {"symbol": request.symbol})
    
    if not response.success:
        raise HTTPException(status_code=400, detail=response.error)
    
    return APIResponse(success=True, data=response.data)

@app.post("/stock/overview", response_model=APIResponse)
async def get_company_overview(
    request: CompanyOverviewRequest,
    client: MCPClient = Depends(get_mcp_client)
):
    """Get company overview and fundamentals"""
    response = await client.call_tool("get_company_overview", {"symbol": request.symbol})
    
    if not response.success:
        raise HTTPException(status_code=400, detail=response.error)
    
    return APIResponse(success=True, data=response.data)

@app.post("/stock/daily", response_model=APIResponse)
async def get_time_series_daily(
    request: TimeSeriesRequest,
    client: MCPClient = Depends(get_mcp_client)
):
    """Get daily time series data"""
    args = {"symbol": request.symbol}
    if request.outputsize:
        args["outputsize"] = request.outputsize
    
    response = await client.call_tool("get_time_series_daily", args)
    
    if not response.success:
        raise HTTPException(status_code=400, detail=response.error)
    
    return APIResponse(success=True, data=response.data)

@app.post("/stock/intraday", response_model=APIResponse)
async def get_time_series_intraday(
    request: IntradayRequest,
    client: MCPClient = Depends(get_mcp_client)
):
    """Get intraday time series data"""
    args = {"symbol": request.symbol}
    if request.interval:
        args["interval"] = request.interval
    
    response = await client.call_tool("get_time_series_intraday", args)
    
    if not response.success:
        raise HTTPException(status_code=400, detail=response.error)
    
    return APIResponse(success=True, data=response.data)

@app.post("/ai/chat", response_model=APIResponse)
async def chat_with_ai(
    request: AskOpenAIRequest,
    client: MCPClient = Depends(get_mcp_client)
):
    """Enhanced AI chat with access to financial tools via function calling"""
    response = await client.call_tool("ask_openai", {
        "question": request.question,
        "context": request.context or ""
    })
    
    if not response.success:
        raise HTTPException(status_code=400, detail=response.error)
    
    return APIResponse(success=True, data={"response": response.data})

# New endpoint for natural language financial queries
@app.post("/financial/query", response_model=APIResponse)
async def financial_query(
    query: str,
    client: MCPClient = Depends(get_mcp_client)
):
    """Process natural language financial queries with automatic tool selection"""
    response = await client.call_tool("ask_openai", {"question": query})
    
    if not response.success:
        raise HTTPException(status_code=400, detail=response.error)
    
    return APIResponse(
        success=True, 
        data={
            "query": query,
            "response": response.data
        }
    )

# Alternative endpoint accepting JSON body
@app.post("/financial/ask", response_model=APIResponse)
async def ask_financial_question(
    request: Dict[str, str],
    client: MCPClient = Depends(get_mcp_client)
):
    """Ask a financial question in natural language"""
    question = request.get("question", "")
    if not question:
        raise HTTPException(status_code=400, detail="Question is required")
    
    response = await client.call_tool("ask_openai", {"question": question})
    
    if not response.success:
        raise HTTPException(status_code=400, detail=response.error)
    
    return APIResponse(
        success=True,
        data={
            "question": question,
            "answer": response.data
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

