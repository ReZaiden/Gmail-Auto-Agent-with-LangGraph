import os
from pathlib import Path
import yaml
from dotenv import load_dotenv
from .logger import setup_logger

# Setup logger
logger = setup_logger("config")

# Load environment variables
load_dotenv(override=True)

# Project root
ROOT_DIR = Path(__file__).parent.parent

class Config:
    """Central configuration manager"""

    # AI config
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
    OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", None)

    # Load YAML config
    @staticmethod
    def load_yaml():
        config_path = ROOT_DIR / "config"
        agents_config_path = config_path / "agents.yaml"
        main_config_path = config_path / "config.yaml"
        if not config_path.exists():
            raise ModuleNotFoundError(f"Config directory not found in {config_path}")
        if not agents_config_path.exists() or not agents_config_path.is_file():
            raise FileNotFoundError(f"agents.yaml not found in {agents_config_path}")
        if not main_config_path.exists() or not main_config_path.is_file():
            raise FileNotFoundError(f"config.yaml not found in {main_config_path}")

        with open(agents_config_path, "r", encoding='utf-8') as f:
            agents_config = yaml.safe_load(f)
        with open(main_config_path, "r", encoding='utf-8') as f:
            main_config = yaml.safe_load(f)
        return agents_config, main_config

    @staticmethod
    def agents_config():
        return Config.load_yaml()[0]


    @staticmethod
    def get():
        return Config.load_yaml()[1]


# Validate required env variables
if not Config.OPENAI_API_KEY:
    logger.error("OPENAI_API_KEY not set")
    raise ValueError("OPENAI_API_KEY not set")
