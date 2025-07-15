import asyncio
from server import FinancialMCPServer

async def main():
    """Main entry point"""
    server = FinancialMCPServer()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())

