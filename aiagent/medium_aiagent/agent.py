import os

from google.adk.agents import Agent

from .prompt import agent_instruction
from .tools.tools import mcp_tools
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

AGENT_MODEL = os.getenv("AGENT_MODEL", "gemini-2.5-flash")

root_agent = Agent(
    model=AGENT_MODEL,
    name="medium_content_aiagent",
    instruction=agent_instruction,
    tools=[mcp_tools],
)
