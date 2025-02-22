from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DBNAME: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: str
    PASSWD: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
