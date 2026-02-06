import { BookCopyStatus, FineStatus, HoldStatus, ID, Role } from "./types";

export abstract class User {
    constructor(
        public readonly id : string,
        public name : string,
        public email : string,
        public readonly role : Role

    ){}
}


export class Member extends User {
    constructor(
        id : string,
        name : string,
        email : string, 
        public maxActiveLoans : number = 5,
        public isActive : boolean = true
    ){
        super(id,name,email,Role.MEMBER);
    }
}


export class Librarian extends User {
    constructor(
        id : string,
        name : string,
        email : string, 
     
    ){
        super(id,name,email,Role.MEMBER);
    }
}

// Catalog and inventory

export class Book {
    constructor(
        public id : string,
        public readonly bookId : string,
        public authors : string []= [],
        public subjects : string [] = []

    ){}
}

export class BookCopy {
    constructor(public readonly id : string,
        public readonly bookId : string,
        public barcode : string,
        public status : BookCopyStatus = BookCopyStatus.AVAILABLE
    
    ){}
}

export class Loan {
    constructor(
        public readonly id : ID,
        public readonly memberId : ID,
        public readonly copyId : ID,
        public checkoutAt : Date,
        public dueAt : Date,
        public returedAt : Date | null = null,
        public renewCount : number = 0     
    ){}

    get isActive(){
        return this.returedAt === null;
    }
}


export class Hold {
    constructor(
        public readonly id : ID,
        public readonly memberId : ID,
        public readonly loanId : ID,
        public placedAt :Date,
        public status : HoldStatus.WAITING

    ){}
}

export class Fine {
    constructor(
        public readonly id : ID,
        public readonly memberId : ID,
        public readonly loanId : ID,
        public reason : "Overdue" | "Lost" | "Damaged",
        public status : FineStatus = FineStatus.UNPAID,
        public createdAt : Date = new Date()
    ){

    }
}







