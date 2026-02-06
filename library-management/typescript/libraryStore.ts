import { Book, BookCopy, Fine, Hold, Librarian, Loan, Member } from "./entities";

type ID = string ;

export class LibraryStore {

    // cataloug
    booksById = new Map<ID , Book>();
    copiesById = new Map<ID,BookCopy>();

    //Users
    membersById = new Map<ID,Member>();
    librarianById = new Map<ID,Librarian>();

    // Cirrulation
    loansById = new Map<ID,Loan>();
    activeLoanByCopyId = new Map<ID, ID>();

    //Holds and Fines
    holdsById = new Map<ID,Hold>();
    finesById = new Map<ID,Fine>();
}

export class LibraryPolicy {
    loanDays = 5;
    maxRenewals = 5;
    maxHolds = 5;
    finePerDayCents = 5;
}