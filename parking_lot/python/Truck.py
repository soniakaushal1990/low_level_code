from Vehicle import Vehicle
from VehicleSize import VehicleSize

class Truck(Vehicle):
    def __init__(self, license_no):
        super().__init__(license_no, VehicleSize.LARGE)

    def get_type(self) -> str:
        return "TRUCK"