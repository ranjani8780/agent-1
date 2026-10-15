import os
import json


from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.messages import ToolMessage

from tools import get_stock_info
import time

key = "key"

model = "nvidia/nemotron-3-ultra-550b-a55b"

llm = ChatOpenAI(
    model=model,
    api_key=key,
    temperature=0,
    base_url="https://openrouter.ai/api/v1"
)

price_prompt = ChatPromptTemplate.from_template(
    """
You are an assistant that receives a stock symbol 

{symbol}

Get the price  and news related to stock """
)

tools = [get_stock_info]

llm_with_tools = llm.bind_tools(tools)

price_chain = price_prompt | llm_with_tools

count =0

while True:

    price_message = price_chain.invoke({"symbol": "HIVE"})


    print("\nLLM response:")
    print(price_message)

    if price_message.tool_calls:

        tool_call = price_message.tool_calls[0]

        print("\nTool requested:")
        print(tool_call)


        # ========================================================
        # 10. EXECUTE THE TOOL
        # ========================================================

        tool_result = get_stock_info.invoke(
            tool_call["args"]
        )

        print("\nTool result:")
        print(tool_result)


        # ========================================================
        # 11. CONVERT TOOL RESULT TO ToolMessage
        # ========================================================

        tool_message = ToolMessage(
            content=json.dumps(tool_result),
            tool_call_id=tool_call["id"]
        )


        # ========================================================
        # 12. SEND TOOL RESULT BACK TO LLM
        # ========================================================

        final_message = llm_with_tools.invoke([
            price_message,
            tool_message
        ])


        # ========================================================
        # 13. PRINT FINAL ANSWER
        # ========================================================

        print("\nFinal stock info answer:")
        print(final_message.content)


    else:

        print("\nThe model did not request the stock info tool.")

        print(price_message.content)
    count+=1
    print(f"\nIteration count: {count}")
    time.sleep(15 * 60)

