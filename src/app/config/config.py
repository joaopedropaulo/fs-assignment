from starlette.config import Config
from starlette.datastructures import Secret

from databases import DatabaseURL

config = Config(".env")

SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)
ALGORITHM: str = config("ALGORITHM", cast=str, default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=10)
DB_USERNAME: str = config("DB_USERNAME", cast=str, default="root")
DB_PASSWORD: str = config("DB_PASSWORD", cast=str, default="example")
DB_NAME: str = config("DB_NAME", cast=str, default="fs-assignment")