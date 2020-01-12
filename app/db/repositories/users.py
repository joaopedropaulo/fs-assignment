from db.connection import get_db_connection

from models.users import User, UserInDB

db = get_db_connection()

def get_user(username: str):
    user = db.users.find_one({"username": username})
    if user:
        return UserInDB(**user)