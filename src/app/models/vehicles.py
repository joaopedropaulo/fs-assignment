from pydantic import BaseModel
from typing import List

class Vehicle(BaseModel):
    id: str
    distance: int

class VehiclesInList(List[Vehicle]):
    vehicles: List[Vehicle]