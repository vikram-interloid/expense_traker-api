from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    # Application
    app_name: str
    app_version: str
    app_env: str
    debug: bool

    # Database
    database_url: str

    # Redis
    # redis_host: str
    # redis_port: int
    # redis_db: int

    # JWT
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    refresh_token_expire_days: int

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()