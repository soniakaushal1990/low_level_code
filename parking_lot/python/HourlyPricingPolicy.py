from PricingPolicy import PricingPolicy
from datetime import datetime
import math


class HourlyPricingPolicy(PricingPolicy):
    def __init__(self,rate_per_hour: float):
        self.rate_per_hour = rate_per_hour

    def calculate(self, ticket, exit_time):
        dur_seconds = (exit_time - ticket.entry_time).total_seconds()
        dur_hours = math.ceil(dur_seconds / 3600)
        return dur_hours * self.rate_per_hour
    

        