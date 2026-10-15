# agent-1
Stock Information Agent:

A Python tool-calling prototype built with LangChain. It asks an LLM to retrieve information for a stock symbol, executes an Alpha Vantage quote tool when requested, and sends the result back to the model for a natural-language response.

The project also defines a Tavily city-news tool, which is not connected to the current stock-agent workflow.

Features:

LLM tool binding through LangChain and an OpenRouter endpoint.

Stock quote retrieval through Alpha Vantage's GLOBAL_QUOTE endpoint.

Tool-result delivery using LangChain ToolMessage.

Console output for model responses, tool calls, API results, and final answers.

Repeated execution with a 15-minute pause after each completed iteration.

A separate city-news search tool configured for up to five results.

Project Structure:

text
.
├── main.py       # Model configuration, tool binding, and recurring execution
├── tools.py      # Alpha Vantage quote tool and Tavily city-news tool
└── README.md     # Project documentation

Requirements:

Python with pip and virtual-environment support.

An OpenRouter API key and access to a model that supports tool calling.

An Alpha Vantage API key.

A Tavily API key to use the optional city-news tool.

Internet access for the external API calls.

The supplied project does not include dependency version pins or a requirements file. Package/API compatibility must be checked in your environment.


How It Works:

The prompt requests stock price and news information for the configured symbol.

The prompt is sent to the model with get_stock_info bound as a tool.

If the model requests a tool call, the script executes the first requested call.

get_stock_info requests quote data from Alpha Vantage.

The response is serialized as JSON and wrapped in a ToolMessage.

The assistant tool-call message and tool result are sent to the model.

The final response is printed to the console.

The iteration count is incremented and execution pauses for 900 seconds.

If no tool call is requested, the script prints the model response instead. The interval is a pause after processing, not a fixed wall-clock schedule.