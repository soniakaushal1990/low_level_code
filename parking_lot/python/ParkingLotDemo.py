from ParkingLot import ParkingLot
from ParkingSpot import ParkingSpot
from VehicleSize import VehicleSize
from Car import Car
from Byke import Byke
from Truck import Truck

class ParkingLotDemo:

    @staticmethod
    def main():
        spots = ([ParkingSpot(VehicleSize.SMALL) for _ in range(300)] +
                 [ParkingSpot(VehicleSize.MEDIUM) for _ in range(500)] +
                 [ParkingSpot(VehicleSize.LARGE) for _ in range(200)]
        )

        lot = ParkingLot(spots)

        vehicles = [
            Car("CAR-101"),
            Car("CAR-102"),
            Byke("BIKE-201"),
            Truck("TRUCK-301"),
            Car("CAR-103"),
            Byke("BIKE-202"),
            Truck("TRUCK-302"),
        ]

        for v in vehicles:
            spot = lot.park(v)
            if(spot):
                print(f"{v.get_type()} {v.get_license_number()}"
                f" parked at spot {spot.spot_id}"        
                )
            else:
                print("Spot not available")
        

        
if __name__ == '__main__':
    ParkingLotDemo.main()
        

