

export enum VehicleType {
    BIKE = "BIKE",
    CAR = "CAR",
    BUS = "BUS"
}


export enum SpotType {
    COMPACT = "COMPACT",
    MEDIUM = "MEDIUM",
    LARGE = "LARGE"
}

export enum TicketStatus {
    ACTIVE = "ACTIVE",
    PAID = "PAID",
    CLOSED = "CLOSED",
    INVALID = "INVALID"
}

export enum SpotStatus{
    OCCUPIED = "OCCUPIED",
    FREE = "FREE",
    OUTOFORDER = "OUTOFORDER"
}

export const COMPATIBLE_SPOTS : Record <VehicleType,SpotType[]> = {
    [VehicleType.BIKE] : [SpotType.COMPACT,SpotType.COMPACT,SpotType.LARGE],
    [VehicleType.CAR] : [SpotType.COMPACT,SpotType.LARGE],
    [VehicleType.BUS] : [SpotType.COMPACT,SpotType.LARGE],
}