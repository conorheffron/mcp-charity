# mcp-charity

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![Python package](https://github.com/conorheffron/mcp-charity/actions/workflows/python-package.yml/badge.svg)](https://github.com/conorheffron/mcp-charity/actions/workflows/python-package.yml)

[![Pylint](https://github.com/conorheffron/mcp-charity/actions/workflows/pylint.yml/badge.svg)](https://github.com/conorheffron/mcp-charity/actions/workflows/pylint.yml)

## Quick Start
### Install Dependencies
```shell
pip install -r requirements.txt
```

### Start MCP Server with `FASTMCP` (`transport=STDIO`, for CLI interface instead of HTTP / Postman)
```shell
fastmcp run charity_server.py
```

### Start MCP Server for Testing with recommended python init main process
```shell
python3 charity_server.py
```

---
## Testing

### Test via CLI with curl (__Note:__ Allows for sub string search values - `direct match not required!`)
```shell
curl --request POST \
  --url http://localhost:8000/mcp \
  --header 'accept: application/json, text/event-stream' \
  --header 'content-type: application/json' \
  --header 'mcp-session-id: my-test-session-124' \
  --data '{ "method": "tools/call", 
    "params": {
        "name": "query_charities", 
        "arguments": { 
            "charity_name": "", 
            "location": "Gal", 
            "cause": "" 
        } 
        }, 
        "jsonrpc": "2.0", 
        "id": 9}'
```
### Response from curl
```shell
event: message
data: {
  "jsonrpc": "2.0",
  "id": 9,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "[{\"name\":\"Irish Cancer Society\",\"location\":\"Galway\",\"cause\":\"Health\"}]"
      }
    ],
    "isError": false
  }
}
```

### Use `Postman` to connect & tests available app tools / end-points
 - Connect to MCP end-point `/mcp`
 - The test available tools, in this case, try `query_charities` tool
![postman](./screenshots/postman.png)

### HTTP Endpoint
 - http://localhost:8000/mcp

### Corresponding Logs
![fastmcp-logs](./screenshots/fastmcp-logs.png)

### Request Body for POST request to `query_charities` tool
```shell
curl --request POST \
  --url http://localhost:8000/mcp \
  --header 'accept: application/json, text/event-stream' \
  --header 'content-type: application/json' \
  --header 'mcp-session-id: my-test-session-124' \
  --data '{ "method": "tools/call", 
  "params": {
      "name": "query_charities", 
      "arguments": { 
          "charity_name": "", 
          "location": "", 
          "cause": "Animals" } 
      }, 
      "jsonrpc": "2.0", 
      "id": 9 }'
```
### Curl Response Body (Formatted where `isError` == false)
```shell
event: message
data: {
  "jsonrpc": "2.0",
  "id": 9,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "[{\"name\":\"Dogs Trust\",\"location\":\"Dublin\",\"cause\":\"Animals\"}]"
      }
    ],
    "isError": false
  }
}
```

### Request Body for POST request to `query_charities` tool with invalid argument
```shell
curl --request POST   --url http://localhost:8000/mcp   --header 'accept: application/json, text/event-stream'   --header 'content-type: application/json'   --header 'mcp-session-id: my-test-session-124'   --data '{ "method": "tools/call", 
  "params": { "name": "query_charities", 
      "arguments": {   
          "causes": "9" 
      } 
  }, 
  "jsonrpc": "2.0", 
  "id": 9}'
 ```

### `ERROR` Response (`isError` == true)
```shell
event: message
data: {
  "jsonrpc": "2.0",
  "id": 9,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "1 validation error for call[query_charities]\ncauses\n  Unexpected keyword argument [type=unexpected_keyword_argument, input_value='9', input_type=str]\n    For further information visit https://errors.pydantic.dev/2.12/v/unexpected_keyword_argument"
      }
    ],
    "isError": true
  }
}
```
