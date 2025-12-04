import pytest
from utils.config import Config
from utils.logger import setup_logger

logger = setup_logger("tests")

def test_env_vars():
    assert Config.OPENAI_API_KEY is not None
    assert Config.OPENAI_BASE_URL is not None
    logger.info('Test .env variables is successfully!')