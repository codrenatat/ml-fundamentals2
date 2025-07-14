import asyncio
import json
import subprocess
import sys
import os
from typing import Dict, Any, Optional
from dataclasses import dataclass
 
@dataclass
class MCPResponse:
    """Response from MCP server"""
    success: bool
    data: Any = None
    error: str = None
 
class MCPClient:
    """Client to communicate with MCP server via subprocess"""
 
    def __init__(self, server_script_path: str, env_vars: Optional[Dict[str, str]] = None):
        self.server_script_path = server_script_path
        self.env_vars = env_vars or {}
        self.process = None
        self.request_id = 0
 
    async def start_server(self):
        """Start the MCP server process (Windows-compatible)"""
        env = os.environ.copy()
        env.update(self.env_vars)
 
        def launch():
            self.process = subprocess.Popen(
                [sys.executable, self.server_script_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=env,
                text=True
            )
 
        await asyncio.to_thread(launch)
 
        # Initialize the server
        await self._send_initialize()
 
    async def stop_server(self):
        """Stop the MCP server process"""
        if self.process:
            self.process.terminate()
            self.process.wait()
 
    async def _send_initialize(self):
        """Send initialization message to MCP server"""
        init_message = {
            "jsonrpc": "2.0",
            "id": self._get_request_id(),
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "clientInfo": {
                    "name": "fastapi-mcp-client",
                    "version": "1.0.0"
                }
            }
        }
 
        response = await self._send_message(init_message)
 
        # Send initialized notification
        initialized_message = {
            "jsonrpc": "2.0",
            "method": "notifications/initialized"
        }
        await self._send_notification(initialized_message)
 
        return response
 
    async def _send_message(self, message: Dict[str, Any]) -> MCPResponse:
        """Send message to MCP server and get response"""
        if not self.process or self.process.stdin is None or self.process.stdout is None:
            return MCPResponse(False, error="Server not started")
 
        try:
            message_str = json.dumps(message) + "\n"
            self.process.stdin.write(message_str)
            self.process.stdin.flush()
 
            response_line = self.process.stdout.readline()
            response_data = json.loads(response_line.strip())
 
            if "error" in response_data:
                return MCPResponse(False, error=response_data["error"])
 
            return MCPResponse(True, data=response_data.get("result"))
 
        except Exception as e:
            return MCPResponse(False, error=str(e))
 
    async def _send_notification(self, message: Dict[str, Any]):
        """Send notification (no response expected)"""
        if not self.process or self.process.stdin is None:
            return
 
        message_str = json.dumps(message) + "\n"
        self.process.stdin.write(message_str)
        self.process.stdin.flush()
 
    def _get_request_id(self) -> int:
        """Get next request ID"""
        self.request_id += 1
        return self.request_id
 
    async def list_tools(self) -> MCPResponse:
        """List available tools"""
        message = {
            "jsonrpc": "2.0",
            "id": self._get_request_id(),
            "method": "tools/list"
        }
        return await self._send_message(message)
 
    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> MCPResponse:
        """Call a specific tool"""
        message = {
            "jsonrpc": "2.0",
            "id": self._get_request_id(),
            "method": "tools/call",
            "params": {
                "name": name,
                "arguments": arguments
            }
        }
        return await self._send_message(message)