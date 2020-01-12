import uvicorn

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from jwt import PyJWTError

from starlette.responses import RedirectResponse
from starlette.status import HTTP_401_UNAUTHORIZED

from services.security import verify_password
from services.token import create_access_token, get_username_from_access_token
from services.authentication import authenticate_user
from services.vehicles import get_vehicles
from models.users import User, UserInDB
from models.token import Token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

app = FastAPI()

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

@app.get("/", include_in_schema=False)
async def read_root():
    return RedirectResponse(url='/docs')


if __name__ == '__main__':
    # only debug
    uvicorn.run(app, host="0.0.0.0", port=8080)
