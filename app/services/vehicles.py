from models.vehicles import Vehicle, VehiclesInList
from db.repositories.vehicles import get_vehicles_by_username

def get_vehicles(username: str):
    vehicles = get_vehicles_by_username(username)
    if vehicles:
        return vehicles