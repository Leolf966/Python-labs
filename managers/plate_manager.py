"""manager"""


plates = []


def add_plate(plate):
    """add plate to list"""
    plates.append(plate)


def find_all_with_diameter_greater_than(number):
    """get list <Plate> when diameter > number"""
    return [obj for obj in plates if obj.diameter > number]


def find_all_with_color_white():
    """"get list <Plate> when color_white >number"""
    return [obj for obj in plates if obj.color == "white"]
