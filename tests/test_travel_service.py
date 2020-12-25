from unittest import TestCase

from process_input import TravelDataStructInput
from travel_service import travel_agency


class TestTravelService(TestCase):
    def test_itinerary_single_hop_by_sea(self):
        data_struct = TravelDataStructInput(
            number_of_hops=1,
            number_of_passengers=1,
            customers_orders=[
                {0: "by-sea"}
            ]
        )
        travel = travel_agency(data_struct)
        travel.print_itinerary()
        self.assertEqual([(0, 'by-sea')], travel.itinerary)

    def test_itinerary_single_hop_airborne(self):
        data_struct = TravelDataStructInput(
            number_of_hops=1,
            number_of_passengers=1,
            customers_orders=[
                {0: "airborne"}
            ]
        )
        travel = travel_agency(data_struct)
        travel.print_itinerary()
        self.assertEqual([(0, 'airborne')], travel.itinerary)

    def test_itinerary_example_sample(self):
        data_struct = TravelDataStructInput(
            number_of_hops=6,
            number_of_passengers=4,
            customers_orders=[
                {0: "by-sea", 2: "by-sea", 3: "by-sea"},
                {0: "by-sea", 5: "airborne"},
                {0: "airborne", 5: "by-sea"},
                {2: "airborne"},
            ]
        )
        travel = travel_agency(data_struct)
        travel.print_itinerary()
        self.assertEqual(
            [(0, 'by-sea'), (1, 'by-sea'), (2, 'airborne'),
             (3, 'by-sea'), (4, 'by-sea'), (5, 'by-sea')], travel.itinerary
        )

    def test_itinerary_example_sample_no_itinerary(self):
        data_struct = TravelDataStructInput(
            number_of_hops=2,
            number_of_passengers=3,
            customers_orders=[
                {0: "by-sea"},
                {0: "airborne"},
                {1: "by-sea"},
            ]
        )
        travel = travel_agency(data_struct)
        travel.print_itinerary()
        self.assertIsNone(travel.itinerary)
