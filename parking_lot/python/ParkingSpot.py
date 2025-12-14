from Vehicle import Vehicle
from spotType import SpotType

class ParkingSpot():
    _counter = 1

    def __init__(self,type:SpotType):
        self.spot_id = ParkingSpot._counter
        ParkingSpot._counter += 1

        self.type = type
        self.vehicle : Vehicle | None = None

    def has_vehicle(self) -> bool:
        return self.vehicle is not None
    
    def can_fit(self,vehicle:Vehicle) -> bool:
        return self.type.value >= vehicle.get_required_spot_size().value
    
    def park(self,vehicle: Vehicle) -> bool:
        if self.has_vehicle():
            return False
        if not self.can_fit(vehicle):
            return False
        self.vehicle = vehicle
        return True
    
    def unpark(self) -> Vehicle | None:
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle