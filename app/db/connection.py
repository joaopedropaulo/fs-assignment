import csv
import json
import os
from services.security import get_password_hash

from pymongo import MongoClient
from config import config

db_username = str(config.DB_USERNAME)
db_password = str(config.DB_PASSWORD)
db_uri = "mongodb://" + db_username + ":" + db_password + "@mongo:27017/"

client = MongoClient(db_uri)

dbnames = client.list_database_names()
if str(config.DB_NAME) not in dbnames:
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(THIS_FOLDER, "users.csv")) as csv_file:
        fieldnames = ("username","password")
        reader = csv.DictReader( csv_file, fieldnames)
        next(reader)
        out = json.dumps( [ row for row in reader ] )
        users = json.loads(out)
        for user in users:
            user["password"] = get_password_hash(user["password"])
            print(user)
            client[str(config.DB_NAME)].users.insert_one(user)
    with open(os.path.join(THIS_FOLDER, "vehicles.csv")) as csv_file:
        fieldnames = ("id","distance","owner")
        reader = csv.DictReader( csv_file, fieldnames)
        next(reader)
        out = json.dumps( [ row for row in reader ] )
        vehicles = json.loads(out)
        for vehicle in vehicles:
            print(vehicle)
            client[str(config.DB_NAME)].vehicles.insert_one(vehicle)

def get_db_connection():
    return client[str(config.DB_NAME)]