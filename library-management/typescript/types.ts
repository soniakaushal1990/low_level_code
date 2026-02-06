
export type ID = string;


export enum Role {
    LIBRARIAN = "LIBRARIAN",
    MEMBER = "MEMBER"

}

export enum BookCopyStatus {
    AVAILABLE = "AVAILABLE",
    LOANED = "LOANED",
    RESERVED = "RESERVED",
    LOST = "LOST",
    MAINTAINECE = "MAINTAINECE"

}

export enum HoldStatus {
    WAITING = "WAITING",
    READY = "READY",
    CANCELLED = "CANCELLED",
    FUllFILLED = "FUllFILLED",
    EXPIRED = "EXPIRED"

}


export enum FineStatus {
    PAID = "PAID",
    UNPAID = "UNPAID",
    WAIVEd = "WAIVED"
}