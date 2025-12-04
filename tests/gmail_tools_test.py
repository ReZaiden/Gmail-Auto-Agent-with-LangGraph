import pytest
from tools.gmail_tools import get_gmail_tools
from utils.logger import setup_logger
import asyncio

logger = setup_logger("tests")

def test_gmail_tools():
    gmail_tools = asyncio.run(get_gmail_tools())
    assert gmail_tools is not None
    search_result = asyncio.run(gmail_tools[2].ainvoke({'query': '', 'max_results': 1}))
    assert len(search_result) > 0
    logger.info('Test gmail_tools is successfully!')