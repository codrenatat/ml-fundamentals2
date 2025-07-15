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
            "get_time_series_weekly": self._get_time_series_weekly,
            "get_time_series_monthly": self._get_time_series_monthly,
            "get_time_series_monthly_adjusted": self._get_time_series_monthly_adjusted,
            "search_ticker": self._search_ticker,
            "get_global_market_status": self._get_global_market_status,
            "get_quote_endpoint_trending": self._get_quote_endpoint_trending,
            "get_historical_options": self._get_historical_options,
            "get_alpha_intelligence": self._get_alpha_intelligence,
            "get_news_sentiments_trending": self._get_news_sentiments_trending,
            "get_earnings_call_transcript": self._get_earnings_call_transcript,
            "get_top_gainers_losers": self._get_top_gainers_losers,
            "get_insider_transactions_trending": self._get_insider_transactions_trending,
            "get_analytics_fixed_window": self._get_analytics_fixed_window,
            "get_analytics_sliding_window": self._get_analytics_sliding_window,
            "get_fundamental_data": self._get_fundamental_data,
            "get_company_overview_trending": self._get_company_overview_trending,
            "get_etf_profile_holdings": self._get_etf_profile_holdings,
            "get_corporate_action_dividends": self._get_corporate_action_dividends,
            "get_corporate_action_splits": self._get_corporate_action_splits,
            "get_income_statement": self._get_income_statement,
            "get_balance_sheet": self._get_balance_sheet,
            "get_cash_flow": self._get_cash_flow,
            "get_earnings_trending": self._get_earnings_trending,
            "get_listing_delisting_status": self._get_listing_delisting_status,
            "get_earnings_calendar": self._get_earnings_calendar,
            
            "get_ipo_calendar": self._get_ipo_calendar,
            "get_exchange_rates_trending": self._get_exchange_rates_trending,
            "get_fx_daily_data": self._get_fx_daily_data,
            "get_fx_weekly_data": self._get_fx_weekly_data,
            "get_fx_monthly_data": self._get_fx_monthly_data,

            "get_exchange_rates_trending": self._get_exchange_rates_trending,
            "get_fx_daily_data": self._get_fx_daily_data,
            "get_fx_weekly_data": self._get_fx_weekly_data,
            "get_fx_monthly_data": self._get_fx_monthly_data,

            "get_wti_price": self._get_wti_price,
            "get_brent_price": self._get_brent_price,
            "get_natural_gas_price": self._get_natural_gas_price,
            "get_copper_price": self._get_copper_price,
            "get_aluminum_price": self._get_aluminum_price,
            "get_wheat_price": self._get_wheat_price,
            "get_corn_price": self._get_corn_price,
            "get_cotton_price": self._get_cotton_price,
            "get_sugar_price": self._get_sugar_price,
            "get_coffee_price": self._get_coffee_price,
            "get_all_commodities_price_index": self._get_all_commodities_price_index,
            "get_real_gdp": self._get_real_gdp,
            "get_real_gdp_per_capita": self._get_real_gdp_per_capita,
            "get_treasury_yield": self._get_treasury_yield,
            "get_federal_funds_rate": self._get_federal_funds_rate,
            "get_cpi": self._get_cpi,
            "get_inflation_rate": self._get_inflation_rate,
            "get_retail_sales": self._get_retail_sales,
            "get_durables": self._get_durables,
            "get_unemployment_rate": self._get_unemployment_rate,
            "get_non_farm_payrolls": self._get_non_farm_payrolls,
            "get_sma": self._get_sma,
            "get_ema": self._get_ema,
            "get_wma": self._get_wma,
            "get_dema": self._get_dema,
            "get_tema": self._get_tema,
            "get_trima": self._get_trima,
            "get_kama": self._get_kama,
            "get_mama": self._get_mama,
            "get_vwap": self._get_vwap,
            "get_tthree": self._get_tthree,
            "get_macdext": self._get_macdext,
            "get_stoch": self._get_stoch,
            "get_stochfast": self._get_stochfast,
            "get_rsi": self._get_rsi,
            "get_stochrsi": self._get_stochrsi,
            "get_willr": self._get_willr,
            "get_adx": self._get_adx,
            "get_adxr": self._get_adxr,
            "get_apo": self._get_apo,
            "get_ppo": self._get_ppo,
            "get_mom": self._get_mom,
            "get_bop": self._get_bop,
            "get_cci": self._get_cci,
            "get_cmo": self._get_cmo,
            "get_roc": self._get_roc,
            "get_rocr": self._get_rocr,
            "get_aroon": self._get_aroon,
            "get_aroonosc": self._get_aroonosc,
            "get_mfi": self._get_mfi,
            "get_trix": self._get_trix,
            "get_ultosc": self._get_ultosc,
            "get_dx": self._get_dx,
            "get_minus_di": self._get_minus_di,
            "get_plus_di": self._get_plus_di,
            "get_minus_dm": self._get_minus_dm,
            "get_plus_dm": self._get_plus_dm,
            "get_bbands": self._get_bbands,
            "get_midpoint": self._get_midpoint,
            "get_midprice": self._get_midprice,
            "get_sar": self._get_sar,
            "get_trange": self._get_trange,
            "get_atr": self._get_atr,
            "get_natr": self._get_natr,
            "get_ad": self._get_ad,
            "get_adosc": self._get_adosc,
            "get_obv": self._get_obv,
            "get_ht_trendline": self._get_ht_trendline,
            "get_ht_sine": self._get_ht_sine,
            "get_ht_trendmode": self._get_ht_trendmode,
            "get_ht_dcperiod": self._get_ht_dcperiod,
            "get_ht_dcphase": self._get_ht_dcphase,
            "get_ht_phasor": self._get_ht_phasor,
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

            "get_time_series_weekly": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {
                            "type": "string",
                            "description": "Stock symbol (e.g., AAPL)"
                        }
                    },
                    "required": ["symbol"]
                },
                "Get weekly time series data"
            ),

            "get_time_series_monthly": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {
                            "type": "string",
                            "description": "Stock symbol (e.g., AAPL)"
                        }
                    },
                    "required": ["symbol"]
                },
                "Get monthly time series data"
            ),

            "get_time_series_monthly_adjusted": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {
                            "type": "string",
                            "description": "Stock symbol (e.g., AAPL)"
                        }
                    },
                    "required": ["symbol"]
                },
                "Get monthly adjusted time series data"
            ),

            "search_ticker": (
                {
                    "type": "object",
                    "properties": {
                        "keywords": {
                            "type": "string",
                            "description": "Search query for a ticker (e.g., Apple)"
                        }
                    },
                    "required": ["keywords"]
                },
                "Search ticker symbols based on keywords"
            ),

            "get_global_market_status": (
                {
                    "type": "object",
                    "properties": {},
                    "required": []
                },
                "Get real-time global market status"
            ),

            "get_top_gainers_losers": (
                {
                    "type": "object",
                    "properties": {},
                    "required": []
                },
                "Get top gainers, losers, and most active stocks in the market"
            ),

            "get_quote_endpoint_trending": (
                {
                    "type": "object",
                    "properties": {},
                    "required": []
                },
                "Get trending tickers from Quote Endpoint"
            ),

            "get_historical_options": (
                {
                    "type": "object",
                    "properties": {},
                    "required": []
                },
                "Get historical options trending data"
            ),

            "get_alpha_intelligence": (
                {
                    "type": "object",
                    "properties": {},
                    "required": []
                },
                "Get Alpha Intelligence analytics"
            ),

            "get_news_sentiments_trending": (
                {
                    "type": "object",
                    "properties": {},
                    "required": []
                },
                "Get trending news and sentiment analysis"
            ),

            "get_earnings_call_transcript": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {
                            "type": "string",
                            "description": "Stock symbol (e.g., AAPL)"
                        }
                    },
                    "required": ["symbol"]
                },
                "Get earnings call transcript for a symbol"
            ),

            "get_insider_transactions_trending": (
                {
                    "type": "object",
                    "properties": {},
                    "required": []
                },
                "Get trending insider transactions"
            ),

            "get_analytics_fixed_window": (
                {
                    "type": "object",
                    "properties": {},
                    "required": []
                },
                "Get fixed window analytics"
            ),

            "get_analytics_sliding_window": (
                {
                    "type": "object",
                    "properties": {},
                    "required": []
                },
                "Get sliding window analytics"
            ),
            "get_fundamental_data": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                    },
                    "required": ["symbol"]
                },
                "Get fundamental data for a given symbol"
            ),

            "get_company_overview_trending": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                    },
                    "required": ["symbol"]
                },
                "Get company overview trending for a given symbol"
            ),

            "get_etf_profile_holdings": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                    },
                    "required": ["symbol"]
                },
                "Get ETF profile and holdings for a given symbol"
            ),

            "get_corporate_action_dividends": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                    },
                    "required": ["symbol"]
                },
                "Get corporate action dividends data for a given symbol"
            ),

            "get_corporate_action_splits": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                    },
                    "required": ["symbol"]
                },
                "Get corporate action splits data for a given symbol"
            ),

            "get_income_statement": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                    },
                    "required": ["symbol"]
                },
                "Get income statement data for a given symbol"
            ),

            "get_balance_sheet": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                    },
                    "required": ["symbol"]
                },
                "Get balance sheet data for a given symbol"
            ),
            "get_cash_flow": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                    },
                    "required": ["symbol"]
                },
                "Get cash flow data for a given symbol"
            ),

            "get_earnings_trending": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                    },
                    "required": ["symbol"]
                },
                "Get earnings trending data for a given symbol"
            ),

            "get_listing_delisting_status": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                    },
                    "required": ["symbol"]
                },
                "Get listing & delisting status for a given symbol"
            ),

            "get_earnings_calendar": (
                {
                    "type": "object",
                    "properties": {
                        "region": {"type": "string", "default": "US"},
                    },
                    "required": []
                },
                "Get earnings calendar for a region"
            ),

            "get_ipo_calendar": (
                {
                    "type": "object",
                    "properties": {
                        "region": {"type": "string", "default": "US"},
                    },
                    "required": []
                },
                "Get IPO calendar for a region"
            ),
            "get_exchange_rates_trending": (
                {
                    "type": "object",
                    "properties": {
                        "base_currency": {"type": "string", "default": "USD"},
                    },
                    "required": []
                },
                "Get trending exchange rates based on a base currency"
            ),"get_exchange_rates_trending": (
                {
                        "type": "object",
                        "properties": {
                            "symbol": {"type": "string"},
                        },
                        "required": ["symbol"]
                    },
                    "Get trending exchange rates for a given symbol"
                ),
            "get_fx_daily_data": (
                    {
                        "type": "object",
                        "properties": {
                            "symbol": {"type": "string"},
                        },
                        "required": ["symbol"]
                    },
                    "Get daily foreign exchange rates for a given symbol"
                ),
            "get_fx_weekly_data": (
                {
                    "type": "object",
                        "properties": {
                            "symbol": {"type": "string"},
                        },
                        "required": ["symbol"]
                    },
                    "Get weekly foreign exchange rates for a given symbol"
                ),

                "get_fx_monthly_data": (
                    {
                        "type": "object",
                        "properties": {
                            "symbol": {"type": "string"},
                        },
                        "required": ["symbol"]
                    },
                    "Get monthly foreign exchange rates for a given symbol"
                ),
            "get_exchange_rates_trending": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                    },
                    "required": ["symbol"]
                },
                "Get trending exchange rates for a given symbol"
            ),
            "get_fx_daily_data": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                    },
                    "required": ["symbol"]
                },
                "Get daily FX rates for a given symbol"
            ),
            "get_fx_weekly_data": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                    },
                    "required": ["symbol"]
                },
                "Get weekly FX rates for a given symbol"
            ),
            "get_fx_monthly_data": (
                {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                    },
                    "required": ["symbol"]
                },
                "Get monthly FX rates for a given symbol"
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
            "get_copper_price": (
                {"type": "object", "properties": {"interval": {"type": "string", "enum": ["monthly", "quarterly", "annual"], "default": "monthly"}},
                 "required": []},
                "Get global copper price data"
            ),
            "get_aluminum_price": (
                {"type": "object", "properties": {"interval": {"type": "string", "enum": ["monthly", "quarterly", "annual"], "default": "monthly"}},
                 "required": []},
                "Get global aluminum price data"
            ),
            "get_wheat_price": (
                {"type": "object", "properties": {"interval": {"type": "string", "enum": ["monthly", "quarterly", "annual"], "default": "monthly"}},
                 "required": []},
                "Get global wheat price data"
            ),
            "get_corn_price": (
                {"type": "object", "properties": {"interval": {"type": "string", "enum": ["monthly", "quarterly", "annual"], "default": "monthly"}},
                 "required": []},
                "Get global corn price data"
            ),
            "get_cotton_price": (
                {"type": "object", "properties": {"interval": {"type": "string", "enum": ["monthly", "quarterly", "annual"], "default": "monthly"}},
                 "required": []},
                "Get global cotton price data"
            ),
            "get_sugar_price": (
                {"type": "object", "properties": {"interval": {"type": "string", "enum": ["monthly", "quarterly", "annual"], "default": "monthly"}},
                 "required": []},
                "Get global sugar price data"
            ),
            "get_coffee_price": (
                {"type": "object", "properties": {"interval": {"type": "string", "enum": ["monthly", "quarterly", "annual"], "default": "monthly"}},
                 "required": []},
                "Get global coffee price data"
            ),
            "get_all_commodities_price_index": (
                {"type": "object", "properties": {"interval": {"type": "string", "enum": ["monthly", "quarterly", "annual"], "default": "monthly"}},
                 "required": []},
                "Get Global Price Index of All Commodities"
            ),
            "get_real_gdp": (
                {"type": "object", "properties": {"interval": {"type": "string", "enum": ["quarterly", "annual"], "default": "quarterly"}},
                 "required": []},
                "Get Real GDP data"
            ),
            "get_real_gdp_per_capita": (
                {"type": "object", "properties": {}},
                "Get Real GDP per capita data"
            ),
            "get_treasury_yield": (
                {"type": "object", "properties": {"interval": {"type": "string", "enum": ["daily", "weekly", "monthly"], "default": "weekly"}, "maturity": {"type": "string", "enum": ["3month", "2year", "5year", "10year", "30year"], "default": "5year"}},
                 "required": []},
                "Get Treasury yield data"
            ),
            "get_federal_funds_rate": (
                {"type": "object", "properties": {"interval": {"type": "string", "enum": ["daily", "weekly", "monthly"], "default": "weekly"}},
                 "required": []},
                "Get Federal Funds Rate data"
            ),
            "get_cpi": (
                {"type": "object", "properties": {"interval": {"type": "string", "enum": ["monthly", "quarterly", "annual"], "default": "monthly"}},
                 "required": []},
                "Get Consumer Price Index data"
            ),
            "get_inflation_rate": (
                {"type": "object", "properties": {}},
                "Get inflation rate data"
            ),
            "get_retail_sales": (
                {"type": "object", "properties": {}},
                "Get retail sales data"
            ),
            "get_durables": (
                {"type": "object", "properties": {}},
                "Get durable goods orders data"
            ),
            "get_unemployment_rate": (
                {"type": "object", "properties": {}},
                "Get unemployment rate data"
            ),
            "get_non_farm_payrolls": (
                {"type": "object", "properties": {}},
                "Get non-farm payrolls data"
            ),
            "get_sma": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string", "description": "Stock symbol (e.g., AAPL)"},
                    "interval": {"type": "string", "enum": ["1min", "5min", "15min", "30min", "60min", "daily", "weekly", "monthly"], "default": "daily"},
                    "time_period": {"type": "integer", "description": "Number of data points used to calculate each moving average value", "default": 20},
                    "series_type": {"type": "string", "enum": ["open", "high", "low", "close"], "default": "close"}
                }, "required": ["symbol"]},
                "Get Simple Moving Average (SMA) data for a given stock symbol"
            ),
            "get_ema": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"},
                    "time_period": {"type": "integer", "default": 20},
                    "series_type": {"type": "string", "default": "close"}
                }, "required": ["symbol"]},
                "Get Exponential Moving Average (EMA) data"
            ),
            "get_wma": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"},
                    "time_period": {"type": "integer", "default": 20},
                    "series_type": {"type": "string", "default": "close"}
                }, "required": ["symbol"]},
                "Get Weighted Moving Average (WMA) data"
            ),
            "get_dema": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"},
                    "time_period": {"type": "integer", "default": 20},
                    "series_type": {"type": "string", "default": "close"}
                }, "required": ["symbol"]},
                "Get Double Exponential Moving Average (DEMA) data"
            ),
            "get_tema": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"},
                    "time_period": {"type": "integer", "default": 20},
                    "series_type": {"type": "string", "default": "close"}
                }, "required": ["symbol"]},
                "Get Triple Exponential Moving Average (TEMA) data"
            ),
            "get_trima": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"},
                    "time_period": {"type": "integer", "default": 20},
                    "series_type": {"type": "string", "default": "close"}
                }, "required": ["symbol"]},
                "Get Triangular Moving Average (TRIMA) data"
            ),
            "get_kama": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"},
                    "time_period": {"type": "integer", "default": 20},
                    "series_type": {"type": "string", "default": "close"}
                }, "required": ["symbol"]},
                "Get Kaufman Adaptive Moving Average (KAMA) data"
            ),
            "get_mama": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"},
                    "fastlimit": {"type": "number", "default": 0.5},
                    "slowlimit": {"type": "number", "default": 0.05},
                    "series_type": {"type": "string", "default": "close"}
                }, "required": ["symbol"]},
                "Get MESA Adaptive Moving Average (MAMA) data"
            ),
            "get_vwap": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Volume Weighted Average Price (VWAP) data"
            ),
            "get_tthree": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"},
                    "time_period": {"type": "integer", "default": 20},
                    "series_type": {"type": "string", "default": "close"}
                }, "required": ["symbol"]},
                "Get Triple Exponential Moving Average (T3) data"
            ),
            "get_macdext": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"},
                    "fastperiod": {"type": "integer", "default": 12},
                    "slowperiod": {"type": "integer", "default": 26},
                    "signalperiod": {"type": "integer", "default": 9},
                    "series_type": {"type": "string", "default": "close"}
                }, "required": ["symbol"]},
                "Get MACD with additional parameters"
            ),
            "get_stoch": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Stochastic Oscillator data"
            ),
            "get_stochfast": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Stochastic Fast Oscillator data"
            ),
            "get_rsi": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"},
                    "time_period": {"type": "integer", "default": 14},
                    "series_type": {"type": "string", "default": "close"}
                }, "required": ["symbol"]},
                "Get Relative Strength Index (RSI) data"
            ),
            "get_stochrsi": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Stochastic RSI data"
            ),
            "get_willr": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Williams %R data"
            ),
            "get_adx": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Average Directional Index (ADX) data"
            ),
            "get_adxr": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Average Directional Movement Index Rating (ADXR) data"
            ),
            "get_apo": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Absolute Price Oscillator (APO) data"
            ),
            "get_ppo": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Percentage Price Oscillator (PPO) data"
            ),
            "get_mom": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Momentum data"
            ),
            "get_bop": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Balance of Power (BOP) data"
            ),
            "get_cci": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Commodity Channel Index (CCI) data"
            ),
            "get_cmo": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Chande Momentum Oscillator (CMO) data"
            ),
            "get_roc": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Rate of Change (ROC) data"
            ),
            "get_rocr": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Rate of Change Ratio (ROCR) data"
            ),
            "get_aroon": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Aroon Indicator data"
            ),
            "get_aroonosc": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Aroon Oscillator data"
            ),
            "get_mfi": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Money Flow Index (MFI) data"
            ),
            "get_trix": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get 1 day rate of change of a Triple Exponential Average (TRIX) data"
            ),
            "get_ultosc": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Ultimate Oscillator data"
            ),
            "get_dx": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Directional Movement Index (DX) data"
            ),
            "get_minus_di": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Minus Directional Indicator (-DI) data"
            ),
            "get_plus_di": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Plus Directional Indicator (+DI) data"
            ),
            "get_minus_dm": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Minus Directional Movement (-DM) data"
            ),
            "get_plus_dm": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Plus Directional Movement (+DM) data"
            ),
            "get_bbands": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Bollinger Bands data"
            ),
            "get_midpoint": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Midpoint data"
            ),
            "get_midprice": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Midprice data"
            ),
            "get_sar": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Parabolic SAR data"
            ),
            "get_trange": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get True Range data"
            ),
            "get_atr": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Average True Range (ATR) data"
            ),
            "get_natr": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Normalized Average True Range (NATR) data"
            ),
            "get_ad": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Chaikin A/D Line data"
            ),
            "get_adosc": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get Chaikin A/D Oscillator data"
            ),
            "get_obv": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"}
                }, "required": ["symbol"]},
                "Get On-Balance Volume (OBV) data"
            ),
            "get_ht_trendline": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"},
                    "series_type": {"type": "string", "default": "close"}
                }, "required": ["symbol"]},
                "Get Hilbert Transform - Trendline data"
            ),
            "get_ht_sine": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"},
                    "series_type": {"type": "string", "default": "close"}
                }, "required": ["symbol"]},
                "Get Hilbert Transform - SineWave data"
            ),
            "get_ht_trendmode": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"},
                    "series_type": {"type": "string", "default": "close"}
                }, "required": ["symbol"]},
                "Get Hilbert Transform - Trend Mode data"
            ),
            "get_ht_dcperiod": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"},
                    "series_type": {"type": "string", "default": "close"}
                }, "required": ["symbol"]},
                "Get Hilbert Transform - Dominant Cycle Period data"
            ),
            "get_ht_dcphase": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"},
                    "series_type": {"type": "string", "default": "close"}
                }, "required": ["symbol"]},
                "Get Hilbert Transform - Dominant Cycle Phase data"
            ),
            "get_ht_phasor": (
                {"type": "object", "properties": {
                    "symbol": {"type": "string"},
                    "interval": {"type": "string", "default": "daily"},
                    "series_type": {"type": "string", "default": "close"}
                }, "required": ["symbol"]},
                "Get Hilbert Transform - Phasor data"
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

    async def _get_time_series_weekly(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        data = await self.av_client.get_time_series_weekly(symbol)
        return json.dumps(data, indent=2)

    async def _get_time_series_monthly(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        data = await self.av_client.get_time_series_monthly(symbol)
        return json.dumps(data, indent=2)

    async def _get_time_series_monthly_adjusted(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        data = await self.av_client.get_time_series_monthly_adjusted(symbol)
        return json.dumps(data, indent=2)

    async def _search_ticker(self, args: Dict[str, Any]) -> str:
        keywords = args["keywords"]
        data = await self.av_client.search_ticker(keywords)
        return json.dumps(data, indent=2)

    async def _get_global_market_status(self, args: Dict[str, Any]) -> str:
        data = await self.av_client.get_global_market_status()
        return json.dumps(data, indent=2)

    async def _get_top_gainers_losers(self, args: Dict[str, Any]) -> str:
        data = await self.av_client.get_top_gainers_losers()
        return json.dumps(data, indent=2)

    async def _get_quote_endpoint_trending(self, args: Dict[str, Any]) -> str:
        data = await self.av_client.get_quote_endpoint_trending()
        return json.dumps(data, indent=2)

    async def _get_historical_options(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        data = await self.av_client.get_historical_options(symbol)
        return json.dumps(data, indent=2)

    async def _get_alpha_intelligence(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        data = await self.av_client.get_alpha_intelligence(symbol)
        return json.dumps(data, indent=2)

    async def _get_news_sentiments_trending(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        topics = args.get("topics")
        data = await self.av_client.get_news_sentiments_trending(symbol=symbol, topics=topics)
        return json.dumps(data, indent=2)

    async def _get_earnings_call_transcript(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        quarter = args.get("quarter")
        year = args.get("year")
        data = await self.av_client.get_earnings_call_transcript(symbol, quarter, year)
        return json.dumps(data, indent=2)

    async def _get_insider_transactions_trending(self, args: Dict[str, Any]) -> str:
        data = await self.av_client.get_insider_transactions_trending()
        return json.dumps(data, indent=2)

    async def _get_analytics_fixed_window(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        window = args.get("window", "30")
        data = await self.av_client.get_analytics_fixed_window(symbol, window)
        return json.dumps(data, indent=2)

    async def _get_analytics_sliding_window(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        window = args.get("window", "30")
        data = await self.av_client.get_analytics_sliding_window(symbol, window)
        return json.dumps(data, indent=2)

    async def _get_fundamental_data(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_fundamental_data(symbol)
        return json.dumps(data, indent=2)

    async def _get_company_overview_trending(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_company_overview_trending(symbol)
        return json.dumps(data, indent=2)

    async def _get_etf_profile_holdings(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_etf_profile_holdings(symbol)
        return json.dumps(data, indent=2)

    async def _get_corporate_action_dividends(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_corporate_action_dividends(symbol)
        return json.dumps(data, indent=2)

    async def _get_corporate_action_splits(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_corporate_action_splits(symbol)
        return json.dumps(data, indent=2)

    async def _get_income_statement(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_income_statement(symbol)
        return json.dumps(data, indent=2)

    async def _get_balance_sheet(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_balance_sheet(symbol)
        return json.dumps(data, indent=2)

    ###
    async def _get_cash_flow(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_cash_flow(symbol)
        return json.dumps(data, indent=2)

    async def _get_earnings_trending(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_earnings_trending(symbol)
        return json.dumps(data, indent=2)

    async def _get_listing_delisting_status(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_listing_delisting_status(symbol)
        return json.dumps(data, indent=2)

    async def _get_earnings_calendar(self, args: Dict[str, Any]) -> str:
        region = args.get("region", "US")
        data = await self.av_client.get_earnings_calendar(region)
        return json.dumps(data, indent=2)

    async def _get_ipo_calendar(self, args: Dict[str, Any]) -> str:
        region = args.get("region", "US")
        data = await self.av_client.get_ipo_calendar(region)
        return json.dumps(data, indent=2)

    async def _get_exchange_rates_trending(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_exchange_rates_trending(symbol)
        return json.dumps(data, indent=2)

    async def _get_fx_daily_data(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_fx_daily_data(symbol)
        return json.dumps(data, indent=2)

    async def _get_fx_weekly_data(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_fx_weekly_data(symbol)
        return json.dumps(data, indent=2)

    async def _get_fx_monthly_data(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_fx_monthly_data(symbol)
        return json.dumps(data, indent=2)

    async def _get_exchange_rates_trending(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_exchange_rates_trending(symbol)
        return json.dumps(data, indent=2)

    async def _get_fx_daily_data(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_fx_daily_data(symbol)
        return json.dumps(data, indent=2)

    async def _get_fx_weekly_data(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_fx_weekly_data(symbol)
        return json.dumps(data, indent=2)

    async def _get_fx_monthly_data(self, args: Dict[str, Any]) -> str:
        symbol = args.get("symbol")
        if not symbol:
            raise ValueError("symbol is required")
        data = await self.av_client.get_fx_monthly_data(symbol)
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
    
    async def _get_copper_price(self, args: Dict[str, Any]) -> str:
        interval = args.get("interval", "monthly")
        data = await self.av_client.get_copper_price(interval)
        return json.dumps(data, indent=2)
    
    async def _get_aluminum_price(self, args: Dict[str, Any]) -> str:
        interval = args.get("interval", "monthly")
        data = await self.av_client.get_aluminum_price(interval)
        return json.dumps(data, indent=2)
    
    async def _get_wheat_price(self, args: Dict[str, Any]) -> str:
        interval = args.get("interval", "monthly")
        data = await self.av_client.get_wheat_price(interval)
        return json.dumps(data, indent=2)
    
    async def _get_corn_price(self, args: Dict[str, Any]) -> str:
        interval = args.get("interval", "monthly")
        data = await self.av_client.get_corn_price(interval)
        return json.dumps(data, indent=2)
    
    async def _get_cotton_price(self, args: Dict[str, Any]) -> str:
        interval = args.get("interval", "monthly")
        data = await self.av_client.get_cotton_price(interval)
        return json.dumps(data, indent=2)
    
    async def _get_sugar_price(self, args: Dict[str, Any]) -> str:
        interval = args.get("interval", "monthly")
        data = await self.av_client.get_sugar_price(interval)
        return json.dumps(data, indent=2)
    
    async def _get_coffee_price(self, args: Dict[str, Any]) -> str:
        interval = args.get("interval", "monthly")
        data = await self.av_client.get_coffee_price(interval)
        return json.dumps(data, indent=2)
    
    async def _get_all_commodities_price_index(self, args: Dict[str, Any]) -> str:
        interval = args.get("interval", "monthly")
        data = await self.av_client.get_global_price_index(interval)
        return json.dumps(data, indent=2)
    
    async def _get_real_gdp(self, args: Dict[str, Any]) -> str:
        interval = args.get("interval", "quarterly")
        data = await self.av_client.get_real_gdp(interval)
        return json.dumps(data, indent=2)
    
    async def _get_real_gdp_per_capita(self, args: Dict[str, Any]) -> str:
        data = await self.av_client.get_real_gdp_per_capita()
        return json.dumps(data, indent=2)
    
    async def _get_treasury_yield(self, args: Dict[str, Any]) -> str:
        interval = args.get("interval", "weekly")
        maturity = args.get("maturity", "5year")
        data = await self.av_client.get_treasury_yield(interval, maturity)
        return json.dumps(data, indent=2)
    
    async def _get_federal_funds_rate(self, args: Dict[str, Any]) -> str:
        interval = args.get("interval", "weekly")
        data = await self.av_client.fed_funds_rate(interval)
        return json.dumps(data, indent=2)
    
    async def _get_cpi(self, args: Dict[str, Any]) -> str:
        interval = args.get("interval", "monthly")
        data = await self.av_client.cpi(interval)
        return json.dumps(data, indent=2)
    
    async def _get_inflation_rate(self, args: Dict[str, Any]) -> str:
        data = await self.av_client.get_inflation_rate()
        return json.dumps(data, indent=2)
    
    async def _get_retail_sales(self, args: Dict[str, Any]) -> str:
        data = await self.av_client.get_retail_sales()
        return json.dumps(data, indent=2)
    
    async def _get_durables(self, args: Dict[str, Any]) -> str:
        data = await self.av_client.get_durables_orders()
        return json.dumps(data, indent=2)
    
    async def _get_unemployment_rate(self, args: Dict[str, Any]) -> str:
        data = await self.av_client.get_unemployment_rate()
        return json.dumps(data, indent=2)
    
    async def _get_non_farm_payrolls(self, args: Dict[str, Any]) -> str:
        data = await self.av_client.get_nonfarm_payrolls()
        return json.dumps(data, indent=2)
    
    async def _get_sma(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        time_period = args.get("time_period", 20)
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_sma(symbol, interval, time_period, series_type)
        return json.dumps(data, indent=2)

    async def _get_ema(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        time_period = args.get("time_period", 20)
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_ema(symbol, interval, time_period, series_type)
        return json.dumps(data, indent=2)

    async def _get_wma(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        time_period = args.get("time_period", 20)
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_wma(symbol, interval, time_period, series_type)
        return json.dumps(data, indent=2)

    async def _get_dema(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        time_period = args.get("time_period", 20)
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_dema(symbol, interval, time_period, series_type)
        return json.dumps(data, indent=2)

    async def _get_tema(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        time_period = args.get("time_period", 20)
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_tema(symbol, interval, time_period, series_type)
        return json.dumps(data, indent=2)

    async def _get_trima(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        time_period = args.get("time_period", 20)
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_trima(symbol, interval, time_period, series_type)
        return json.dumps(data, indent=2)

    async def _get_kama(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        time_period = args.get("time_period", 20)
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_kama(symbol, interval, time_period, series_type)
        return json.dumps(data, indent=2)

    async def _get_mama(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        fastlimit = args.get("fastlimit", 0.5)
        slowlimit = args.get("slowlimit", 0.05)
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_mama(symbol, interval, fastlimit, slowlimit, series_type)
        return json.dumps(data, indent=2)

    async def _get_vwap(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_vwap(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_tthree(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        time_period = args.get("time_period", 20)
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_tthree(symbol, interval, time_period, series_type)
        return json.dumps(data, indent=2)

    async def _get_macdext(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        fastperiod = args.get("fastperiod", 12)
        slowperiod = args.get("slowperiod", 26)
        signalperiod = args.get("signalperiod", 9)
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_macdext(symbol, interval, fastperiod, slowperiod, signalperiod, series_type)
        return json.dumps(data, indent=2)

    async def _get_stoch(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_stoch(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_stochfast(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_stochfast(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_rsi(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        time_period = args.get("time_period", 14)
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_rsi(symbol, interval, time_period, series_type)
        return json.dumps(data, indent=2)

    async def _get_stochrsi(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_stochrsi(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_willr(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_willr(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_adx(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_adx(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_adxr(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_adxr(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_apo(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_apo(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_ppo(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_ppo(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_mom(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_mom(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_bop(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_bop(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_cci(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_cci(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_cmo(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_cmo(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_roc(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_roc(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_rocr(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_rocr(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_aroon(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_aroon(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_aroonosc(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_aroonosc(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_mfi(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_mfi(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_trix(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_trix(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_ultosc(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_ultosc(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_dx(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_dx(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_minus_di(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_minus_di(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_plus_di(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_plus_di(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_minus_dm(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_minus_dm(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_plus_dm(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_plus_dm(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_bbands(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_bbands(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_midpoint(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_midpoint(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_midprice(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_midprice(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_sar(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_sar(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_trange(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_trange(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_atr(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_atr(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_natr(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_natr(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_ad(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_ad(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_adosc(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_adosc(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_obv(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        data = await self.av_client.get_obv(symbol, interval)
        return json.dumps(data, indent=2)

    async def _get_ht_trendline(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_ht_trendline(symbol, interval, series_type)
        return json.dumps(data, indent=2)

    async def _get_ht_sine(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_ht_sine(symbol, interval, series_type)
        return json.dumps(data, indent=2)

    async def _get_ht_trendmode(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_ht_trendmode(symbol, interval, series_type)
        return json.dumps(data, indent=2)

    async def _get_ht_dcperiod(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_ht_dcperiod(symbol, interval, series_type)
        return json.dumps(data, indent=2)

    async def _get_ht_dcphase(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_ht_dcphase(symbol, interval, series_type)
        return json.dumps(data, indent=2)

    async def _get_ht_phasor(self, args: Dict[str, Any]) -> str:
        symbol = args["symbol"].upper()
        interval = args.get("interval", "daily")
        series_type = args.get("series_type", "close")
        data = await self.av_client.get_ht_phasor(symbol, interval, series_type)
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
