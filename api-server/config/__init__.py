import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

env = os.getenv('api-server-env', 'local')
env_file_name = f'.env.{env}'


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=('.env', env_file_name),
        env_file_encoding='utf-8'
    )


@lru_cache
def get_app_config():
    """
    get app config for dependency injection wrapped in functools.lru_cache
    - initialized on app start up and not changed until the app goes down

    :return: appropriate env-specified application configuration object
    """
    return AppConfig()
