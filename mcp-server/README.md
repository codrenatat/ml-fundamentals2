# Financial MCP API Server

A FastAPI-based REST API wrapper for a Financial MCP (Model Context Protocol) Server that provides access to financial data and AI-powered analysis.

## Features

- Stock quote retrieval
- Company overview and fundamentals
- Time series data (daily and intraday)
- AI-powered financial analysis via OpenAI
- RESTful API endpoints
- Automatic tool selection for natural language queries

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Variables

Create a `.env` file in the `mcp-server` directory with the following variables:

```env
# Required
OPENAI_API_KEY=your_openai_api_key_here
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key_here

# Optional (defaults shown)
OPENAI_MODEL=gpt-3.5-turbo
MAX_TOKENS=1000
TEMPERATURE=0.7
```

### 3. Get API Keys

- **OpenAI API Key**: Get from [OpenAI Platform](https://platform.openai.com/api-keys)
- **Alpha Vantage API Key**: Get from [Alpha Vantage](https://www.alphavantage.co/support/#api-key)

## Running the Server

### Start the API Server

```bash
python run_api.py
```

The server will start on `http://localhost:8000`

### API Documentation

- Swagger UI: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

## API Endpoints

### Core Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /tools` - List available tools

### Financial Data Endpoints

- `POST /stock/quote` - Get current stock quote
- `POST /stock/overview` - Get company overview
- `POST /stock/daily` - Get daily time series data
- `POST /stock/intraday` - Get intraday time series data

### AI Endpoints

- `POST /ai/chat` - Chat with AI about financial topics
- `POST /financial/query` - Natural language financial queries

## Troubleshooting

### Common Issues

1. **BrokenPipeError**: This usually means the MCP server failed to start.

2. **Missing Environment Variables**: Make sure both `OPENAI_API_KEY` and `ALPHA_VANTAGE_API_KEY` are set.

3. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`.

### Testing

Run the test script to check your setup:

```bash
python test_server.py
```

### Project Structure

```
mcp-server/
├── main.py              # MCP server entry point
├── server.py            # MCP server implementation
├── fastapi_server.py    # FastAPI REST API
├── mcp_client.py        # MCP client for communication
├── tools.py             # Tool implementations
├── alpha_vantage_client.py  # Alpha Vantage API client
├── openai_client.py     # OpenAI API client
├── config.py            # Configuration management
├── api_models.py        # Pydantic models for API
└── run_api.py           # API server launcher
```

### Adding New Tools

1. Add tool definition in `tools.py`
2. Add corresponding endpoint in `fastapi_server.py`
3. Update API models in `api_models.py` if needed 