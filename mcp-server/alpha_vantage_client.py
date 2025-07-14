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
    
    async def _make_request(self, function: str, symbol: str = None, **kwargs) -> Dict[str, Any]:
        """Make HTTP request to Alpha Vantage API"""
        params = {
            "function": function,
            "apikey": self.api_key,
            **kwargs
        }
        if symbol:
            params["symbol"] = symbol
        
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
        return await self._make_request("WTI", symbol=None, interval=interval)
    
    async def get_brent_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get Brent crude oil price"""
        return await self._make_request("BRENT", symbol=None, interval=interval)
    
    async def get_natural_gas_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get Henry Hub natural gas spot price"""
        return await self._make_request("NATURAL_GAS", symbol=None, interval=interval)
    
    async def get_copper_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get global copper price"""
        return await self._make_request("COPPER", symbol=None, interval=interval)
    
    async def get_aluminum_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get global aluminum price"""
        return await self._make_request("ALUMINUM", symbol=None, interval=interval)
    
    async def get_wheat_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get global wheat price"""
        return await self._make_request("WHEAT", symbol=None, interval=interval)
    
    async def get_corn_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get global corn price"""
        return await self._make_request("CORN", symbol=None, interval=interval)
    
    async def get_cotton_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get global cotton price"""
        return await self._make_request("COTTON", symbol=None, interval=interval)
    
    async def get_sugar_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get global sugar price"""
        return await self._make_request("SUGAR", symbol=None, interval=interval)
    
    async def get_coffee_price(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get global coffee price"""
        return await self._make_request("COFFEE", symbol=None, interval=interval)
    
    async def get_global_price_index(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get Global Price Index of All Commodities"""
        return await self._make_request("ALL_COMMODITIES", symbol=None, interval=interval)
    
    async def get_real_gdp(self, interval: str = "quarterly") -> Dict[str, Any]:
        """Get annual and quarterly Real GDP of the United States"""
        return await self._make_request("REAL_GDP", symbol=None, interval=interval)
    
    async def get_real_gdp_per_capita(self) -> Dict[str, Any]:
        """Get quarterly Real GDP Per Capita of the United States"""
        return await self._make_request("REAL_GDP_PER_CAPITA", symbol=None)
    
    async def get_treasury_yield(self, interval: str = "weekly", maturity: str = "5year") -> Dict[str, Any]:
        """Get US Treasury yield data"""
        return await self._make_request("TREASURY_YIELD", symbol=None, interval=interval, maturity=maturity)
    
    async def fed_funds_rate(self, interval: str = "weekly") -> Dict[str, Any]:
        """Get US Federal Funds Rate"""
        return await self._make_request("FEDERAL_FUNDS_RATE", symbol=None, interval=interval)
    
    async def cpi(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get US Consumer Price Index (CPI)"""
        return await self._make_request("CPI", symbol=None, interval=interval)
    
    async def get_inflation_rate(self) -> Dict[str, Any]:
        """Get US Inflation Rate"""
        return await self._make_request("INFLATION", symbol=None)
    
    async def get_retail_sales(self) -> Dict[str, Any]:
        """Get US Advance Retail Sales: Retail Trade data"""
        return await self._make_request("RETAIL_SALES", symbol=None)
    
    async def get_durables_orders(self) -> Dict[str, Any]:
        """Get US Durable Goods Orders data"""
        return await self._make_request("DURABLES", symbol=None)
    
    async def get_unemployment_rate(self) -> Dict[str, Any]:
        """Get US Unemployment Rate"""
        return await self._make_request("UNEMPLOYMENT", symbol=None)
    
    async def get_nonfarm_payrolls(self) -> Dict[str, Any]:
        """Get US Non-Farm Payrolls data"""
        return await self._make_request("NONFARM_PAYROLL", symbol=None)