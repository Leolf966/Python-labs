"""classes"""

from .plate import Plate


class SaladPlate(Plate):
    """SaladPlate"""

    # pylint: disable=too-many-arguments
    def __init__(self, diameter=0.1, material=None, color=None, is_clean=False, has_food=False,
                 form="oval", dish_washer_acceptable=True):
        super().__init__(diameter, material, color, is_clean, has_food)
        self.form = form
        self.dish_washer_acceptable = dish_washer_acceptable

    def get_max_food_weight(self):
        return 3.14*self.diameter*self.diameter*self.diameter/24

    def __str__(self):
        return f"{self.diameter} {self.material} {self.color} {self.is_clean} {self.has_food} " \
               f"{self.form} {self.dish_washer_acceptable}"
