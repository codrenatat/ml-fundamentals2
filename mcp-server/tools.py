from mcp.types import Tool
import json
from typing import List, Dict, Any
from alpha_vantage_client import AlphaVantageClient
from openai_client import OpenAIClient

class ToolHandler:
    """Enhanced tool handler with OpenAI function registration"""
    
    def __init__(self, alpha_vantage_client: AlphaVantageClient, openai_client: OpenAIClient):
        self.av_client = alpha_vantage_client
        self.openai_client = openai_client
        self._register_functions()
    
    def _register_functions(self):
        """Register all functions with OpenAI client"""
        # Register get_stock_quote
        self.openai_client.register_function(
            name="get_stock_quote",
            function=self._get_stock_quote_wrapper,
            description="Get current stock quote and price information for a given symbol",
            parameters={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock symbol (e.g., AAPL, MSFT, GOOGL)"
                    }
                },
                "required": ["symbol"]
            }
        )
        
        # Register get_company_overview
        self.openai_client.register_function(
            name="get_company_overview",
            function=self._get_company_overview_wrapper,
            description="Get detailed company information, fundamentals, and financial metrics",
            parameters={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock symbol (e.g., AAPL, MSFT, GOOGL)"
                    }
                },
                "required": ["symbol"]
            }
        )
        
        # Register get_time_series_daily
        self.openai_client.register_function(
            name="get_time_series_daily",
            function=self._get_time_series_daily_wrapper,
            description="Get daily historical stock price data for analysis and trends",
            parameters={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock symbol (e.g., AAPL, MSFT, GOOGL)"
                    },
                    "outputsize": {
                        "type": "string",
                        "description": "Amount of data to return: 'compact' (100 days) or 'full' (20+ years)",
                        "enum": ["compact", "full"],
                        "default": "compact"
                    }
                },
                "required": ["symbol"]
            }
        )
        
        # Register get_time_series_intraday
        self.openai_client.register_function(
            name="get_time_series_intraday",
            function=self._get_time_series_intraday_wrapper,
            description="Get intraday stock price data for today's trading session",
            parameters={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock symbol (e.g., AAPL, MSFT, GOOGL)"
                    },
                    "interval": {
                        "type": "string",
                        "description": "Time interval for intraday data",
                        "enum": ["1min", "5min", "15min", "30min", "60min"],
                        "default": "5min"
                    }
                },
                "required": ["symbol"]
            }
        )
    
    # Wrapper functions for OpenAI function calls
    async def _get_stock_quote_wrapper(self, symbol: str) -> str:
        """Wrapper for stock quote that returns formatted string"""
        try:
            data = await self.av_client.get_stock_quote(symbol.upper())
            return json.dumps(data, indent=2)
        except Exception as e:
            return f"Error retrieving stock quote for {symbol}: {str(e)}"
    
    async def _get_company_overview_wrapper(self, symbol: str) -> str:
        """Wrapper for company overview that returns formatted string"""
        try:
            data = await self.av_client.get_company_overview(symbol.upper())
            return json.dumps(data, indent=2)
        except Exception as e:
            return f"Error retrieving company overview for {symbol}: {str(e)}"
    
    async def _get_time_series_daily_wrapper(self, symbol: str, outputsize: str = "compact") -> str:
        """Wrapper for daily time series that returns formatted string"""
        try:
            data = await self.av_client.get_time_series_daily(symbol.upper(), outputsize)
            return json.dumps(data, indent=2)
        except Exception as e:
            return f"Error retrieving daily data for {symbol}: {str(e)}"
    
    async def _get_time_series_intraday_wrapper(self, symbol: str, interval: str = "5min") -> str:
        """Wrapper for intraday time series that returns formatted string"""
        try:
            data = await self.av_client.get_time_series_intraday(symbol.upper(), interval)
            return json.dumps(data, indent=2)
        except Exception as e:
            return f"Error retrieving intraday data for {symbol}: {str(e)}"
    
    def get_tool_definitions(self) -> List[Tool]:
        """Return list of available tool definitions for MCP"""
        return [
            Tool(
                name="get_stock_quote",
                description="Get current stock quote for a given symbol",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "symbol": {
                            "type": "string",
                            "description": "Stock symbol (e.g., AAPL, MSFT)"
                        }
                    },
                    "required": ["symbol"]
                }
            ),
            Tool(
                name="get_company_overview",
                description="Get detailed company information and fundamentals",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "symbol": {
                            "type": "string",
                            "description": "Stock symbol (e.g., AAPL, MSFT)"
                        }
                    },
                    "required": ["symbol"]
                }
            ),
            Tool(
                name="get_time_series_daily",
                description="Get daily historical stock price data",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "symbol": {
                            "type": "string",
                            "description": "Stock symbol (e.g., AAPL, MSFT)"
                        },
                        "outputsize": {
                            "type": "string",
                            "description": "Amount of data (compact or full)",
                            "default": "compact"
                        }
                    },
                    "required": ["symbol"]
                }
            ),
            Tool(
                name="get_time_series_intraday",
                description="Get intraday stock price data",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "symbol": {
                            "type": "string",
                            "description": "Stock symbol (e.g., AAPL, MSFT)"
                        },
                        "interval": {
                            "type": "string",
                            "description": "Time interval (1min, 5min, 15min, 30min, 60min)",
                            "default": "5min"
                        }
                    },
                    "required": ["symbol"]
                }
            ),
            Tool(
                name="ask_openai",
                description="Ask OpenAI a question with access to financial tools",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "question": {
                            "type": "string",
                            "description": "The question to ask OpenAI"
                        },
                        "context": {
                            "type": "string",
                            "description": "Optional financial data context"
                        }
                    },
                    "required": ["question"]
                }
            )
        ]
    
    async def handle_tool_call(self, name: str, arguments: Dict[str, Any]) -> str:
        """Handle tool execution"""
        try:
            if name == "get_stock_quote":
                symbol = arguments.get("symbol", "").upper()
                data = await self.av_client.get_stock_quote(symbol)
                return json.dumps(data, indent=2)
                
            elif name == "get_company_overview":
                symbol = arguments.get("symbol", "").upper()
                data = await self.av_client.get_company_overview(symbol)
                return json.dumps(data, indent=2)
                
            elif name == "get_time_series_daily":
                symbol = arguments.get("symbol", "").upper()
                outputsize = arguments.get("outputsize", "compact")
                data = await self.av_client.get_time_series_daily(symbol, outputsize)
                return json.dumps(data, indent=2)
                
            elif name == "get_time_series_intraday":
                symbol = arguments.get("symbol", "").upper()
                interval = arguments.get("interval", "5min")
                data = await self.av_client.get_time_series_intraday(symbol, interval)
                return json.dumps(data, indent=2)
                
            elif name == "ask_openai":
                question = arguments.get("question", "")
                context = arguments.get("context", "")
                result = await self.openai_client.ask_financial_question(question, context)
                return result
                
            else:
                return f"Unknown tool: {name}"
                
        except Exception as e:
            return f"Error executing tool {name}: {str(e)}"

