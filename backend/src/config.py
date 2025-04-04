import yaml
import asyncio
from pathlib import Path
from typing import List


from pydantic import validator
from pydantic_settings import BaseSettings

class PostgresConfig(BaseSettings):
    host: str
    port: int
    user: str
    password: str
    name: str

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"    


class RedisConfig(BaseSettings):
    host: str
    port: int
    user: str
    password: str
    name: str

    @property
    def url(self) -> str:
        return f"redis://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
    
class JWTConfig(BaseSettings):
    secret_key: str
    access_token_exp: int = 5
    algorithm: str = "HS256"


class AdminAuthConfig(BaseSettings):
    login: str
    password: str
    

class LogsConfig(BaseSettings):
    level: str
    retention: str
    rotation: str
    
    
class AnimeApiConfig(BaseSettings):
    data_api:str 
    download_api:str
    image_api:str


class Config(BaseSettings):
    postgresql: PostgresConfig
    redis: RedisConfig
    jwt: JWTConfig
    admin: AdminAuthConfig
    logs: LogsConfig
    anime_api:AnimeApiConfig

    @classmethod
    def from_yaml(cls, config_file: Path) -> "Config":
        with open(config_file, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            
        return cls(**config)


project_src: Path = Path(__file__).resolve().parent
project_root: Path = project_src.parent
path_to_yaml = project_root / ".env.back.yaml"
cfg = Config.from_yaml(path_to_yaml)

# print(cfg.postgresql.password)

