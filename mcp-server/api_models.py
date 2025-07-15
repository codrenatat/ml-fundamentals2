from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, List

class StockPriceRequest(BaseModel):
    """Request model for intraday stock price"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("5min", description="Time interval (1min, 5min, 15min, 30min, 60min)")

class TimeSeriesWeeklyRequest(BaseModel):
    """Request model for weekly time series data"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")
    interval: Optional[str] = Field("weekly", description="Time interval, default is weekly")

class TimeSeriesMonthlyRequest(BaseModel):
    """Request model for monthly time series data"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")
    interval: Optional[str] = Field("monthly", description="Time interval, default is monthly")

class TimeSeriesMonthlyAdjustedRequest(BaseModel):
    """Request model for monthly adjusted time series data"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")
    interval: Optional[str] = Field("monthly", description="Time interval, default is monthly")

class SearchTickerRequest(BaseModel):
    """Request model for searching ticker symbols"""
    keywords: str = Field(..., description="Search query keywords (e.g., Apple)")

class GlobalMarketStatusRequest(BaseModel):
    """Request model for global market status"""
    # No required fields, but can add optional region if needed
    region: Optional[str] = Field(None, description="Region code for market status (e.g., US)")

class TopGainersLosersRequest(BaseModel):
    """Request model for top gainers and losers"""
    region: Optional[str] = Field("US", description="Region to fetch top gainers and losers for")

class QuoteEndpointTrendingRequest(BaseModel):
    """Request model for quote endpoint trending"""
    interval: Optional[str] = Field("monthly", description="Time interval (daily, weekly, monthly)")

class HistoricalOptionsRequest(BaseModel):
    """Request model for historical options data"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")

class AlphaIntelligenceRequest(BaseModel):
    """Request model for Alpha Intelligence™ data"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")

class NewsSentimentsTrendingRequest(BaseModel):
    """Request model for News & Sentiments Trending"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")

class EarningsCallTranscriptRequest(BaseModel):
    """Request model for Earnings Call Transcript"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")

class InsiderTransactionsTrendingRequest(BaseModel):
    """Request model for Insider Transactions Trending"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")

class AnalyticsFixedWindowRequest(BaseModel):
    """Request model for Analytics (Fixed Window) data"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")
    window: Optional[int] = Field(14, description="Window size for analytics")

class AnalyticsSlidingWindowRequest(BaseModel):
    """Request model for Analytics (Sliding Window) data"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")
    window: Optional[int] = Field(14, description="Window size for analytics")

class FundamentalDataRequest(BaseModel):
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")

class CompanyOverviewTrendingRequest(BaseModel):
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")

class ETFProfileHoldingsRequest(BaseModel):
    symbol: str = Field(..., description="ETF symbol (e.g., SPY)")

class CorporateActionDividendsRequest(BaseModel):
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")

class CorporateActionSplitsRequest(BaseModel):
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")

class IncomeStatementRequest(BaseModel):
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")

class BalanceSheetRequest(BaseModel):
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")

class CashFlowRequest(BaseModel):
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")

class EarningsTrendingRequest(BaseModel):
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")

class ListingDelistingStatusRequest(BaseModel):
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL)")

class EarningsCalendarRequest(BaseModel):
    region: Optional[str] = Field("US", description="Region to fetch earnings calendar for (e.g., US)")

class IPOCalendarRequest(BaseModel):
    region: Optional[str] = Field("US", description="Region to fetch IPO calendar for (e.g., US)")

class ExchangeRatesTrendingRequest(BaseModel):
    symbol: str = Field(..., description="Currency pair symbol (e.g., EURUSD)")

class FXDailyRequest(BaseModel):
    symbol: str = Field(..., description="Currency pair symbol for daily data (e.g., USDJPY)")

class FXWeeklyRequest(BaseModel):
    symbol: str = Field(..., description="Currency pair symbol for weekly data (e.g., GBPUSD)")

class FXMonthlyRequest(BaseModel):
    symbol: str = Field(..., description="Currency pair symbol for monthly data (e.g., AUDUSD)")

class ExchangeRatesTrendingRequest(BaseModel):
    symbol: str = Field(..., description="Currency pair symbol (e.g., EURUSD)")

class FXDailyRequest(BaseModel):
    symbol: str = Field(..., description="Currency pair symbol for daily data (e.g., USDJPY)")

class FXWeeklyRequest(BaseModel):
    symbol: str = Field(..., description="Currency pair symbol for weekly data (e.g., GBPUSD)")

class FXMonthlyRequest(BaseModel):
    symbol: str = Field(..., description="Currency pair symbol for monthly data (e.g., AUDUSD)")



class WTIPriceRequest(BaseModel):
    """Request model for WTI crude oil price"""
    interval: Optional[str] = Field("monthly", description="Time interval (daily, weekly, monthly)")

class BrentPriceRequest(BaseModel):
    """Request model for Brent crude oil price"""
    interval: Optional[str] = Field("monthly", description="Time interval (daily, weekly, monthly)")

class NaturalGasPriceRequest(BaseModel):
    """Request model for Natural Gas price"""
    interval: Optional[str] = Field("monthly", description="Time interval (daily, weekly, monthly)")

class CopperPriceRequest(BaseModel):
    """Request for global copper price"""
    interval: Optional[str] = Field("monthly", description="Time interval (monthly, quarterly, annual)")

class AluminiumPriceRequest(BaseModel):
    """Request for global aluminium price"""
    interval: Optional[str] = Field("monthly", description="Time interval (monthly, quarterly, annual)")

class WheatPriceRequest(BaseModel):
    """Request for global wheat price"""
    interval: Optional[str] = Field("monthly", description="Time interval (monthly, quarterly, annual)")

class CornPriceRequest(BaseModel):
    """Request for global corn price"""
    interval: Optional[str] = Field("monthly", description="Time interval (monthly, quarterly, annual)")

class CottonPriceRequest(BaseModel):
    """Request for global cotton price"""
    interval: Optional[str] = Field("monthly", description="Time interval (monthly, quarterly, annual)")

class SugarPriceRequest(BaseModel):
    """Request for global sugar price"""
    interval: Optional[str] = Field("monthly", description="Time interval (monthly, quarterly, annual)")

class CoffeePriceRequest(BaseModel):
    """Request for global coffee price"""
    interval: Optional[str] = Field("monthly", description="Time interval (monthly, quarterly, annual)")

class GPIACRequest(BaseModel):
    """Request for Global Price Index of All Commodities"""
    interval: Optional[str] = Field("monthly", description="Time interval (monthly, quarterly, annual)")

class RealGDPRequest(BaseModel):
    """Request for annual and quarterly Real GDP of the United States."""
    interval: Optional[str] = Field("quarterly", description="Time interval (quarterly, annual)")

class RealGDPPerCapitaRequest(BaseModel):
    """Request for quarterly Real GDP Per Capita of the United States."""

class TreasuryYieldRequest(BaseModel):
    """Request model for US Treasury Yield"""
    interval: Optional[str] = Field("daily", description="Time interval (daily, weekly, monthly)")
    maturity: Optional[str] = Field("5year", description="Maturity timeline (e.g., 3month, 2year, 5year, etc.)")

class FederalFundsRateRequest(BaseModel):
    """Request model for Federal Funds Rate"""
    interval: Optional[str] = Field("daily", description="Time interval (daily, weekly, monthly)")

class ConsumerPriceIndexRequest(BaseModel):
    """Request model for Consumer Price Index (CPI)"""
    interval: Optional[str] = Field("monthly", description="Time interval (monthly, semiannual)")

class InflationRateRequest(BaseModel):
    """Request model for annual Inflation Rate"""

class RetailSalesRequest(BaseModel):
    """Request the monthly Advance Retail Sales: Retail Trade data of the United States."""

class DurablesRequest(BaseModel):
    """Request the monthly manufacturers' new orders of durable goods in the United States."""

class UnemploymentRateRequest(BaseModel):
    """Request the monthly unemployment rate of the United States."""

class NonFarmPayrollsRequest(BaseModel):
    """Request the monthly Non-Farm Payrolls data of the United States."""

class SMARequest(BaseModel):
    """Request model for Simple Moving Average (SMA)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(20, description="Number of data points used to calculate each moving average value")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class EMARequest(BaseModel):
    """Request model for Exponential Moving Average (EMA)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(20, description="Number of data points used to calculate each moving average value")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class WMARequest(BaseModel):
    """Request model for Weighted Moving Average (WMA)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(20, description="Number of data points used to calculate each moving average value")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class DEMARequest(BaseModel):
    """Request model for Double Exponential Moving Average (DEMA)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(20, description="Number of data points used to calculate each moving average value")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class TEMARequest(BaseModel):
    """Request model for Triple Exponential Moving Average (TEMA)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(20, description="Number of data points used to calculate each moving average value")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class TRIMARequest(BaseModel):
    """Request model for Triangular Moving Average (TRIMA)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(20, description="Number of data points used to calculate each moving average value")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class KAMARequest(BaseModel):
    """Request model for Kaufman's Adaptive Moving Average (KAMA)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(20, description="Number of data points used to calculate each moving average value")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class MAMARequest(BaseModel):
    """Request model for MESA Adaptive Moving Average (MAMA)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    fast_limit: Optional[float] = Field(0.5, description="Fast limit for MAMA calculation")
    slow_limit: Optional[float] = Field(0.05, description="Slow limit for MAMA calculation")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

#class VWAPRequest(BaseModel):
#    """Request model for Volume Weighted Average Price (VWAP)"""
#    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
#    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")

class T3Request(BaseModel):
    """Request model for triple exponential moving average"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(20, description="Number of data points used to calculate each moving average value")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

#class MACDRequest(BaseModel):
#    """Request model for Moving Average Convergence Divergence (MACD)"""
#    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
#    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
#    fast_period: Optional[int] = Field(12, description="Fast period for MACD calculation")
#    slow_period: Optional[int] = Field(26, description="Slow period for MACD calculation")
#    signal_period: Optional[int] = Field(9, description="Signal period for MACD calculation")
#    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class MACDEXTRequest(BaseModel):
    """Request model for MACD with customizable parameters"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    fastperiod: Optional[int] = Field(12, description="Fast period for MACD calculation")
    slowperiod: Optional[int] = Field(26, description="Slow period for MACD calculation")
    signalperiod: Optional[int] = Field(9, description="Signal period for MACD calculation")
    fastmatype: Optional[int] = Field(0, description="Type of moving average for fast line (0=EMA, 1=SMA)")
    slowmatype: Optional[int] = Field(0, description="Type of moving average for slow line (0=EMA, 1=SMA)")
    signalmatype: Optional[int] = Field(0, description="Type of moving average for signal line (0=EMA, 1=SMA)")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class STOCHRequest(BaseModel):
    """Request model for Stochastic Oscillator"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    fastkperiod: Optional[int] = Field(14, description="Fast %K period")
    slowkperiod: Optional[int] = Field(3, description="Slow %K period")
    slowdperiod: Optional[int] = Field(3, description="Slow %D period")
    slowkmatype: Optional[int] = Field(0, description="Type of moving average for Slow %K (0=EMA, 1=SMA)")
    slowdmatype: Optional[int] = Field(0, description="Type of moving average for Slow %D (0=EMA, 1=SMA)")

class STOCHFRequest(BaseModel):
    """Request model for Stochastic Fast Oscillator"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    fastkperiod: Optional[int] = Field(14, description="Fast %K period")
    fastdperiod: Optional[int] = Field(3, description="Fast %D period")
    fastdmatype: Optional[int] = Field(0, description="Type of moving average for Fast %D (0=EMA, 1=SMA)")

class RSIRequest(BaseModel):
    """"Request model for Relative Strength Index (RSI)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate RSI")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class STOCHRSIRequest(BaseModel):
    """Request model for Stochastic Relative Strength Index (StochRSI)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate StochRSI")
    fastkperiod: Optional[int] = Field(14, description="Fast %K period")
    fastdperiod: Optional[int] = Field(3, description="Fast %D period")
    fastdmatype: Optional[int] = Field(0, description="Type of moving average for Fast %D (0=EMA, 1=SMA)")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class WILLRRequest(BaseModel):
    """Request model for Williams %R"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate Williams %R")

class ADXRequest(BaseModel):
    """Request model for Average Directional Index (ADX)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate ADX")

class ADXRRequest(BaseModel):
    """Request model for Average Directional Movement Index Rating (ADXR)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate ADXR")

class APORequest(BaseModel):
    """Request model for Absolute Price Oscillator (APO)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    fastperiod: Optional[int] = Field(12, description="Fast period for APO calculation")
    slowperiod: Optional[int] = Field(26, description="Slow period for APO calculation")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class PPORequest(BaseModel):
    """Request model for Percentage Price Oscillator (PPO)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    fastperiod: Optional[int] = Field(12, description="Fast period for PPO calculation")
    slowperiod: Optional[int] = Field(26, description="Slow period for PPO calculation")
    matype: Optional[int] = Field(0, description="Type of moving average for PPO (0=EMA, 1=SMA)")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class MOMRequest(BaseModel):
    """Request model for Momentum"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(10, description="Number of data points used to calculate momentum")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class BOPRequest(BaseModel):
    """Request model for Balance of Power (BOP)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")

class CCIRequest(BaseModel):
    """Request model for Commodity Channel Index (CCI)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(20, description="Number of data points used to calculate CCI")

class CMORequest(BaseModel):
    """Request model for Chande Momentum Oscillator (CMO)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate CMO")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class ROCRequest(BaseModel):
    """Request model for Rate of Change (ROC)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(10, description="Number of data points used to calculate ROC")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class ROCRRequest(BaseModel):
    """Request model for Rate of Change Ratio (ROCR)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(10, description="Number of data points used to calculate ROCR")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class AROONRequest(BaseModel):
    """Request model for Aroon Indicator"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate Aroon")

class AROONOSCRequest(BaseModel):
    """Request model for Aroon Oscillator values"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate Aroon Oscillator")

class MFIRequest(BaseModel):
    """Request model for Money Flow Index (MFI)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate MFI")

class TRIXRequest(BaseModel):
    """Request model for the 1-day rate of change of a triple exponentially smoothed moving average"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(30, description="Number of data points used to calculate TRIX")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class ULTOSCRequest(BaseModel):
    """Request model for Ultimate Oscillator"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    timeperiod1: Optional[int] = Field(7, description="First time period for calculation")
    timeperiod2: Optional[int] = Field(14, description="Second time period for calculation")
    timeperiod3: Optional[int] = Field(28, description="Third time period for calculation")

class DXRequest(BaseModel):
    """Request model for directional movement index"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(7, description="First time period for calculation")

class MINUS_DIRequest(BaseModel):
    """Request model for Minus Directional Indicator"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate Minus Directional Indicator")

class PLUS_DIRequest(BaseModel):
    """Request model for Plus Directional Indicator"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate Plus Directional Indicator")

class MINUS_DMRequest(BaseModel):
    """Request model for Minus Directional Movement"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate Minus Directional Movement")

class PLUS_DMRequest(BaseModel):
    """Request model for Plus Directional Movement"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate Plus Directional Movement")

class BBANDSRequest(BaseModel):
    """Request model for Bollinger Bands"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(20, description="Number of data points used to calculate Bollinger Bands")
    nbdevup: Optional[int] = Field(2, description="Number of standard deviations for upper band")
    nbdevdn: Optional[int] = Field(2, description="Number of standard deviations for lower band")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class MIDPOINTRequest(BaseModel):
    """Request model for Midpoint"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate midpoint")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class MIDPRICERequest(BaseModel):
    """Request model for midpoint price values"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate midpoint price")

class SARRequest(BaseModel):
    """Request model for Parabolic SAR (Stop and Reverse)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    acceleration: Optional[float] = Field(0.02, description="Acceleration factor for SAR calculation")
    maximum: Optional[float] = Field(0.2, description="Maximum value for acceleration factor")

class TRANGE(BaseModel):
    """Request model for True Range"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")

class ATRRequest(BaseModel):
    """Request model for Average True Range (ATR)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate ATR")

class NATRRequest(BaseModel):
    """Request model for Normalized Average True Range (NATR)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    time_period: Optional[int] = Field(14, description="Number of data points used to calculate NATR")

class ADRequest(BaseModel):
    """Request model for Chaikin A/D Line"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")

class ADOSCRequest(BaseModel):
    """Request model for Chaikin A/D Oscillator"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    fastperiod: Optional[int] = Field(3, description="Fast period for A/D Oscillator calculation")
    slowperiod: Optional[int] = Field(10, description="Slow period for A/D Oscillator calculation")

class OBVRequest(BaseModel):
    """Request model for On-Balance Volume (OBV)"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")

class HT_TRENDLINERequest(BaseModel):
    """Request model for Hilbert Transform - Instantaneous Trendline"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class HT_SINERequest(BaseModel):
    """Request model for Hilbert Transform"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class HT_TRENDMODERequest(BaseModel):
    """Request model for Hilbert Transform - Trend vs Cycle Mode"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class HT_DCPERIODRequest(BaseModel):
    """Request model for Hilbert Transform - Dominant Cycle Period"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class HT_DCPHASERequest(BaseModel):
    """Request model for Hilbert Transform - Dominant Cycle Phase"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

class HT_PHASORRequest(BaseModel):
    """Request model for Hilbert Transform - Phasor Components"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("daily", description="Time interval (1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)")
    series_type: Optional[str] = Field("close", description="Series type (open, high, low, close)")

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
