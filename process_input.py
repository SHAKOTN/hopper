from itertools import chain

from dataclasses import dataclass
from sys import stdin
from typing import List
from typing import TextIO
from typing import Dict

from constants import WaysToTravel


class ValidationError(Exception):
    pass


@dataclass
class TravelDataStructInput:
    """
    Data class to operate with input data
    Serves for data `serialization` from customer IQM input format
    """
    number_of_hops: int
    number_of_passengers: int
    # len of this tuple equals to number_of_passengers
    customers_orders: List[Dict[int, str]]

    def _validate(self) -> None:
        assert isinstance(self.number_of_hops, int)
        assert isinstance(self.number_of_passengers, int)

        if not self.number_of_passengers == len(self.customers_orders):
            raise ValidationError(
                "There is not enough data about each customer orders or the number of passengers"
                " is incorrect"
            )

        if max(
            chain.from_iterable([list(order.keys()) for order in self.customers_orders])
        ) > self.number_of_hops - 1:
            raise ValidationError("Invalid number of hops")

        if self.number_of_passengers > 400:
            raise ValidationError(
                "According to requirements there should be at most 400 customers"
            )

        for customer_order in self.customers_orders:
            # Validate that each customer has at most one demand to travel by plane
            if len([way_to_travel for way_to_travel in customer_order.values()
                    if way_to_travel == WaysToTravel.AIRBORNE.value]) > 1:
                raise ValidationError("Customer cannot request more than one trip by plane")

    def __post_init__(self):
        self._validate()


def read_from_file(file_path: str) -> TravelDataStructInput:
    with open(file_path, 'r') as input_file:
        return _read_input(input_file)


def read_from_stdin() -> TravelDataStructInput:
    return _read_input(stdin)


def _read_input(input_object: TextIO):
    number_of_hops = 0
    number_of_passengers = 0
    customers_orders = []
    for index, line in enumerate(input_object):
        stripped_line = line.lstrip().rstrip()
        if index == 0:
            number_of_hops = int(stripped_line)
        elif index == 1:
            number_of_passengers = int(stripped_line)
        else:
            customer_order_unparsed = str(stripped_line).split(", ")
            customers_orders.append(
                {int(hop[0]): hop[2:]for hop in customer_order_unparsed}
            )
    return TravelDataStructInput(
        number_of_hops,
        number_of_passengers,
        customers_orders
    )
