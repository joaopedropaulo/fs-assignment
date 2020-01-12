import uvicorn
#import jwt

#from datetime import timedelta #,datetime

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from jwt import PyJWTError

#from starlette.responses import RedirectResponse
from starlette.status import HTTP_401_UNAUTHORIZED

#from pydantic import BaseModel

from services.security import verify_password
from services.token import create_access_token, get_username_from_access_token
from services.authentication import authenticate_user
from services.vehicles import get_vehicles
from models.users import User, UserInDB
from models.token import Token

# to get a string like this run:
# openssl rand -hex 32
#SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
#ALGORITHM = "HS256"
#ACCESS_TOKEN_EXPIRE_MINUTES = 10

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

app = FastAPI()

#def get_user(db, username: str):
#    if username in db:
#        user_dict = db[username]
#        return UserInDB(**user_dict)
#
async def get_authenticated_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
       authenticated_user = get_username_from_access_token(token)
    except PyJWTError:
        raise credentials_exception
    if authenticated_user is None:
        raise credentials_exception
    return authenticated_user


#async def get_current_active_user(current_user: User = Depends(get_current_user)):
#    return current_user


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/vehicles")
async def get_vehicles_for_user(authenticated_user: str = Depends(get_authenticated_user)):
    vehicles = get_vehicles(authenticated_user)
    print(vehicles)
    return {"vehicles": vehicles}

#@app.get("/users/me/", response_model=User)
#async def read_users_me(current_user: User = Depends(get_current_active_user)):
#    return current_user
#
#
#@app.get("/users/me/items/")
#async def read_own_items(current_user: User = Depends(get_current_active_user)):
#    return [{"item_id": "Foo", "owner": current_user.username}]

#app = FastAPI()
#
#oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
#
#
#class User(BaseModel):
#    username: str
#    email: Optional[str] = None
#    full_name: Optional[str] = None
#    disabled: Optional[bool] = None
#
#@app.get("/", include_in_schema=False)
#async def read_root():
#    return RedirectResponse(url='/docs')
#
#def fake_decode_token(token):
#    return User(
#        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
#    )
#
#
#async def get_current_user(token: str = Depends(oauth2_scheme)):
#    user = fake_decode_token(token)
#    return user


#@app.get("/users/me")
#async def read_users_me(current_user: User = Depends(get_current_user)):
#    return current_user

#@app.get("/vehicles")
#async def post(token: str = Depends(oauth2_scheme)):
#    return {"token" : token}

if __name__ == '__main__':
    # only debug
    uvicorn.run(app, host="0.0.0.0", port=8080)
