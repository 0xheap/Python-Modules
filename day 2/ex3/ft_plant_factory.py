#!/usr/bin/env python3
"""
Exercise 3: Plant Factory.

Streamlines plant creation process using list comprehension.
Demonstrates efficient object instantiation and iteration.
"""


class Plant:
    """
    Represents a plant with basic attributes.

    Attributes:
        Name (str): The plant's name.
        Height (int): The plant's height in centimeters.
        Age (int): The plant's age in days.
    """

    total = 0

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


plants_data = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120),
]

plants = [Plant(name, height, age) for name, height, age in plants_data]
size = 0
print("=== Plant Factory Output ===")
for plant in plants:
    size += 1
    print(f"Created: {plant.Name} ({plant.Height}cm, {plant.Age} days)")

print(f"\nTotal plants created: {size}")
