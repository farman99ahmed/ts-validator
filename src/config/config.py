"""Module for Application Config"""

import os
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """Class for App config"""
    TITLE: str = os.getenv('APP_TITLE', 'TS Validator')


class OpenAISettings(BaseSettings):
    """Class for Open AI Settings config"""
    URL: str = os.getenv('OPEN_AI_URL', 'https://api.openai.com/v1/chat/completions')
    API_KEY: str = os.getenv('OPEN_AI_API_KEY', '###########')
    MODEL: str = os.getenv('OPEN_AI_MODEL', 'gpt-4')
    MAX_TOKEN: int = 1000
