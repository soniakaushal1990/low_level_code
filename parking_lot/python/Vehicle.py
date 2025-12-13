from abc import ABC
from VehicleSize import VehicleSize
from abc import abstractmethod

class Vehicle(ABC):
    def __init__(self,license_no:str,size:VehicleSize):
        self._license_no = license_no
        self._size = size

    def get_license_number(self) -> str:
        return self._license_no
    
    def get_size(self) -> str:
        return self._size
    
    @abstractmethod
    def get_type(self) -> str:
        return "Vehicle"
    


        