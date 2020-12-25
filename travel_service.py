from dataclasses import dataclass
from typing import Dict

from constants import WaysToTravel
from process_input import TravelDataStructInput
from itertools import product


@dataclass
class Customer:
    hops: Dict[int, str]
    satisfied: bool = False


class PacificTravelAgency:
    def __init__(self, data: TravelDataStructInput):
        self.number_of_hops = data.number_of_hops
        self.number_of_passengers = data.number_of_passengers
        self.customers = [Customer(order_map) for order_map in data.customers_orders]
        self.itinerary = None
        self.possible_itineraries_pairs = []

        # Initialize all possible itineraries and sort them by the amount of "airborne" ascending
        # by using product
        for itinerary in sorted(    
            product(
                [WaysToTravel.BY_SEA.value, WaysToTravel.AIRBORNE.value], repeat=self.number_of_hops
            ),
            key=lambda i: i.count(WaysToTravel.AIRBORNE.value)
        ):
            itinerary_pairs = []
            for island, travel_way in enumerate(itinerary):
                itinerary_pairs.append((island, travel_way))
            self.possible_itineraries_pairs.append(itinerary_pairs)

    def are_all_customers_satisfied(self) -> bool:
        return False not in [customer.satisfied for customer in self.customers]

    def _reset_customers(self) -> None:
        for customer in self.customers:
            customer.satisfied = False

    def print_itinerary(self) -> None:
        for itinerary in self.possible_itineraries_pairs:
            for customer in self.customers:
                if any(hop in itinerary for hop in customer.hops.items()):
                    customer.satisfied = True
            if self.are_all_customers_satisfied():
                print(itinerary)
                self.itinerary = itinerary
                break
            else:
                self._reset_customers()
        if not self.itinerary:
            print("NO ITINERARY")


travel_agency = PacificTravelAgency
