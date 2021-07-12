import requests
import pprint

base_url = "http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com"
industry_conversion_factor = 250

def get_data(url_path):
    url = base_url + url_path
    response = requests.get(url)
    page = response.json()

    data = page["objects"]

    if page["next"]:
        new_data = get_data(page["next"])
        data.extend(new_data)

    return data


def calculate_average_weight(products, category):
    total_cubic_weight = 0
    count_category = 0

    for product in products:
        if product["category"] == "Air Conditioners":
            product["cubic_weight"] = calculate_cubic_weight(product)
            total_cubic_weight += product["cubic_weight"]
            count_category += 1

    return total_cubic_weight / count_category


def calculate_cubic_weight(product):
    cubic_weight_cm = (
        product["size"]["width"]
        * product["size"]["height"]
        * product["size"]["length"]
        * industry_conversion_factor
    )
    cubic_weight_m = cubic_weight_cm / 100
    return cubic_weight_m
