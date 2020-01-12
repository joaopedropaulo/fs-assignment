import json
import os

from db.connection import get_db_connection

from models.users import User, UserInDB

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

db = get_db_connection()

with open(os.path.join(THIS_FOLDER, 'fake_users_db.json'), 'r') as fake_data:
    fake_users_db=json.load(fake_data)

def get_user(username: str):
    user = db.users.find_one({"username": username})
    if user:
        return UserInDB(**user)