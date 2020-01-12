from app.db.connection import get_db_connection, get_mongo_asc

from app.models.vehicles import Vehicle, VehiclesInList

from pymongo import ASCENDING


db = get_db_connection()

# For a given 'username', retrieves from the database all the vehicles associated to this user,
# sorted by distance - first the ones that are at a closer distance
def get_vehicles_by_username(username: str):
    vehicles = db.vehicles.find({"owner": username}).sort([("distance", get_mongo_asc())])
    if vehicles:
        listOfVs = []
        for i in vehicles:
            print(Vehicle(**i))
            listOfVs.append(Vehicle(**i))
        return VehiclesInList(listOfVs)