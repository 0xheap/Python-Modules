#!/usr/bin/env python3
"""
Exercise 5: Specialized Plant Types.

Creates specialized plant types using inheritance.
Demonstrates inheritance, super(), and polymorphism.
"""


class Plant:
    """
    Base class for all plants.

    Attributes:
        name (str): The plant's name.
        height (int): The plant's height in centimeters.
        age (int): The plant's age in days.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a basic plant.

        Args:
            name: The plant's name.
            height: The plant's height in centimeters.
            age: The plant's age in days.
        """
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    A flowering plant with color.

    Inherits from Plant and adds flower-specific attributes.

    Attributes:
        color (str): The flower's color.
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a flower.

        Args:
            name: The flower's name.
            height: The flower's height in centimeters.
            age: The flower's age in days.
            color: The flower's color.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        """
        Make the flower bloom.

        Returns:
            A message about the flower blooming.
        """
        return f"{self.name} is blooming beautifully!"

    def information(self) -> str:
        return (
            f"{self.name} (Flower): {self.height}cm, {self.age} days, "
            f"{self.color} color"
        )


class Tree(Plant):
    """
    A tree with trunk diameter.

    Inherits from Plant and adds tree-specific attributes.

    Attributes:
        trunk_diameter (int): The tree's trunk diameter in centimeters.
    """

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        """
        Initialize a tree.

        Args:
            name: The tree's name.
            height: The tree's height in centimeters.
            age: The tree's age in days.
            trunk_diameter: The trunk diameter in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        """
        Calculate shade area produced by the tree.

        Returns:
            A message with the shade area in square meters.
        """
        shade_area = self.trunk_diameter * (3.14 / 2)
        return f"{self.name} provides {shade_area} square meters of shade"

    def information(self) -> str:
        return (
            f"{self.name} (Tree): {rose.height}cm, {rose.age} days, "
            f"{self.trunk_diameter} diameter"
        )


class Vegetable(Plant):
    """
    A vegetable plant with harvest information.

    Inherits from Plant and adds vegetable-specific attributes.

    Attributes:
        harvest_season (str): When to harvest the vegetable.
        nutritional_value (str): Nutritional information.
    """

    def __init__(
        self, name: str, height: int, age: int, harvest_season: str,
        nutritional_value: str
    ) -> None:
        """
        Initialize a vegetable.

        Args:
            name: The vegetable's name.
            height: The vegetable's height in centimeters.
            age: The vegetable's age in days.
            harvest_season: When to harvest.
            nutritional_value: Nutritional information.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def information(self) -> str:
        return (
            f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
            f"{self.harvest_season} harvest"
        )


print("=== Garden Plant Types ===\n")
rose = Flower("Rose", 25, 30, "red")
print(rose.information())
print(rose.bloom() + '\n')

oak = Tree("Oak", 500, 1825, 50)
print(oak.information())
print(oak.produce_shade() + '\n')

tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin c")
print(tomato.information())
print(f"{tomato.name} is rich in {tomato.nutritional_value}")
