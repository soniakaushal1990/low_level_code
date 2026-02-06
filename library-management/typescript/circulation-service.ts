import { LibraryStore , LibraryPolicy }  from "./libraryStore";
import { Loan } from "./entities";

type ID = string ;


class CirrulationService {
    constructor(private store : LibraryStore, private policy : LibraryPolicy){

    }

    checkout(memberId : ID , copyId : ID) : Loan {

        // Invariants 
        // Member exists and is active
        // member loan < limit
        // book copy eixts and is avaibale //
        //actions
        //copy has no loan
        // create loan
        //update store by loanId and activeLoanByCopyId
        throw new Error("Not Implemented");
    }

    returnCopy(copyId : ID) : void {

        //Invariants
        //Active Loand exists for this copy

        // actions
        //update the store
        //close the loan
        // make copy available
        // hooks
        // fine cal
        // payment
        //notify

        throw new Error("Not Implemented");
    }
}