"""main"""
from managers.plate_manager import add_plate, plates
from managers.plate_manager import find_all_with_diameter_greater_than, find_all_with_color_white
from models.salad_plate import SaladPlate
from models.soup_plate import SoupPlate
from models.pie_plate import PiePlate
from models.coffee_plate import CoffeePlate

if __name__ == "__main__":

    add_plate(CoffeePlate(2.7, "clay", "brown", True, True, 400))
    add_plate(CoffeePlate(2.9, "ceramic", "white", True, True, 350))
    add_plate(SaladPlate(2.4, "metal", "white", True, True, "oval", True))
    add_plate(SoupPlate(3.5, "ceramic", "blue", True, True, 12, "Borsch"))
    add_plate(SoupPlate())
    add_plate(PiePlate(2.8, "plastic", "white", True, True, "polka-dot"))
    add_plate(PiePlate())

    for plate in plates:
        print(plate)
    print('_' * 50)

    for i in find_all_with_diameter_greater_than(2.7):
        print(i)
    print('_' * 50)

    for i in find_all_with_color_white():
        print(i)
    print('_' * 50)
