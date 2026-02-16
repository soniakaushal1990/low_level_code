import { Policy } from "./policies";
import { VehicleType , SpotType ,SpotStatus, TicketStatus} from "./types";


export class Vehicle {
    constructor(
     public readonly vehicleType : VehicleType,
     public readonly plateNo : string
    ){}
    // Implement the Vehicle class methods
}

export class ParkingSpot {
   private spotStatus: SpotStatus = SpotStatus.FREE;
   private occupiedBy?:Vehicle;

    constructor(
        public readonly id : string,
        public readonly type : SpotType
    ){}
}



export class Ticket{
    public readonly status : TicketStatus = TicketStatus.ACTIVE;
    public readonly issuesAt:Date = new Date();
    public readonly paidAt?: Date;


    constructor(
        public readonly id : string,
        public readonly vehicleType : VehicleType,
        public readonly spotId: string
    ){

    }
}


export class ParkingLot {

    private parkingSpots :Map<string, ParkingSpot>;
    private ticketSeq = 0;

    constructor(
        public readonly id : string,
        parkingSpots : ParkingSpot[],
        private readonly pricing : Policy

    ){
            this.parkingSpots = new Map(parkingSpots.map(s => [s.id,s]))
    }


    public parkVehicle(){

    }

    public payAndExit(){

    }

    private issueTicket(){
        
    }
}