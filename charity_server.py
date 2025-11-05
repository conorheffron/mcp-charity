import json
from typing import Optional
from fastmcp import FastMCP

# Initialize the FastMCP server & set stateless to allow for test session IDs for curl POST request
app = FastMCP(name="CharityQueryServer", stateless_http=True)

# Load the local JSON file containing charity data
with open("charities.json", "r") as file:
    charities_data = json.load(file)

# Define a tool to query charity data
@app.tool(name="query_charities", description="Query charity data by name")
def query_charities(name: Optional[str] = None,
                    location: Optional[str] = None,
                    cause: Optional[str] = None):
    """Query Charities Data in memory by optional name/location, or cause search strings"""
    results = []
    for charity in charities_data:
        if (name and name.lower() not in charity["name"].lower()) or \
                (location and location.lower() not in charity["location"].lower()) or \
                (cause and cause.lower() not in charity["cause"].lower()):
            continue
        results.append(charity)
    if not results:
        return charities_data
    else:
        return results

if __name__ == "__main__":
    """Main process"""
    app.run(transport="http", host="0.0.0.0", port=8000)
