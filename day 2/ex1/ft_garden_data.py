#!/usr/bin/env python3
"""
Exercise 1: Garden Data Organizer.

Manages multiple plants using a Plant class to organize data efficiently.
Demonstrates basic class structure and object creation.
"""


class Plant:
    """
    Represents a plant in the garden.

    Attributes:
        name (str): The plant's name.
        height (int): The plant's height in centimeters.
        age (int): The plant's age in days.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new Plant instance.

        Args:
            name: The plant's name.
            height: The plant's height in centimeters.
            age: The plant's age in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def info(self) -> str:
        """
        Return string representation of the plant.

        Returns:
            The plant's name, hieght anf age'
        """
        return f"{self.name} : {self.height}cm, {self.age} days old"


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

print("=== Garden Plant Registry ===")
print(rose.info())
print(sunflower.info())
print(cactus.info())
