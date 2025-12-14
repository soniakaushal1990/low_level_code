from datetime import datetime
from ParkingSpot import ParkingSpot
from PricingPolicy import PricingPolicy
from Vehicle import Vehicle
from Ticket import Ticket
from PricingPolicy import PricingPolicy
from Receipt import Receipt

class ParkingLot:
    def __init__(self,spots: list[ParkingSpot], pricing_policy: PricingPolicy):
        self.spots = spots
        self.pricing_policy = pricing_policy

        self.active_tickets: dict[str , Ticket] = {}
        self.spot_by_id = dict[int, ParkingSpot] = {s.spot_id : s for s in spots}

        self._ticket_counter = 1

    def find_spot(self,vehicle:Vehicle) -> ParkingSpot | None:
        for spot in self.spots:
            if spot.has_vehicle():
                continue
            if spot.can_fit(vehicle):
                return spot
        return None

    def _next_ticket_id(self) -> str:
        ticket_id = f"T-{self._ticket_counter}"
        self._ticket_counter += 1
        return ticket_id 
            
    def park(self,vehicle: Vehicle) -> Ticket:
        spot = self.find_spot(vehicle)
        if spot is None:
            raise Exception("No spot availabe")
        
        parked = spot.park(vehicle)

        if not parked:
            raise Exception("Failed to park")
        
        ticket = Ticket(
            ticket_id=self._next_ticket_id(),
            license_no=vehicle.get_license_no(),
            spot_id=spot.spot_id,
            entry_time=datetime.now(datetime.timezone.utc)
        )

        self.active_tickets[ticket.ticket_id] = ticket
        return ticket

    def unpark(self, ticket_id: str) -> Receipt:
        ticket = self.active_tickets.get(ticket_id)
        if ticket is None: 
            raise Exception("Ticket not valid")
        
        spot = self.spot_by_id.get(ticket.spot_id)

        if spot is None: 
            raise Exception("Spot not found for ticket")
        vehicle = spot.unpark()

        if vehicle is None:
            raise Exception("Spot already empty")
        
        exit_time = datetime.now(datetime.timezone.utc)
        ticket.close(exit_time)

        amount = self.pricing_policy.calculate(ticket,exit_time)

        receipt = Receipt(
            ticket_id=ticket.ticket_id,
            license_no=ticket.license_no,
            spot_id=ticket.spot_id,
            entry_time=ticket.entry_time,
            exit_time=exit_time,
            amount=amount
        )
        del self.active_tickets[ticket_id]
        return receipt


