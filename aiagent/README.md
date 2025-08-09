## Medium Content AI Agent (`aiagent`)

An agent that drafts Medium-ready articles and creates posts via an MCP toolset. It uses `google-adk` for the agent runtime and connects to the local `medium-mcp-server` over HTTP.

### Features
- **Article generation**: Writes a complete Markdown article with structure and suggested tags.
- **Medium integration**: Calls MCP tools to create posts on Medium as draft, public, or unlisted.
- **FastMCP integration**: Uses the new simplified FastMCP server via STDIO transport.
- **Configurable model**: Set the agent model via `AGENT_MODEL`.

### Requirements
- Python 3.9+
- The `medium-mcp-server` FastMCP server (see `medium-mcp-server/README.md`).

### Environment variables
- **`AGENT_MODEL`**: LLM model name (default: `gemini-2.5-flash`).
- **`MEDIUM_MCP_URL`**: MCP base URL (default: `http://127.0.0.1:5055/mcp/`).

Place these in an `.env` file at the project root of `aiagent/` or set them in your shell. `python-dotenv` is used to load `.env` automatically.

Example `.env`:
```
AGENT_MODEL=gemini-2.5-flash
MEDIUM_MCP_URL=http://127.0.0.1:5055/mcp/
```

Note: The Medium API token is configured in the MCP server, not here. See `medium-mcp-server/README.md` and set `MEDIUM_INTEGRATION_TOKEN` there.

### Install
From the `aiagent/` directory:
```
# Windows (CMD)
python -m venv .venv
.venv\Scripts\activate

# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

### Setup FastMCP Server

1. **Install FastMCP server dependencies** (from `medium-mcp-server/` directory):
```bash
cd ../medium-mcp-server
pip install -r requirements.txt
```

2. **Set your Medium token** in the environment or `.env` file:
```bash
MEDIUM_INTEGRATION_TOKEN=your_integration_token_here
```

3. **Test the FastMCP server** (optional):
```bash
cd ../medium-mcp-server
python server.py
# OR
fastmcp dev server.py
```

### Usage in Python

Import the pre-configured agent instance `root_agent` from `aiagent.agent`.

```python
from aiagent.agent import root_agent

prompt = "Write a Medium article about building a Streamlit dashboard for sales analytics."

# Refer to google-adk Agent API for invocation methods.
# Common patterns include synchronous `run(...)` or streaming variants.
result = root_agent.run(prompt)  # if your google-adk version provides `.run`

print(result)
```

If your `google-adk` version exposes different invocation methods (e.g., `chat`, `respond`, `stream`), use those accordingly. See the `google-adk` documentation.

### How it Works

The assembled agent lives in `aiagent/agent.py` as `root_agent` and is configured with:
- System instruction from `aiagent/prompt.py` describing the end-to-end workflow for article creation and Medium posting.
- MCP tools from `aiagent/tools/tools.py` pointing to `MEDIUM_MCP_URL`.

Tooling note: The server currently exposes `medium_create_post`. Publishing is controlled via `publish_status` on creation (set to `public` to publish). If you see references to `medium_publish_post` in the prompt, use `medium_create_post` with `publish_status="public"` instead.

### Project files
- `aiagent/agent.py`: Builds the `root_agent` with model, instruction, and MCP tools.
- `aiagent/prompt.py`: System prompt and tool usage rules.
- `aiagent/tools/tools.py`: MCP toolset configuration and endpoint.
- `aiagent/requirements.txt`: Python dependencies (`google-adk`, `python-dotenv`).

### Troubleshooting
- **404 or tool not found**: Ensure `medium-mcp-server` is running and reachable at `MEDIUM_MCP_URL`. Call `GET /mcp/tools` and verify `medium_create_post` is listed.
- **Auth errors**: Set `MEDIUM_INTEGRATION_TOKEN` in the MCP server environment.
- **Model loading issues**: Set `AGENT_MODEL` to a valid model supported by your `google-adk` runtime.

### Testing the Integration

1. **Test the FastMCP server directly**:
```bash
cd ../medium-mcp-server
python server.py
# Should start without errors
```

2. **Test with FastMCP dev mode**:
```bash
cd ../medium-mcp-server
fastmcp dev server.py
# Try the medium_create_post tool with test data
```

3. **Test the agent integration**:
```python
from aiagent.agent import root_agent
result = root_agent.run("Write a test article about Python and create a draft")
```
