import sys
import asyncio

if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())


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
            
    async def get_stock_price(self, symbol: str, interval: str = "5min") -> Dict[str, Any]:
        """Get intraday stock price data"""
        return await self._make_request("TIME_SERIES_INTRADAY", symbol, interval=interval)
        
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

    async def get_wti_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get WTI crude oil price"""
        return await self._make_request("WTI", interval=interval)
    
    async def get_brent_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get Brent crude oil price"""
        return await self._make_request("BRENT", interval=interval)
    
    async def get_natural_gas_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get Henry Hub natural gas spot price"""
        return await self._make_request("NATURAL_GAS", interval=interval)
    
    async def get_copper_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get global copper price"""
        return await self._make_request("COPPER", interval=interval)
    
    async def get_aluminum_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get global aluminum price"""
        return await self._make_request("ALUMINUM", interval=interval)
    
    async def get_wheat_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get global wheat price"""
        return await self._make_request("WHEAT", interval=interval)
    
    async def get_corn_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get global corn price"""
        return await self._make_request("CORN", interval=interval)
    
    async def get_cotton_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get global cotton price"""
        return await self._make_request("COTTON", interval=interval)
    
    async def get_sugar_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get global sugar price"""
        return await self._make_request("SUGAR", interval=interval)
    
    async def get_coffee_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get global coffee price"""
        return await self._make_request("COFFEE", interval=interval)
    
    async def get_global_price_index(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get Global Price Index of All Commodities"""
        return await self._make_request("ALL_COMMODITIES", interval=interval)