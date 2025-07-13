from mcp.types import Tool
import json
from typing import Any, Callable, Dict, List
from alpha_vantage_client import AlphaVantageClient
from openai_client import OpenAIClient

class ToolHandler:
    """Enhanced tool handler with OpenAI function registration and dynamic dispatch"""
    def __init__(
        self,
        alpha_vantage_client: AlphaVantageClient,
        openai_client: OpenAIClient
    ):
        self.av_client = alpha_vantage_client
        self.openai_client = openai_client
        # Build dynamic mapping of tool names to handlers
        self._build_tool_map()
        # Register functions with OpenAI
        self._register_functions()

    def _build_tool_map(self):
        """Prepare dynamic dispatch map"""
        self._tool_map: Dict[str, Callable[[Dict[str, Any]], Any]] = {
            "get_stock_price": self._get_stock_price,
            "get_stock_quote": self._get_stock_quote,
            "get_company_overview": self._get_company_overview,
            "get_time_series_daily": self._get_time_series_daily,
            "get_time_series_intraday": self._get_time_series_intraday,
            "ask_openai": self._ask_openai,
        }

    def _register_functions(self):
        """Register all functions dynamically with OpenAI client"""
        for name, handler in self._tool_map.items():
            schema, description = self._get_schema_and_description(name)
            self.openai_client.register_function(
                name=name,
                function=self._make_wrapper(name),
                description=description,
                parameters=schema
            )

    def _get_schema_and_description(self, name: str) -> (Dict[str, Any], str):
        """Return JSON schema and description for each tool"""
        definitions = {
            "get_stock_price": (  
                {"type": "object", "properties": {"symbol": {"type": "string"}, "interval": {"type": "string", "enum": ["1min", "5min", "15min", "30min", "60min"], "default": "5min"}}, "required": ["symbol"]},
                "Get intraday stock price data"
            ),
            "get_stock_quote": (
                {"type": "object", "properties": {"symbol": {"type": "string", "description": "Stock symbol (e.g., AAPL)"}}, "required": ["symbol"]},
                "Get current stock quote for a given symbol"
            ),
            "get_company_overview": (
                {"type": "object", "properties": {"symbol": {"type": "string", "description": "Stock symbol (e.g., AAPL)"}}, "required": ["symbol"]},
                "Get detailed company overview and fundamentals"
            ),
            "get_time_series_daily": (
                {"type": "object", "properties": {"symbol": {"type": "string"}, "outputsize": {"type": "string", "enum": ["compact", "full"], "default": "compact"}}, "required": ["symbol"]},
                "Get daily historical stock price data"
            ),
            "get_time_series_intraday": (
                {"type": "object", "properties": {"symbol": {"type": "string"}, "interval": {"type": "string", "enum": ["1min", "5min", "15min", "30min", "60min"], "default": "5min"}}, "required": ["symbol"]},
                "Get intraday stock price data for today's trading session"
            ),
            "ask_openai": (
                {"type": "object", "properties": {"question": {"type": "string"}, "context": {"type": "string"}}, "required": ["question"]},
                "Ask OpenAI a financial question"
            ),
            "get_wti_price": (
                {"type": "object", "properties": {"interval": {"type": "string", "enum": ["daily", "weekly", "monthly"], "default": "monthly"}},
                 "required": []},
                "Get WTI crude oil price data"
            ),
            "get_brent_price": (
                {"type": "object", "properties": {"interval": {"type": "string", "enum": ["daily", "weekly", "monthly"], "default": "monthly"}},
                 "required": []},
                "Get Brent crude oil price data"
            ),
            "get_natural_gas_price": (
                {"type": "object", "properties": {"interval": {"type": "string", "enum": ["daily", "weekly", "monthly"], "default": "monthly"}},
                 "required": []},
                "Get Natural Gas price data"
            ),
        }
        return definitions[name]

    def _make_wrapper(self, name: str) -> Callable:
        """Creates an async wrapper for a given tool name"""
        async def wrapper(**kwargs):
            return await self.handle_tool_call(name, kwargs)
        return wrapper

    # Internal handlers matching map
    async def _get_stock_price(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "5min")
        data = await self.av_client.get_time_series_intraday(symbol, interval)
        # Extract latest price
        time_series = data.get(f"Time Series ({interval})", {})
        if not time_series:
            return json.dumps({"error": "No data found"})
        latest_time = sorted(time_series.keys())[-1]
        latest_data = time_series[latest_time]
        latest_price = latest_data["4. close"]
        return json.dumps({
            "symbol": symbol,
            "latest_time": latest_time,
            "latest_close": latest_price
        }, indent=2)

    async def _get_stock_quote(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        data = await self.av_client.get_stock_quote(symbol)
        return json.dumps(data, indent=2)

    async def _get_company_overview(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        data = await self.av_client.get_company_overview(symbol)
        return json.dumps(data, indent=2)

    async def _get_time_series_daily(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        outputsize = args.get("outputsize", "compact")
        data = await self.av_client.get_time_series_daily(symbol, outputsize)
        return json.dumps(data, indent=2)

    async def _get_time_series_intraday(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "5min")
        data = await self.av_client.get_time_series_intraday(symbol, interval)
        return json.dumps(data, indent=2)

    async def _ask_openai(self, args: Dict[str, Any]) -> str:
        question = args.get("question", "")
        context = args.get("context", "")
        return await self.openai_client.ask_financial_question(question, context)
    
    async def _get_wti_price(self, args: Dict[str, Any]) -> str:
        interval = args.get("interval", "monthly")
        data = await self.av_client.get_wti_price(interval)
        return json.dumps(data, indent=2)
    
    async def _get_brent_price(self, args: Dict[str, Any]) -> str:
        interval = args.get("interval", "monthly")
        data = await self.av_client.get_brent_price(interval)
        return json.dumps(data, indent=2)
    
    async def _get_natural_gas_price(self, args: Dict[str, Any]) -> str:
        interval = args.get("interval", "monthly")
        data = await self.av_client.get_natural_gas_price(interval)
        return json.dumps(data, indent=2)

    async def handle_tool_call(self, name: str, arguments: Dict[str, Any]) -> str:
        """Handle tool execution dynamically via dispatch map"""
        try:
            handler = self._tool_map.get(name)
            if not handler:
                return f"Unknown tool: {name}"
            return await handler(arguments)
        except Exception as e:
            return f"Error executing tool {name}: {str(e)}"

    def get_tool_definitions(self) -> List[Tool]:
        """Return list of available tool definitions for MCP"""
        return [
            Tool(name=name, description=self._get_schema_and_description(name)[1], inputSchema=self._get_schema_and_description(name)[0])
            for name in self._tool_map
        ]
