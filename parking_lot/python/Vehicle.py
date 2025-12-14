from parking_lot.python.spotType import VehicleSize , SpotSize
from abc import ABC , abstractmethod

class Vehicle(ABC):
    def __init__(self,license_no:str):
        self._license_no = license_no

    def get_license_no(self) -> str:
        return self._license_no
    
    @abstractmethod
    def get_required_spot_size(self) -> SpotSize:
        pass 

    

        