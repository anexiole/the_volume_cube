import json
import urllib3

from urllib.parse import urlparse

import pprint
import calculator


def main():
    url_path = "/api/products/1"
    all_data = calculator.get_data(url_path)

    average = calculator.calculate_average_weight(all_data, "Air Conditioners")
    print("Average cubic weight is " + str(average))


if __name__ == "__main__":
    main()
