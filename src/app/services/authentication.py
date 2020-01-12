from app.services.security import verify_password
from app.db.users import get_user

# Service for user authentication

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user