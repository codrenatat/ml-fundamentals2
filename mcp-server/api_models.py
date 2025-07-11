from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, List

class ToolCallRequest(BaseModel):
    """Request model for tool calls"""
    tool_name: str = Field(..., description="Name of the tool to call")
    arguments: Dict[str, Any] = Field(default_factory=dict, description="Arguments for the tool")

class StockQuoteRequest(BaseModel):
    """Request model for stock quotes"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")

class CompanyOverviewRequest(BaseModel):
    """Request model for company overview"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")

class TimeSeriesRequest(BaseModel):
    """Request model for time series data"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    outputsize: Optional[str] = Field("compact", description="Amount of data (compact or full)")

class IntradayRequest(BaseModel):
    """Request model for intraday data"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("5min", description="Time interval (1min, 5min, 15min, 30min, 60min)")

class AskOpenAIRequest(BaseModel):
    """Request model for OpenAI questions"""
    question: str = Field(..., description="Question to ask OpenAI")
    context: Optional[str] = Field(None, description="Optional financial context")

class APIResponse(BaseModel):
    """Standard API response"""
    success: bool
    data: Any = None
    error: Optional[str] = None
    message: Optional[str] = None

class ToolInfo(BaseModel):
    """Tool information"""
    name: str
    description: str
    parameters: Dict[str, Any]

class ToolsListResponse(BaseModel):
    """Response for tools list"""
    success: bool
    tools: List[ToolInfo] = []
    error: Optional[str] = None
