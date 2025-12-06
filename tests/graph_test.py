import pytest
from utils.logger import setup_logger
from graph.setup import Graph

import asyncio

logger = setup_logger("tests")

def test_graph():
    graph = Graph()
    asyncio.run(graph.setup())
    assert graph.graph is not None
    prompt = """
    send a gmail to test@gmail.com with this information:
    subject: test
    body: this is a test message
    
    Output Rule:
    If sending gmail to test@gmail.com is successful, return 1 and if not return 0
    without any extra information or text format
    """
    result = asyncio.run(graph.run(prompt))
    assert  int(result["messages"][-1].content) == 1
    logger.info('Test .env variables is successfully!')