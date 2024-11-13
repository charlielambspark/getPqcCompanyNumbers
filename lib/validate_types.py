import sys
from typing import List
from pathlib import Path

def validate_types(types: List[str]):
    if len(types) not in [2, 3]:
        exit_with_comments()

    input_path, output_path = Path(types[0]).resolve(), Path(types[1]).resolve()

    if not input_path.is_file():
        print("Input file does not exist")
        sys.exit(1)

    max_num = None
    if len(types) == 3:
        try:
            max_num = int(types[2])
            if max_num <= 0:
                print("Max length must be a positive integer")
                sys.exit(1)
        except ValueError:
            print("Max length must be a positive integer")
            sys.exit(1)

    return input_path, output_path, max_num

def exit_with_comments():
    print("Usage: python3 main.py <input_file> <output_file> [max_length]")
    print("The max_length argument is optional and must be a positive integer.")
    sys.exit(1)