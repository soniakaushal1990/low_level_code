from parking_lot.python.spotType import VehicleSize, SpotSize
from Vehicle import Vehicle

class Car(Vehicle):
    def get_required_spot_size(self) -> SpotSize:
        return SpotSize.COMPACT
