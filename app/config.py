from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # perform validation for env variables 
    database_hostname: str 
    database_port: str 
    database_password: str 
    database_name: str 
    database_username: str 
    secret_key: str 
    algorithm: str # for signing token
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

settings = Settings()