from Vehicle import Vehicle
from parking_lot.python.spotType import SpotType

class Bike(Vehicle):
    def get_required_spot_size(self) -> SpotType:
        return SpotType.BIKE