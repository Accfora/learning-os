from utils.statistics import calculate_average, find_min, find_max
from utils.reader import read_numbers
from pathlib import Path
import logging
import json

with open(Path("config.json"), "r", encoding="utf-8") as file:
    config = json.load(file)

input_file = config["input_file"] ### > JSON
log_file = config["log_file"] ### > JSON

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8",
)

logging.info("BEGIN of program.")

def validate_numbers(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty.")

def main():
    current_directory = Path.cwd()

    file = Path(f'{current_directory}/{input_file}') ### > JSON
    try:
        numbers = read_numbers(file)
        logging.info(f"File successfully read: {file}")
        logging.info(f"Number of values read: {len(numbers)}")

        validate_numbers(numbers)

        print(f'\nCurrent directory: {current_directory}')
        print(f'avg = {calculate_average(numbers)}')
        print(f'min = {find_min(numbers)}')
        print(f'max = {find_max(numbers)}')

    except FileNotFoundError:
        logging.error(f"File not found: {file}")
        print("File not found.")
    except ValueError as e:
        if str(e) == "The list of numbers is empty.":
            logging.error("The list of numbers is empty.")
            print(f"Error: {e}")
        else:
            logging.error(f"Invalid data in the file: {file}")  
            print(f"Invalid data in the file.")

if __name__ == "__main__":
    main()

logging.info("END of program.")