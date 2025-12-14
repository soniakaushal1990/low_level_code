from datetime import datetime


class Ticket:
    def __init__(
        self,
        ticket_id: str,
        license_no: str,
        spot_id: int,
        entry_time: datetime
    ):
        self.ticket_id = ticket_id
        self.license_no = license_no
        self.spot_id = spot_id
        self.entry_time = entry_time
        self.exit_time: datetime | None = None

    def close(self, exit_time) -> datetime | None:
        self.exit_time = exit_time