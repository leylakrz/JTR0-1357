from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Postgres
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432
    POSTGRES_DB_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_URL: str = ""
    POSTGRES_ASYNC_URL: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.POSTGRES_URL = f'postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB_NAME}'
        self.POSTGRES_ASYNC_URL = f'postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB_NAME}'


settings = Settings()
