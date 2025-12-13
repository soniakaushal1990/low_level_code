from Vehicle import Vehicle
from ParkingSpot import ParkingSpot
from typing import Optional,List,Dict


class ParkingLot:
   
    MAX_SPOTS = 1000
   
    def __init__(self,spots: List[ParkingSpot]):
        if len(spots) > self.MAX_SPOTS:
            raise ValueError(f"Max spots allowed is {self.MAX_SPOTS}")
        
        self.spots : List[ParkingSpot] = spots
        self.spot_by_id : Dict[int,ParkingSpot] = {s.spot_id: s for s in spots}

    def park(self,vehicle: Vehicle) -> Optional[ParkingSpot]:  
        
        best_spot: Optional[ParkingSpot] = None

        for spot in self.spots:
            if spot.isOccupied():
                continue
            if not spot.fits(vehicle):
                continue 

            if best_spot is None or spot.size < best_spot.size:
                best_spot = spot

        if best_spot is None:
            return None
        
        best_spot.park(vehicle)

        return best_spot


    def free(self,spot_id : int) -> bool :
        spot = self.spot_by_id.get(spot_id)
        if spot is None:
            return False
        spot.unpark()
        return True
    
    def available_spots_count(self) -> int:
        return sum(1 for s in self.spots if not s.isOccupied())
    

    
    




    

        
    

        

