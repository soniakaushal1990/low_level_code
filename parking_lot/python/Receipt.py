from datetime import datetime


class Receipt:
    def __init__(self,              
        ticket_id: str,
        license_no : str,
        amount : float,
        entry_time : datetime,
        exit_time : datetime           
    ):
        
        self.ticket_id = ticket_id
        self.license_no = license_no
        self.amount = amount
        self.entry_time = entry_time
        self.exit_time = exit_time  
  