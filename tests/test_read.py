from unittest import TestCase
from unittest.mock import patch, mock_open

from process_input import read_from_file


class TestReadInput(TestCase):

    def test_read(self):
        with patch('builtins.open', mock_open(
                read_data="""6
4
0 by-sea, 2 by-sea, 3 by-sea
0 by-sea, 5 airborne
0 airborne, 5 by-sea
2 airborne""")):
            data_struct = read_from_file("whatever")
            self.assertEqual(6, data_struct.number_of_hops)
            self.assertEqual(4, data_struct.number_of_passengers)