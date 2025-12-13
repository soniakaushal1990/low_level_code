from Vehicle import Vehicle
from VehicleSize import VehicleSize
from typing import Optional
from dataclasses import dataclass,field
import itertools

@dataclass

class ParkingSpot:

    size: VehicleSize
    idCounter = itertools.count(1)
    spot_id: int = field(init=False)
    vehicle: Optional[Vehicle] = field(default=None, init=False)

    def __post_init__(self) -> None:
        self.spot_id = next(ParkingSpot.idCounter)

    def isOccupied(self) -> bool:
        return self.vehicle is not None
    
    def fits(self,vehicle:Vehicle) -> bool:
        return self.size >= vehicle.get_size() 
    
    def park(self,vehicle:Vehicle) -> bool:
        if self.isOccupied():
            return False
        if not self.fits(vehicle):
            return False
        self.vehicle = vehicle
        return True

    def unpark(self) -> Optional[Vehicle]:
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle

            

    





    


