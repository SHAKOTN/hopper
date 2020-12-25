from unittest import TestCase

from process_input import TravelDataStructInput, ValidationError


class TestDataStructs(TestCase):
    def test_struct_valid(self):
        data_struct = TravelDataStructInput(
            number_of_hops=1,
            number_of_passengers=1,
            customers_orders=[
                {0: "by-sea"}
            ]
        )
        self.assertEqual(1, data_struct.number_of_hops)
        self.assertEqual(1, data_struct.number_of_passengers)
        self.assertEqual({0: "by-sea"}, data_struct.customers_orders[0])

    def test_unequal_num_of_passengers_vs_orders(self):
        with self.assertRaises(ValidationError) as exc_context:
            TravelDataStructInput(
                number_of_hops=1,
                number_of_passengers=1,
                customers_orders=[
                    {1: "by-sea", 0: "airborne"},
                    {0: "airborne"},
                ]
            )
        self.assertEqual(
            "There is not enough data about each customer "
            "orders or the number of passengers is incorrect", str(exc_context.exception)
        )

    def test_asked_for_plane_more_than_once(self):
        with self.assertRaises(ValidationError) as exc_context:
            TravelDataStructInput(
                number_of_hops=3,
                number_of_passengers=2,
                customers_orders=[
                    {0: "by-sea", 2: "airborne"},
                    {0: "airborne", 1: "airborne"},
                ]
            )
        self.assertEqual(
            "Customer cannot request more than one trip by plane", str(exc_context.exception)
        )

    def test_invalid_amount_of_hops(self):
        with self.assertRaises(ValidationError) as exc_context:
            TravelDataStructInput(
                number_of_hops=1,
                number_of_passengers=2,
                customers_orders=[
                    {0: "by-sea", 2: "airborne"},
                    {0: "airborne", 2: "airborne"},
                ]
            )
        self.assertEqual(
            "Invalid number of hops", str(exc_context.exception)
        )

    def test_raise_if_more_than_400_customers(self):
        with self.assertRaises(ValidationError) as exc_context:
            TravelDataStructInput(
                number_of_hops=1,
                number_of_passengers=401,
                customers_orders=[
                    {0: "by-sea"} for _ in range(401)
                ]
            )
        self.assertEqual(
            "According to requirements there should be at most 400 customers",
            str(exc_context.exception)
        )
