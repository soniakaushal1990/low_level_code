from Vehicle import Vehicle
from VehicleSize import VehicleSize

class Byke(Vehicle):
    def __init__(self, license_no):
        super().__init__(license_no, VehicleSize.SMALL)

    def get_type(self) -> str:
        return "BYKE"