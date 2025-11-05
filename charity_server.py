"""MCP Server module"""
import json
from typing import Optional
from fastmcp import FastMCP

# Initialize the FastMCP server & set stateless to allow for test session IDs for curl POST request
mcp = FastMCP(name="CharityQueryServer", stateless_http=True)

# Load the local JSON file containing charity data
with open("charities.json", mode="r", encoding="utf-8") as file:
    charities_data = json.load(file)

# Define a tool to query charity data
@mcp.tool(name="query_charities", description="Query charity data by name")
async def query_charities(charity_name: Optional[str] = None,
                    location: Optional[str] = None,
                    cause: Optional[str] = None):
    """Query Charities Data in memory by optional name/location, or cause search strings"""
    # Use list comprehension for cleaner filtering / search
    results = [
        charity for charity in charities_data
        if (not charity_name or charity_name.lower() in charity["name"].lower()) and
           (not location or location.lower() in charity["location"].lower()) and
           (not cause or cause.lower() in charity["cause"].lower())
    ]
    # Return results if found, otherwise return the original data
    return results if results else charities_data

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
