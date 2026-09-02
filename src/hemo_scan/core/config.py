from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    llm_base_url: str
    llm_api_key: str
    llm_model: str
    prompt_file: Path = Path("prompts/analysis.md")


settings = Settings()
