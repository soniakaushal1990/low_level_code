import { VehicleType } from "./types";

export interface Policy {
    calculateFee(issuedAt:Date,paidAt:Date,VehicleType: VehicleType) :number;
} 



export class HourlyPricingPolicy implements Policy {

    calculateFee(issuedAt: Date, paidAt: Date, VehicleType: VehicleType): number {
       // TODO : Implement this later
        return 0;
    }
}