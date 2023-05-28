"""classes"""

from .plate import Plate


class CoffeePlate(Plate):
    """CoffeePlate"""

    # pylint: disable=too-many-arguments
    def __init__(self, diameter=0.1, material=None, color=None, is_clean=False, has_food=False,
                 weight=None):
        super().__init__(diameter, material, color, is_clean, has_food)
        self.weight = weight

    def get_max_food_weight(self):
        """counts the weight of food"""


def __str__(self):
    return f"{self.diameter} {self.material} {self.color} {self.is_clean} {self.has_food}" \
           f"{self.weight}"
