from app.db.connection import get_db_connection

from app.models.users import User, UserInDB

db = get_db_connection()

# Retrieves the user document from the database, given an existing 'username'
def get_user(username: str):
    user = db.users.find_one({"username": username})
    if user:
        return UserInDB(**user)