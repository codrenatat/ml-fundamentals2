import uvicorn
import os
import dotenv

dotenv.load_dotenv()

if __name__ == "__main__":
    # Check for required environment variables
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is required")
        exit(1)
    
    if not os.getenv("ALPHA_VANTAGE_API_KEY"):
        print("Error: ALPHA_VANTAGE_API_KEY environment variable is required")
        exit(1)
    
    print("Starting Financial MCP API Server...")
    print("API Documentation will be available at: http://localhost:8000/docs")
    print("Health check: http://localhost:8000/health")
    
    uvicorn.run(
        "fastapi_server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
