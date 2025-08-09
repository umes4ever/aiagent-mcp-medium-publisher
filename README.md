# AI Agent using Google Agent Development Kit (ADK) and Medium MCP Server using FastMCP

**aiagent**: An AI agent built using the Google Agent Development Kit (ADK), designed to interact with users and perform tasks via a web interface.

**medium-mcp-server**: A server built with FastMCP that acts as a Medium MCP (Message Control Protocol) backend, managing communication and coordination for the AI agent.


## Running with Docker Compose

To run both the `aiagent` and `medium-mcp-server` services using Docker Compose, follow these steps:

1. **Build and start the services:**

   ```bash
   docker-compose up --build
   ```

   This command will build the Docker images (if not already built) and start both containers.

2. **Access the services:**

   - **aiagent web interface:** [http://localhost:8000](http://localhost:8000)
   - **medium-mcp-server API:** [http://localhost:5055/mcp/](http://localhost:5055/mcp/)

3. **Stopping the services:**

   Press `Ctrl+C` in the terminal running Docker Compose, then run:

   ```bash
   docker-compose down
   ```

This setup ensures both services are networked together and ready for development or testing.

For more details, see the accompanying Medium post: [AI-Powered Medium Publishing with MCP Server: From Draft to Post in One Command](https://medium.com/@umes4ever)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/umes4ever/aiagent-mcp-medium-publisher/LICENSE) file for details.