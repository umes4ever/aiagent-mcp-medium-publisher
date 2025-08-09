import os

from google.adk.tools.mcp_tool import MCPToolset, StreamableHTTPConnectionParams
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# Medium MCP toolset (streamable-http)
MEDIUM_MCP_URL = os.getenv("MEDIUM_MCP_URL", "http://127.0.0.1:5055/mcp/")

mcp_tools = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url=f"{MEDIUM_MCP_URL}",
        headers={},
    ),
    tool_filter=[
        "medium_create_post",
    ],
)
