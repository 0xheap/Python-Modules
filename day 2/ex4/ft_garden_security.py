#!/usr/bin/env python3
"""
Exercise 4: Garden Security System.

Protects plant data from corruption using encapsulation and validation.
Demonstrates private attributes, getters, and setters.
"""


class SecurePlant:
    """
    A plant with protected data and validation.

    Uses name mangling to protect height and age attributes.
    Validates all modifications to prevent invalid data.

    Attributes:
        name (str): The plant's name (public).
        __height (int): The plant's height in cm (private).
        __age (int): The plant's age in days (private).
    """

    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        """
        Initialize a secure plant with validation.

        Args:
            name: The plant's name.
            height: Initial height in centimeters (default: 0).
            age: Initial age in days (default: 0).
        """
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """
        Set plant height with validation.

        Args:
            height: New height value in centimeters.

        Prints error message if height is negative.
        """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age: int) -> None:
        """
        Set plant age with validation.

        Args:
            age: New age value in days.

        Prints error message if age is negative.
        """
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")

    def get_height(self) -> int:
        """
        Get the plant's current height.

        Returns:
            The plant's height in centimeters.
        """
        return self.__height

    def get_age(self) -> int:
        """
        Get the plant's current age.

        Returns:
            The plant's age in days.
        """
        return self.__age

    def plant_information(self) -> str:
        return (
            "Current plant: "
            f"{self.name} ({self.__height}cm, {self.__age} days)"
        )


print("=== Garden Security System ===")
rose = SecurePlant("Rose", 25, 30)
rose.set_height(55)
print("\n" + rose.plant_information())
