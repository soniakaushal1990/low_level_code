from abc import ABC, abstractmethod
from Ticket import Ticket
from Receipt import Receipt

class PricingPolicy:
    @abstractmethod
    def calculate(self,ticket:Ticket,exit_time) -> float:
        pass