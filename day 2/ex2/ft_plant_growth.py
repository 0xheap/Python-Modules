#!/usr/bin/env python3
"""
Exercise 2: Plant Growth Simulator.

Simulates plant growth over time with methods to modify plant state.
Demonstrates instance methods and object state changes.
"""


class Plant:
    """
    Represents a plant that can grow and age over time.

    Attributes:
        Name (str): The plant's name.
        Height (int): The plant's height in centimeters.
        Age (int): The plant's age in days.
    """

    def __init__(self, Name: str, Height: int, Age: int) -> None:
        """
        Initialize a new Plant instance.

        Args:
            Name: The plant's name.
            Height: The plant's height in centimeters.
            Age: The plant's age in days.
        """
        self.Name = Name
        self.Height = Height
        self.Age = Age
        self.total_growth = 0

    def age(self, day: int = 1) -> None:
        """
        Age the plant by specified number of days.

        Args:
            day: Number of days to age (default: 1).
        """
        self.Age += day

    def grow(self, cm: int = 1) -> None:
        """
        Grow the plant by specified centimeters.

        Args:
            cm: Centimeters to grow (default: 1).
        """
        self.Height += cm

    def get_info(self):
        """
        Get formatted information about the plant.

        Returns:
            String with plant name, height, and age.
        """
        return f"{self.Name}: {self.Height}cm, {self.Age} days old"


rose = Plant("Rose", 25, 30)

numbers = [0, 1, 2, 3, 4, 5]
for i in numbers:
    if i == 0:
        print("=== Day 1 ===")
        print(rose.get_info())
    rose.grow()
    rose.age()

print("=== Day 7 ===")
print(rose.get_info())
