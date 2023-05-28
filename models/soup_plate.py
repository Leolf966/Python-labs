"""classes"""

from .plate import Plate


class SoupPlate(Plate):
    """SoupPlate"""

    # pylint: disable=too-many-arguments
    def __init__(self, diameter=0.1, material=None, color=None, is_clean=False, has_food=False,
                 depth=3.5, soup="borsch"):
        super().__init__(diameter, material, color, is_clean, has_food)
        self.depth = depth
        self.soup = soup

    def get_max_food_weight(self):
        return 3.14*self.diameter*self.diameter()*self.depth/8

    def __str__(self):
        return f"{self.diameter} {self.material} {self.color} {self.is_clean} {self.has_food} " \
               f"{self.depth} {self.soup}"
