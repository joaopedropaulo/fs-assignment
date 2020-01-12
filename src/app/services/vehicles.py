from app.models.vehicles import Vehicle, VehiclesInList
from app.db.vehicles import get_vehicles_by_username

# Service for vehicles operations

def get_vehicles(username: str):
    vehicles = get_vehicles_by_username(username)
    if vehicles:
        return vehicles