from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, List

class StockPriceRequest(BaseModel):
    """Request model for intraday stock price"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, MSFT)")
    interval: Optional[str] = Field("5min", description="Time interval (1min, 5min, 15min, 30min, 60min)")

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
