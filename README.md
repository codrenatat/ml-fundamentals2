# ML Fundamentals 2 - Financial Chat Assistant

A full-stack web application that provides an AI-powered financial chat assistant with real-time market data integration. The system combines a React frontend, Node.js backend with TypeScript, and a Python MCP (Model Context Protocol) server for financial analysis and AI responses.

## Features

- **Real-time Chat Interface**: Modern React-based chat UI with conversation management
- **AI-Powered Responses**: Integration with OpenAI GPT models for intelligent financial advice
- **Market Data Integration**: Live financial data from Alpha Vantage API
- **Conversation Persistence**: PostgreSQL database for storing chat history
- **RESTful API**: Elysia.js backend with Swagger documentation
- **Containerized Deployment**: Docker Compose setup for easy development and deployment
- **Type-Safe Backend**: TypeScript implementation with Kysely ORM

## Architecture

The application consists of three main components:

### Frontend (React + Vite)
- Modern React 19 application
- Axios for API communication
- Responsive chat interface with sidebar navigation
- Real-time message updates

### Backend (Node.js + TypeScript)
- Elysia.js framework for high-performance API
- PostgreSQL database with Kysely ORM
- RESTful endpoints for conversations and messages
- CORS enabled for frontend integration
- Swagger API documentation

### MCP Server (Python + FastAPI)
- Model Context Protocol implementation
- Alpha Vantage API integration for financial data
- OpenAI GPT integration for AI responses
- Tool-based architecture for extensible functionality

## Tech Stack

- **Frontend**: React 19, Vite, Axios
- **Backend**: Node.js, TypeScript, Elysia.js, Kysely, PostgreSQL
- **MCP Server**: Python, FastAPI, OpenAI API, Alpha Vantage API
- **Database**: PostgreSQL 13
- **Containerization**: Docker & Docker Compose
- **Runtime**: Bun (backend), Node.js (frontend)

## Prerequisites

- Docker and Docker Compose
- Node.js 18+ (for frontend development)
- Python 3.11+ (for MCP server development)
- Bun runtime (for backend development)
- API Keys:
  - OpenAI API key
  - Alpha Vantage API key

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ml-fundamentals2
   ```

2. **Environment Setup**

   Create environment files for each service:

   **MCP Server (.env)**
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
   OPENAI_MODEL=gpt-4
   MAX_TOKENS=1000
   TEMPERATURE=0.7
   ```

   **Backend (.env)**
   ```env
   DATABASE_URL=postgresql://postgres:12345@localhost:5433/mcp
   ```

3. **Start Services with Docker**
   ```bash
   docker-compose up -d
   ```

4. **Install Dependencies**

   **Frontend:**
   ```bash
   cd frontend
   npm install
   ```

   **Backend:**
   ```bash
   cd backend
   bun install
   ```

   **MCP Server:**
   ```bash
   cd mcp-server
   pip install -r requirements.txt
   ```

## Usage

1. **Start the Backend**
   ```bash
   cd backend
   bun run dev
   ```

2. **Start the Frontend**
   ```bash
   cd frontend
   npm run dev
   ```

3. **Start the MCP Server**
   ```bash
   cd mcp-server
   python main.py
   ```

4. **Access the Application**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:3333
   - API Documentation: http://localhost:3333/swagger

## API Endpoints

### Conversations
- `GET /chats` - List all conversations
- `POST /chats` - Create new conversation
- `GET /chats/:id` - Get conversation by ID

### Messages
- `GET /messages/:conversationId` - Get messages for conversation
- `POST /messages` - Send new message

## Development

### Running Tests
```bash
# Backend tests
cd backend
bun test

# Frontend linting
cd frontend
npm run lint
```

### Database Migrations
The database is initialized with the SQL file in `init/backup.sql` when the container starts.

### Building for Production
```bash
# Frontend
cd frontend
npm run build

# Backend (if needed)
cd backend
bun run build
```

## Configuration

### Environment Variables

**MCP Server:**
- `OPENAI_API_KEY`: Your OpenAI API key
- `ALPHA_VANTAGE_API_KEY`: Your Alpha Vantage API key
- `OPENAI_MODEL`: GPT model to use (default: gpt-4)
- `MAX_TOKENS`: Maximum tokens for AI responses
- `TEMPERATURE`: AI response creativity (0.0-1.0)

**Backend:**
- `DATABASE_URL`: PostgreSQL connection string

## Acknowledgments

- [Elysia.js](https://elysiajs.com/) for the backend framework
- [React](https://reactjs.org/) for the frontend library
- [OpenAI](https://openai.com/) for AI capabilities
- [Alpha Vantage](https://www.alphavantage.co/) for financial data
- [Model Context Protocol](https://modelcontextprotocol.io/) for the server architecture</content>
