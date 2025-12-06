from graph.setup import Graph
import asyncio
from typing import List

import gradio as gr

# Create and setup the graph
graph = Graph()
asyncio.run(graph.setup())

# Define the chat function to interact with the graph
async def chat(message: str, history: List):
    result = await graph.run(message)
    return result["messages"][-1].content

# Launch the Gradio interface
gr.ChatInterface(fn=chat, title="Gmail Auto Agent", description="An AI agent to help you manage your Gmail account automatically.", save_history=True).launch()
