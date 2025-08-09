# Medium MCP Server (FastMCP)

A simple, powerful MCP server for creating Medium posts using the Medium API, built with FastMCP for maximum simplicity and ease of use.

## ✨ Features

- **🚀 Single-file implementation** - Everything in one `server.py` file
- **📝 medium_create_post tool** - Create Medium posts as draft, public, or unlisted
- **🔧 Built with FastMCP** - Modern, simple MCP framework
- **🎯 Minimal dependencies** - Only 3 required packages
- **💡 Easy to understand** - Clear, well-documented code
- **🔒 Secure** - Environment-based token management

## 📋 Prerequisites

- Python 3.10 or higher
- Medium integration token ([Get one here](https://medium.com/me/settings))

## 🚀 Quick Start

### 1. Installation

```bash
# Navigate to the server directory
cd medium-mcp-server

# Create and activate virtual environment
# Windows (CMD)
python -m venv .venv
.venv\Scripts\activate

# Linux/macOS (bash/zsh)
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Create a `.env` file in the project root:

```env
MEDIUM_INTEGRATION_TOKEN=your_integration_token_here
```

> **Note**: Get your Medium integration token from [Medium Settings](https://medium.com/me/settings) → Integration tokens

### 3. Run the Server

```bash
# Standard mode (Streamable HTTP transport for MCP clients)
python server.py

# Development mode (interactive testing)
fastmcp dev server.py
```

## 🛠️ Usage Examples

### Basic Example

Create a simple draft post:

```python
# Using the MCP tool
{
  "tool": "medium_create_post",
  "arguments": {
    "title": "My First MCP Post",
    "content": "# Hello World\n\nThis post was created using the Medium MCP server!"
  }
}
```

### Advanced Example

Create a public post with all options:

```python
{
  "tool": "medium_create_post", 
  "arguments": {
    "title": "Advanced MCP Post",
    "content": "# Advanced Features\n\nThis post demonstrates all available options.",
    "publish_status": "public",
    "content_format": "markdown",
    "tags": ["mcp", "medium", "automation", "fastmcp"],
    "canonical_url": "https://myblog.com/advanced-mcp-post",
    "notify_followers": true,
    "license": "cc-40-by"
  }
}
```

### Response Format

```json
{
  "success": true,
  "post": {
    "id": "abc123...",
    "title": "My First MCP Post", 
    "authorId": "user123...",
    "tags": ["mcp"],
    "url": "https://medium.com/@user/my-first-mcp-post-abc123",
    "publishStatus": "draft"
  },
  "message": "Post 'My First MCP Post' created successfully as draft"
}
```

## 📖 Tool Reference

### medium_create_post

Creates a Medium post with comprehensive options.

#### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `title` | string | Title for the post |
| `content` | string | Post body content (markdown or HTML) |

#### Optional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `publish_status` | enum | `"draft"` | Publication status: `"draft"`, `"public"`, or `"unlisted"` |
| `content_format` | enum | `"markdown"` | Content format: `"markdown"` or `"html"` |
| `tags` | array | `null` | List of up to 5 tags for the post |
| `canonical_url` | string | `null` | Canonical URL if cross-posting from another site |
| `notify_followers` | boolean | `false` | Whether to notify followers when publishing |
| `license` | string | `null` | License identifier (e.g., "cc-40-by") |

#### Publish Status Options

- **`"draft"`** - Save as draft (default, can be published later)
- **`"public"`** - Publish immediately to your followers and Medium
- **`"unlisted"`** - Publish but don't distribute (shareable via direct link)

## 📁 Project Structure

```
medium-mcp-server/
├── server.py          # 🎯 Single-file FastMCP server (all logic here)
├── requirements.txt   # 📦 Minimal dependencies
├── README.md         # 📚 This documentation
├── .env              # 🔑 Environment variables (create this)
└── .gitignore        # 🚫 Git ignore file
```

## 🔒 Security Best Practices

- **Never commit tokens**: Keep `.env` out of version control
- **Use environment variables**: Set `MEDIUM_INTEGRATION_TOKEN` securely
- **Token scope**: Your integration token has full access to your Medium account
- **Rotate tokens**: Regenerate tokens periodically from Medium settings

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **"MEDIUM_INTEGRATION_TOKEN environment variable is required"** | Create `.env` file or set environment variable |
| **"Medium API error (401)"** | Check that your integration token is valid and not expired |
| **"Import errors"** | Ensure virtual environment is activated and dependencies installed |
| **"fastmcp: command not found"** | Install dependencies with `pip install -r requirements.txt` |

## 🔄 Migration from FastAPI Version

This FastMCP version replaces the previous complex multi-file FastAPI implementation:

The functionality remains identical, but the code is much simpler and easier to maintain.

## 📚 Learn More

- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [Medium API Documentation](https://github.com/Medium/medium-api-docs)
- [MCP Protocol Specification](https://spec.modelcontextprotocol.io/)

---

**Built with ❤️ using [FastMCP](https://github.com/jlowin/fastmcp)**