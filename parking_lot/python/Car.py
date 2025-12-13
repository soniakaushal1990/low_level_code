from Vehicle import Vehicle
from VehicleSize import VehicleSize

class Car(Vehicle):
    def __init__(self, license_number:str):
        super().__init__(license_number,VehicleSize.MEDIUM)

    def get_type(self) -> str:
        return "CAR"
        



