import aiohttp
from typing import Dict, Any

class AlphaVantageClient:
    """Client for Alpha Vantage financial data API"""
    
    BASE_URL = "https://www.alphavantage.co/query"
    
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    async def _make_request(self, function: str, symbol: str, **kwargs) -> Dict[str, Any]:
        """Make HTTP request to Alpha Vantage API"""
        params = {
            "function": function,
            "symbol": symbol,
            "apikey": self.api_key,
            **kwargs
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL, params=params) as response:
                if response.status != 200:
                    raise Exception(f"Alpha Vantage API error: {response.status}")
                return await response.json()
    
    async def get_stock_quote(self, symbol: str) -> Dict[str, Any]:
        """Get current stock quote"""
        return await self._make_request("GLOBAL_QUOTE", symbol)
    
    async def get_company_overview(self, symbol: str) -> Dict[str, Any]:
        """Get company overview and fundamentals"""
        return await self._make_request("OVERVIEW", symbol)
    
    async def get_time_series_daily(self, symbol: str, outputsize: str = "compact") -> Dict[str, Any]:
        """Get daily time series data"""
        return await self._make_request("TIME_SERIES_DAILY", symbol, outputsize=outputsize)
    
    async def get_time_series_intraday(self, symbol: str, interval: str = "5min") -> Dict[str, Any]:
        """Get intraday time series data"""
        return await self._make_request("TIME_SERIES_INTRADAY", symbol, interval=interval)

