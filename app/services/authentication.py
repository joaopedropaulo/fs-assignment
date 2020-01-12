from services.security import verify_password
from db.repositories.users import get_user

# TODO: change the authenticate method so that it doesn't receive a db object from the main app
def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user