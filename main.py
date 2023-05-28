"""main"""

from plate import Plate

if __name__ == "__main__":

    Plate1 = Plate()
    Plate2 = Plate(2.4, "metal", "white", True, True)
    Plate3 = Plate(3.5, "ceramic", "blue", True, True)
    Plate4 = Plate(2.8, "plastic", "white", True, True)
    Plate.get_instance()
    Plate.get_instance()
    print(Plate1)
    print(Plate2)
    print(Plate3)
    print(Plate4)
