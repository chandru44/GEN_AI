from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "soc-copilot-v2"
    app_env: str = "dev"
    api_key: str = "change-me"
    openai_api_key: str = ""
    model_name: str = "gpt-4.1-mini"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
