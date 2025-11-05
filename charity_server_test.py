import pytest
from fastmcp.client import Client
from fastmcp.client.transports import FastMCPTransport

from charity_server import mcp

@pytest.fixture
async def main_mcp_client():
    async with Client(transport=mcp) as mcp_client:
        yield mcp_client

@pytest.mark.asyncio
async def test_list_tools(main_mcp_client: Client[FastMCPTransport]):
    list_tools = await main_mcp_client.list_tools()

    assert len(list_tools) == 1
    assert list_tools[0].name == "query_charities"

# @pytest.mark.asyncio
# async def test_query_charities_empty_response(main_mcp_client: Client[FastMCPTransport]):
#     """Test querying charities with no matching results."""
#     queryBody = { "method": "tools/call", 
#   "params": { "name": "query_charities", 
#       "arguments": { 
#           "name": "", 
#           "location": "Gal", 
#           "cause": "" 
#       } 
#   }, 
#   "jsonrpc": "2.0", 
#   "id": 9}
#     response = await main_mcp_client.call_tool('query_charities', charity_name="", location="Gal", cause="")
    
#     assert response.status_code == 200
#     assert "results" in response.json()
#     assert len(response.json()["results"]) == 0