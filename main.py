import logging
import argparse

from process_input import read_from_file
from process_input import read_from_stdin
from travel_service import travel_agency

logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_path")
    args = parser.parse_args()
    if args.file_path:
        data_struct = read_from_file(args.file_path)
    else:
        data_struct = read_from_stdin()
    travel_agency(data_struct).print_itinerary()
