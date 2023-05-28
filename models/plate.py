"""classes"""
from abc import ABC, abstractmethod


class Plate(ABC):  # pylint: disable=too-few-public-methods
    """Abstract Plate"""

    instance = None

    # pylint: disable=too-many-arguments
    def __init__(self, diameter=0.1, material=None, color=None, is_clean=False, has_food=False):
        self.diameter = diameter
        self.material = material
        self.color = color
        self.is_clean = is_clean
        self.has_food = has_food

    @abstractmethod
    def get_max_food_weight(self):
        """counts the weight of food"""

    @classmethod
    def get_instance(cls):
        """return def constructor"""
        if cls.instance is None:
            cls.instance = Plate()
        return cls.instance

    def wash(self):
        """washes the plate and shows whether it is clean"""
        self.is_clean = True

    def dirty(self):
        """shows that the plate is dirty"""
        self.is_clean = False

    def eat(self):
        """doesn't show that there is food and shows that the plate is dirty"""
        self.has_food = False

    def add_food(self):
        """shows that there is food on the plate"""
        self.has_food = True

    def __str__(self):
        return f"{self.diameter}, {self.material}, {self.color}, {self.is_clean}, {self.has_food}"
