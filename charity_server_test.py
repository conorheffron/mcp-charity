"""charity_server_test.py: Tests for the charity MCP server."""
import pytest
from fastmcp.client import Client
from charity_server import mcp

@pytest.fixture
async def mcp_client():
    """Setup MCP client for testing."""
    async with Client(transport=mcp) as client:
        yield client

@pytest.mark.asyncio
async def test_list_tools(mcp_client: Client[FastMCPTransport]):
    """List available tools in the MCP server."""
    list_tools = await mcp_client.list_tools()

    assert len(list_tools) == 1
    assert list_tools[0].name == "query_charities"
