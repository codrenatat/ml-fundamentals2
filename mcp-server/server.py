from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, ServerCapabilities

from config import Config
from alpha_vantage_client import AlphaVantageClient
from openai_client import OpenAIClient
from tools import ToolHandler


class FinancialMCPServer:
    """Main MCP server class"""
    
    def __init__(self):
        self.config = Config()
        self.server = Server("financial-assistant")
        self.setup_clients()
        self.setup_handlers()
    
    def setup_clients(self):
        """Initialize API clients"""
        self.av_client = AlphaVantageClient(self.config.alpha_vantage_api_key)
        self.openai_client = OpenAIClient(
            api_key=self.config.openai_api_key,
            model=self.config.openai_model,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature
        )
        self.tool_handler = ToolHandler(self.av_client, self.openai_client)
    
    def setup_handlers(self):
        """Setup MCP server handlers"""
        
        @self.server.list_tools()
        async def handle_list_tools():
            return self.tool_handler.get_tool_definitions()
        
        @self.server.call_tool()
        async def handle_call_tool(name: str, arguments: dict):
            result = await self.tool_handler.handle_tool_call(name, arguments)
            return [TextContent(type="text", text=result)]
    
    async def run(self):
        """Run the MCP server"""
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="financial-assistant",
                    server_version="1.0.0",
                    capabilities=ServerCapabilities(
                        tools=None
                    ),
                ),
            )
