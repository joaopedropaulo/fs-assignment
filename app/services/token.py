import jwt
from datetime import datetime, timedelta
from config import config
from models.token import Token, TokenData

def create_access_token(*, data: dict):
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = data.copy()
    expire = datetime.utcnow() + access_token_expires
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, str(config.SECRET_KEY), algorithm=str(config.ALGORITHM))
    return encoded_jwt

def get_username_from_access_token(token: str):
    payload = jwt.decode(token, str(config.SECRET_KEY), algorithm=str(config.ALGORITHM))
    username: str = payload.get("sub")
    token_data = TokenData(username=username)
    return token_data.username