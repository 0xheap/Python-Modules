#!/usr/bin/env python3
"""
Exercise 0: Planting Your First Seed.

Basic Python program structure demonstration using if __name__ == "__main__".
Displays information about a plant in the garden.
"""

if __name__ == "__main__":
    plant_name = "Rose"
    plant_height_cm = 25
    plant_age_days = 30

    print("=== Welcome to My Garden ===")
    print("Plant:", plant_name)
    print("Height:", plant_height_cm, "cm", sep=" ")
    print("Age:", plant_age_days, "days", sep=" ")
    print("\n=== End of Program ===")
    c = input(int())
