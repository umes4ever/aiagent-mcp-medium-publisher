#!/usr/bin/env python3
"""
Medium MCP Server using FastMCP

A robust MCP server for creating Medium posts using the Medium API.
Set MEDIUM_INTEGRATION_TOKEN environment variable before running.
"""

import os
import logging
from typing import List, Optional, Literal, Dict, Any
import httpx
from fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("MEDIUM_INTEGRATION_TOKEN")
if not TOKEN:
    raise EnvironmentError(f"Missing MEDIUM_INTEGRATION_TOKEN")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

BASE_URL = "https://api.medium.com/v1"
mcp = FastMCP("Medium MCP Server")

class MediumAPIError(Exception):
    """Raised for Medium API errors."""
    pass

async def _make_medium_request(
    method: str,
    endpoint: str,
    json_data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Make a request to the Medium API with retries for transient errors."""
    url = f"{BASE_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    
    async with httpx.AsyncClient(timeout=60) as client:
        for attempt in range(3):
            try:
                logging.debug(f"Request {method} {url} attempt {attempt+1}")
                response = await client.request(method, url, headers=headers, json=json_data)
                
                if response.is_success:
                    return response.json().get("data", {})
                
                try:
                    error_data = response.json()
                    error_msg = error_data.get("message", response.text)
                except Exception:
                    error_msg = response.text
                
                if response.status_code >= 500 and attempt < 2:
                    logging.warning(f"Retrying due to server error {response.status_code}: {error_msg}")
                    continue
                
                raise MediumAPIError(f"Medium API error ({response.status_code}): {error_msg}")
            
            except httpx.RequestError as e:
                if attempt < 2:
                    logging.warning(f"Network error: {e}. Retrying...")
                    continue
                raise MediumAPIError(f"Network error: {e}")

    raise MediumAPIError("Failed to get a successful response after retries.")

@mcp.tool()
async def medium_create_post(
    title: str,
    content: str,
    publish_status: Literal["draft", "public", "unlisted"] = "draft",
    content_format: Literal["markdown", "html"] = "markdown", 
    tags: Optional[List[str]] = None,
    canonical_url: Optional[str] = None,
    notify_followers: bool = False,
    license: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a Medium post.

    Args:
        title: Title of the post
        content: Content in markdown or HTML
        publish_status: 'draft', 'public', or 'unlisted'
        content_format: 'markdown' or 'html'
        tags: Up to 5 tags
        canonical_url: Canonical link if cross-posting
        notify_followers: Whether to notify followers
        license: License type

    Returns:
        Dictionary containing the created post data
    """
    try:
        me_data = await _make_medium_request("GET", "/me")
        user_id = me_data.get("id")
        if not user_id:
            raise MediumAPIError("Could not retrieve Medium user ID.")

        if tags:
            tags = [t.strip() for t in tags if t.strip()]
            if len(tags) > 5:
                logging.warning("Trimming tags to maximum 5.")
                tags = tags[:5]

        post_data = {
            "title": title,
            "contentFormat": content_format,
            "content": content,
            "publishStatus": publish_status,
            "notifyFollowers": notify_followers
        }
        if tags: post_data["tags"] = tags
        if canonical_url: post_data["canonicalUrl"] = canonical_url
        if license: post_data["license"] = license

        post_result = await _make_medium_request(
            "POST", 
            f"/users/{user_id}/posts",
            post_data
        )

        logging.info(f"Post '{title}' created successfully as {publish_status}")
        return {
            "success": True,
            "post": post_result,
            "message": f"Post '{title}' created successfully as {publish_status}"
        }

    except MediumAPIError as e:
        logging.error(f"Medium API error: {e}")
        return {"success": False, "error": str(e)}

    except Exception as e:
        logging.exception("Unexpected error creating Medium post.")
        return {"success": False, "error": f"Unexpected error: {str(e)}"}

def main() -> None:
    mcp.run(transport="streamable-http", host="0.0.0.0", port=5055)


if __name__ == "__main__":
    main()
