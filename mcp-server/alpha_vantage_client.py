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

    async def get_intraday(self, symbol: str, interval: str = "1min") -> Dict[str, Any]:
        """Get intraday time series data for a stock"""
        return await self._make_request("TIME_SERIES_INTRADAY", symbol, interval=interval)

    async def get_time_series_weekly(self, symbol: str) -> Dict[str, Any]:
        """Get weekly time series data"""
        return await self._make_request("TIME_SERIES_WEEKLY", symbol)

    async def get_time_series_monthly(self, symbol: str) -> Dict[str, Any]:
        """Get monthly time series data"""
        return await self._make_request("TIME_SERIES_MONTHLY", symbol)

    async def search_ticker(self, keywords: str) -> Dict[str, Any]:
        """Search ticker symbols based on keywords"""
        return await self._make_request("SYMBOL_SEARCH", keywords)

    async def get_global_market_status(self) -> Dict[str, Any]:
        """Get real-time global market status"""
        return await self._make_request("MARKET_STATUS")

    async def get_top_gainers_losers(self) -> Dict[str, Any]:
        """Get top gainers, losers, and most active stocks"""
        return await self._make_request("TOP_GAINERS_LOSERS")

    async def get_top_gainers_losers(self) -> Dict[str, Any]:
        """Get top gainers, losers, and most active stocks"""
        return await self._make_request("TOP_GAINERS_LOSERS")

    async def _get_quote_endpoint_trending(self, symbol: str) -> Dict[str, Any]:
        """ Get Quote Endpoint Trending data for a given symbol. """
        return await self._make_request("QUOTE_ENDPOINT_TRENDING", symbol)

    async def get_earnings_call_transcript(self, symbol: str) -> Dict[str, Any]:
        """Get Earnings Call Transcript for a given symbol"""
        return await self._make_request("EARNINGS_CALL_TRANSCRIPT", symbol)

    async def get_top_gainers_losers(self, region: str = "US") -> Dict[str, Any]:
        """Get Top Gainers & Losers for a region (default US)"""
        return await self._make_request("TOP_GAINERS_LOSERS", symbol=None, region=region)

    async def get_options_data(self, symbol: str) -> Dict[str, Any]:
        """Get options data for a given symbol"""
        return await self._make_request("OPTIONS", symbol)

    async def get_quote_endpoint_trending(self, interval: str = "monthly") -> Dict[str, Any]:
        """Get trending quotes across US equities"""
        return await self._make_request("TRENDING_QUOTES", symbol=None, interval=interval)

    async def get_historical_options(self, symbol: str) -> Dict[str, Any]:
        """Get historical options data for a given symbol"""
        return await self._make_request("HISTORICAL_OPTIONS", symbol)

    async def get_alpha_intelligence(self, symbol: str) -> Dict[str, Any]:
        """Get Alpha Intelligence™ data for a given symbol"""
        return await self._make_request("ALPHA_INTELLIGENCE", symbol)

    async def get_news_sentiments_trending(self, symbol: str) -> Dict[str, Any]:
        """Get News & Sentiments Trending for a given symbol"""
        return await self._make_request("NEWS_SENTIMENTS_TRENDING", symbol)

    async def get_earnings_call_transcript(self, symbol: str) -> Dict[str, Any]:
        """Get Earnings Call Transcript for a given symbol"""
        return await self._make_request("EARNINGS_CALL_TRANSCRIPT", symbol)

    async def get_top_gainers_losers(self, region: str = "US") -> Dict[str, Any]:
        """Get Top Gainers & Losers for a region (default US)"""
        return await self._make_request("TOP_GAINERS_LOSERS", symbol=None, region=region)

    async def get_insider_transactions_trending(self, symbol: str) -> Dict[str, Any]:
        """Get Insider Transactions Trending for a given symbol"""
        return await self._make_request("INSIDER_TRANSACTIONS_TRENDING", symbol)

    async def get_analytics_fixed_window(self, symbol: str, window: int = 14) -> Dict[str, Any]:
        """Get Analytics (Fixed Window) data for a symbol with a specified window size"""
        return await self._make_request("ANALYTICS_FIXED_WINDOW", symbol, window=window)

    async def get_analytics_sliding_window(self, symbol: str, window: int = 14) -> Dict[str, Any]:
        """Get Analytics (Sliding Window) data for a symbol with a specified window size"""
        return await self._make_request("ANALYTICS_SLIDING_WINDOW", symbol, window=window)

    async def get_fundamental_data(self, symbol: str) -> Dict[str, Any]:
        """Get fundamental data for a given symbol"""
        return await self._make_request("FUNDAMENTAL_DATA", symbol)

    async def get_company_overview_trending(self, symbol: str) -> Dict[str, Any]:
        """Get company overview trending data for a given symbol"""
        return await self._make_request("COMPANY_OVERVIEW_TRENDING", symbol)

    async def get_etf_profile_holdings(self, symbol: str) -> Dict[str, Any]:
        """Get ETF profile and holdings for a given symbol"""
        return await self._make_request("ETF_PROFILE_HOLDINGS", symbol)

    async def get_corporate_action_dividends(self, symbol: str) -> Dict[str, Any]:
        """Get corporate action dividend data for a given symbol"""
        return await self._make_request("CORPORATE_ACTION_DIVIDENDS", symbol)

    async def get_corporate_action_splits(self, symbol: str) -> Dict[str, Any]:
        """Get corporate action splits data for a given symbol"""
        return await self._make_request("CORPORATE_ACTION_SPLITS", symbol)

    async def get_income_statement(self, symbol: str) -> Dict[str, Any]:
        """Get income statement data for a given symbol"""
        return await self._make_request("INCOME_STATEMENT", symbol)

    async def get_balance_sheet(self, symbol: str) -> Dict[str, Any]:
        """Get balance sheet data for a given symbol"""
        return await self._make_request("BALANCE_SHEET", symbol)

    async def get_cash_flow(self, symbol: str) -> Dict[str, Any]:
        """Get cash flow data for a given symbol"""
        return await self._make_request("CASH_FLOW", symbol)

    async def get_earnings_trending(self, symbol: str) -> Dict[str, Any]:
        """Get earnings trending data for a given symbol"""
        return await self._make_request("EARNINGS_TRENDING", symbol)

    async def get_listing_delisting_status(self, symbol: str) -> Dict[str, Any]:
        """Get listing & delisting status for a given symbol"""
        return await self._make_request("LISTING_DELISTING_STATUS", symbol)

    async def get_earnings_calendar(self, region: str = "US") -> Dict[str, Any]:
        """Get earnings calendar for a region (default US)"""
        return await self._make_request("EARNINGS_CALENDAR", symbol=None, region=region)

    async def get_ipo_calendar(self, region: str = "US") -> Dict[str, Any]:
        """Get IPO calendar for a region (default US)"""
        return await self._make_request("IPO_CALENDAR", symbol=None, region=region)

    async def get_exchange_rates_trending(self, symbol: str) -> Dict[str, Any]:
        """Get Exchange Rates Trending for a given symbol"""
        return await self._make_request("EXCHANGE_RATES_TRENDING", symbol)

    async def get_fx_daily_data(self, symbol: str) -> Dict[str, Any]:
        """Get Daily FX (foreign exchange) rates for a given symbol"""
        return await self._make_request("FX_DAILY", symbol)

    async def get_fx_weekly_data(self, symbol: str) -> Dict[str, Any]:
        """Get Weekly FX rates for a given symbol"""
        return await self._make_request("FX_WEEKLY", symbol)

    async def get_fx_monthly_data(self, symbol: str) -> Dict[str, Any]:
        """Get Monthly FX rates for a given symbol"""
        return await self._make_request("FX_MONTHLY", symbol)
                
    async def get_exchange_rates_trending(self, symbol: str) -> Dict[str, Any]:
        """Get Exchange Rates Trending for a given symbol"""
        return await self._make_request("EXCHANGE_RATES_TRENDING", symbol)

    async def get_fx_daily_data(self, symbol: str) -> Dict[str, Any]:
        """Get Daily FX (foreign exchange) rates for a given symbol"""
        return await self._make_request("FX_DAILY", symbol)

    async def get_fx_weekly_data(self, symbol: str) -> Dict[str, Any]:
        """Get Weekly FX rates for a given symbol"""
        return await self._make_request("FX_WEEKLY", symbol)

    async def get_fx_monthly_data(self, symbol: str) -> Dict[str, Any]:
        """Get Monthly FX rates for a given symbol"""
        return await self._make_request("FX_MONTHLY", symbol)




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

    async def get_sma(self, symbol: str, interval: str = "daily", time_period: int = 20, series_type: str = "close") -> Dict[str, Any]:
        """Get Simple Moving Average (SMA) data"""
        return await self._make_request("SMA", symbol, interval=interval, time_period=time_period, series_type=series_type)
    
    async def get_ema(self, symbol: str, interval: str = "daily", time_period: int = 20, series_type: str = "close") -> Dict[str, Any]:
        """Get Exponential Moving Average (EMA) data"""
        return await self._make_request("EMA", symbol, interval=interval, time_period=time_period, series_type=series_type)
    
    async def get_wma(self, symbol: str, interval: str = "daily", time_period: int = 20, series_type: str = "close") -> Dict[str, Any]:
        """Get Weighted Moving Average (WMA) data"""
        return await self._make_request("WMA", symbol, interval=interval, time_period=time_period, series_type=series_type)
    
    async def get_dema(self, symbol: str, interval: str = "daily", time_period: int = 20, series_type: str = "close") -> Dict[str, Any]:
        """Get Double Exponential Moving Average (DEMA) data"""
        return await self._make_request("DEMA", symbol, interval=interval, time_period=time_period, series_type=series_type)
    
    async def get_tema(self, symbol: str, interval: str = "daily", time_period: int = 20, series_type: str = "close") -> Dict[str, Any]:
        """Get Triple Exponential Moving Average (TEMA) data"""
        return await self._make_request("TEMA", symbol, interval=interval, time_period=time_period, series_type=series_type)
    
    async def get_trima(self, symbol: str, interval: str = "daily", time_period: int = 20, series_type: str = "close") -> Dict[str, Any]:
        """Get Triangular Moving Average (TRIMA) data"""
        return await self._make_request("TRIMA", symbol, interval=interval, time_period=time_period, series_type=series_type)
    
    async def get_kama(self, symbol: str, interval: str = "daily", time_period: int = 20, series_type: str = "close") -> Dict[str, Any]:
        """Get Kaufman Adaptive Moving Average (KAMA) data"""
        return await self._make_request("KAMA", symbol, interval=interval, time_period=time_period, series_type=series_type)
    
    async def get_mama(self, symbol: str, interval: str = "daily", fastlimit: float = 0.5, slowlimit: float = 0.05, series_type: str = "close") -> Dict[str, Any]:
        """Get MESA Adaptive Moving Average (MAMA) data"""
        return await self._make_request("MAMA", symbol, interval=interval, fast_limit=fastlimit, slow_limit=slowlimit, series_type=series_type)
    
    async def get_vwap(self, symbol: str, interval: str = "daily") -> Dict[str, Any]:
        """Get Volume Weighted Average Price (VWAP) data"""
        return await self._make_request("VWAP", symbol, interval=interval)
    
    async def get_tthree(self, symbol: str, interval: str = "daily", time_period: int = 20, series_type: str = "close") -> Dict[str, Any]:
        """Get Triple Exponential Moving Average (T3) data"""
        return await self._make_request("T3", symbol, interval=interval, time_period=time_period, series_type=series_type)
    
    #async def get_macd(self, symbol: str, interval: str = "daily", fastperiod: int = 12, slowperiod: int = 26, signalperiod: int = 9, series_type: str = "close") -> Dict[str, Any]:
    #    """Get Moving Average Convergence Divergence (MACD) data"""
    #    return await self._make_request("MACD", symbol, interval=interval, fast_period=fastperiod, slow_period=slowperiod, signal_period=signalperiod, series_type=series_type)

    async def get_macdext(self, symbol: str, interval: str = "daily", fastperiod: int = 12, slowperiod: int = 26, signalperiod: int = 9, series_type: str = "close", fastmatype: int = 0, slowmatype: int = 0, signalmatype: int = 0) -> Dict[str, Any]:
        """Get MACD with additional parameters"""
        return await self._make_request("MACDEXT", symbol, interval=interval, fast_period=fastperiod, slow_period=slowperiod, signal_period=signalperiod, series_type=series_type, fastmatype=fastmatype, slowmatype=slowmatype, signalmatype=signalmatype)
    
    async def get_stoch(self, symbol: str, interval: str = "daily", fastkperiod: int = 5, slowkperiod: int = 3, slowdperiod: int = 3, slowkmatype: int = 0, slowdmatype: int = 0) -> Dict[str, Any]:
        """Get Stochastic Oscillator data"""
        return await self._make_request("STOCH", symbol, interval=interval, fastk_period=fastkperiod, slowk_period=slowkperiod, slowd_period=slowdperiod, slowkmatype=slowkmatype, slowdmatype=slowdmatype)
    
    async def get_stochfast(self, symbol: str, interval: str = "daily", fastkperiod: int = 5, fastdperiod: int = 3, fastdmatype: int = 0) -> Dict[str, Any]:
        """Get Stochastic Fast Oscillator data"""
        return await self._make_request("STOCHF", symbol, interval=interval, fastk_period=fastkperiod, fastd_period=fastdperiod, fastdmatype=fastdmatype)
    
    async def get_rsi(self, symbol: str, interval: str = "daily", time_period: int = 14, series_type: str = "close") -> Dict[str, Any]:
        """Get Relative Strength Index (RSI) data"""
        return await self._make_request("RSI", symbol, interval=interval, time_period=time_period, series_type=series_type)
    
    async def get_stochrsi(self, symbol: str, interval: str = "daily", time_period: int = 14, fastkperiod: int = 5, fastdperiod: int = 3, fastdmatype: int = 0, series_type: str = "close") -> Dict[str, Any]:
        """Get Stochastic RSI data"""
        return await self._make_request("STOCHRSI", symbol, interval=interval, time_period=time_period, fastk_period=fastkperiod, fastd_period=fastdperiod, fastdmatype=fastdmatype, series_type=series_type)
    
    async def get_willr(self, symbol: str, interval: str = "daily", time_period: int = 14) -> Dict[str, Any]:
        """Get Williams %R data"""
        return await self._make_request("WILLR", symbol, interval=interval, time_period=time_period)
    
    async def get_adx(self, symbol: str, interval: str = "daily", time_period: int = 14) -> Dict[str, Any]:
        """Get Average Directional Index (ADX) data"""
        return await self._make_request("ADX", symbol, interval=interval, time_period=time_period)
    
    async def get_adxr(self, symbol: str, interval: str = "daily", time_period: int = 14) -> Dict[str, Any]:
        """Get Average Directional Movement Index Rating (ADXR) data"""
        return await self._make_request("ADXR", symbol, interval=interval, time_period=time_period)
    
    async def get_apo(self, symbol: str, interval: str = "daily", fastperiod: int = 12, slowperiod: int = 26, series_type: str = "close") -> Dict[str, Any]:
        """Get Absolute Price Oscillator (APO) data"""
        return await self._make_request("APO", symbol, interval=interval, fast_period=fastperiod, slow_period=slowperiod, series_type=series_type)
    
    async def get_ppo(self, symbol: str, interval: str = "daily", fastperiod: int = 12, slowperiod: int = 26, series_type: str = "close", matype: int = 0) -> Dict[str, Any]:
        """Get Percentage Price Oscillator (PPO) data"""
        return await self._make_request("PPO", symbol, interval=interval, fast_period=fastperiod, slow_period=slowperiod, series_type=series_type, matype=matype)
    
    async def get_mom(self, symbol: str, interval: str = "daily", time_period: int = 10, series_type: str = "close") -> Dict[str, Any]:
        """Get Momentum data"""
        return await self._make_request("MOM", symbol, interval=interval, time_period=time_period, series_type=series_type)
    
    async def get_bop(self, symbol: str, interval: str = "daily") -> Dict[str, Any]:
        """Get Balance of Power (BOP) data"""
        return await self._make_request("BOP", symbol, interval=interval)
    
    async def get_cci(self, symbol: str, interval: str = "daily", time_period: int = 20) -> Dict[str, Any]:
        """Get Commodity Channel Index (CCI) data"""
        return await self._make_request("CCI", symbol, interval=interval, time_period=time_period)
    
    async def get_cmo(self, symbol: str, interval: str = "daily", time_period: int = 14, series_type: str = "close") -> Dict[str, Any]:
        """Get Chande Momentum Oscillator (CMO) data"""
        return await self._make_request("CMO", symbol, interval=interval, time_period=time_period, series_type=series_type)
    
    async def get_roc(self, symbol: str, interval: str = "daily", time_period: int = 10, series_type: str = "close") -> Dict[str, Any]:
        """Get Rate of Change (ROC) data"""
        return await self._make_request("ROC", symbol, interval=interval, time_period=time_period, series_type=series_type)
    
    async def get_rocr(self, symbol: str, interval: str = "daily", time_period: int = 10, series_type: str = "close") -> Dict[str, Any]:
        """Get Rate of Change Ratio (ROCR) data"""
        return await self._make_request("ROCR", symbol, interval=interval, time_period=time_period, series_type=series_type)
    
    async def get_aroon(self, symbol: str, interval: str = "daily", time_period: int = 14) -> Dict[str, Any]:
        """Get Aroon Indicator data"""
        return await self._make_request("AROON", symbol, interval=interval, time_period=time_period)
    
    async def get_aroonosc(self, symbol: str, interval: str = "daily", time_period: int = 14) -> Dict[str, Any]:
        """Get Aroon Oscillator data"""
        return await self._make_request("AROONOSC", symbol, interval=interval, time_period=time_period)
    
    async def get_mfi(self, symbol: str, interval: str = "daily", time_period: int = 14) -> Dict[str, Any]:
        """Get Money Flow Index (MFI) data"""
        return await self._make_request("MFI", symbol, interval=interval, time_period=time_period)
    
    async def get_trix(self, symbol: str, interval: str = "daily", time_period: int = 30, series_type: str = "close") -> Dict[str, Any]:
        """Get 1 day rate of change of a Triple Exponential Average (TRIX) data"""
        return await self._make_request("TRIX", symbol, interval=interval, time_period=time_period, series_type=series_type)
    
    async def get_ultosc(self, symbol: str, interval: str = "daily", timeperiod1: int = 7, timeperiod2: int = 14, timeperiod3: int = 28) -> Dict[str, Any]:
        """Get Ultimate Oscillator data"""
        return await self._make_request("ULTOSC", symbol, interval=interval, timeperiod1=timeperiod1, time_period2=timeperiod2, timeperiod3=timeperiod3)
    
    async def get_dx(self, symbol: str, interval: str = "daily", time_period: int = 14) -> Dict[str, Any]:
        """Get Directional Movement Index (DX) data"""
        return await self._make_request("DX", symbol, interval=interval, time_period=time_period)
    
    async def get_minus_di(self, symbol: str, interval: str = "daily", time_period: int = 14) -> Dict[str, Any]:
        """Get Minus Directional Indicator (-DI) data"""
        return await self._make_request("MINUS_DI", symbol, interval=interval, time_period=time_period)
    
    async def get_plus_di(self, symbol: str, interval: str = "daily", time_period: int = 14) -> Dict[str, Any]:
        """Get Plus Directional Indicator (+DI) data"""
        return await self._make_request("PLUS_DI", symbol, interval=interval, time_period=time_period)
    
    async def get_minus_dm(self, symbol: str, interval: str = "daily", time_period: int = 14) -> Dict[str, Any]:
        """Get Minus Directional Movement (-DM) data"""
        return await self._make_request("MINUS_DM", symbol, interval=interval, time_period=time_period)
    
    async def get_plus_dm(self, symbol: str, interval: str = "daily", time_period: int = 14) -> Dict[str, Any]:
        """Get Plus Directional Movement (+DM) data"""
        return await self._make_request("PLUS_DM", symbol, interval=interval, time_period=time_period)
    
    async def get_bbands(self, symbol: str, interval: str = "daily", time_period: int = 20, nbdevup: int = 2, nbdevdn: int = 2, series_type: str = "close") -> Dict[str, Any]:
        """Get Bollinger Bands data"""
        return await self._make_request("BBANDS", symbol, interval=interval, time_period=time_period, nbdevup=nbdevup, nbdevdn=nbdevdn, series_type=series_type)
    
    async def get_midpoint(self, symbol: str, interval: str = "daily", time_period: int = 14, series_type: str = "close") -> Dict[str, Any]:
        """Get Midpoint data"""
        return await self._make_request("MIDPOINT", symbol, interval=interval, time_period=time_period, series_type=series_type)
    
    async def get_midprice(self, symbol: str, interval: str = "daily", time_period: int = 14) -> Dict[str, Any]:
        """Get Midprice data"""
        return await self._make_request("MIDPRICE", symbol, interval=interval, time_period=time_period)
    
    async def get_sar(self, symbol: str, interval: str = "daily", acceleration: float = 0.02, maximum: float = 0.2) -> Dict[str, Any]:
        """Get Parabolic SAR data"""
        return await self._make_request("SAR", symbol, interval=interval, acceleration=acceleration, maximum=maximum)
    
    async def get_trange(self, symbol: str, interval: str = "daily") -> Dict[str, Any]:
        """Get True Range data"""
        return await self._make_request("TRANGE", symbol, interval=interval)
    
    async def get_atr(self, symbol: str, interval: str = "daily", time_period: int = 14) -> Dict[str, Any]:
        """Get Average True Range (ATR) data"""
        return await self._make_request("ATR", symbol, interval=interval, time_period=time_period)
    
    async def get_natr(self, symbol: str, interval: str = "daily", time_period: int = 14) -> Dict[str, Any]:
        """Get Normalized Average True Range (NATR) data"""
        return await self._make_request("NATR", symbol, interval=interval, time_period=time_period)
    
    async def get_ad(self, symbol: str, interval: str = "daily") -> Dict[str, Any]:
        """Get Chaikin A/D Line data"""
        return await self._make_request("AD", symbol, interval=interval)
    
    async def get_adosc(self, symbol: str, interval: str = "daily", fastperiod: int = 3, slowperiod: int = 10) -> Dict[str, Any]:
        """Get Chaikin A/D Oscillator data"""
        return await self._make_request("ADOSC", symbol, interval=interval, fast_period=fastperiod, slow_period=slowperiod)
    
    async def get_obv(self, symbol: str, interval: str = "daily") -> Dict[str, Any]:
        """Get On-Balance Volume (OBV) data"""
        return await self._make_request("OBV", symbol, interval=interval)
    
    async def get_ht_trendliner(self, symbol: str, interval: str = "daily", series_type: str = "close") -> Dict[str, Any]:
        """Get Hilbert Transform - Trendline data"""
        return await self._make_request("HT_TRENDLINE", symbol, interval=interval, series_type=series_type)
    
    async def get_ht_sine(self, symbol: str, interval: str = "daily", series_type: str = "close") -> Dict[str, Any]:
        """Get Hilbert Transform - SineWave data"""
        return await self._make_request("HT_SINE", symbol, interval=interval, series_type=series_type)
    
    async def get_ht_trendmode(self, symbol: str, interval: str = "daily", series_type: str = "close") -> Dict[str, Any]:
        """Get Hilbert Transform - Trend Mode data"""
        return await self._make_request("HT_TRENDMODE", symbol, interval=interval, series_type=series_type)
    
    async def get_ht_dcperiod(self, symbol: str, interval: str = "daily", series_type: str = "close") -> Dict[str, Any]:
        """Get Hilbert Transform - Dominant Cycle Period data"""
        return await self._make_request("HT_DCPERIOD", symbol, interval=interval, series_type=series_type)
    
    async def get_ht_dcphase(self, symbol: str, interval: str = "daily", series_type: str = "close") -> Dict[str, Any]:
        """Get Hilbert Transform - Dominant Cycle Phase data"""
        return await self._make_request("HT_DCPHASE", symbol, interval=interval, series_type=series_type)
    
    async def get_ht_phasor(self, symbol: str, interval: str = "daily", series_type: str = "close") -> Dict[str, Any]:
        """Get Hilbert Transform - Phasor data"""
        return await self._make_request("HT_PHASOR", symbol, interval=interval, series_type=series_type)
