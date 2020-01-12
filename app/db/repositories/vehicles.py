from db.connection import get_db_connection, get_mongo_asc

from models.vehicles import Vehicle, VehiclesInList

from pymongo import ASCENDING


db = get_db_connection()

def get_vehicles_by_username(username: str):
    vehicles = db.vehicles.find({"owner": username}).sort([("distance", get_mongo_asc())])
    if vehicles:
        listOfVs = []
        for i in vehicles:
            print(Vehicle(**i))
            listOfVs.append(Vehicle(**i))
        return VehiclesInList(listOfVs)