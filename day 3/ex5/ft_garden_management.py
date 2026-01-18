"""
Garden Management System - Exception Handling Exercise

This module demonstrates advanced Python exception handling concepts:
- Custom exception hierarchies
- Error recovery and graceful degradation
- Resource management with try/finally blocks
- Input validation with meaningful error messages

Classes:
    GardenError: Base exception for garden-related errors
    PlantError: Exception for plant-specific problems
    WaterError: Exception for water-related issues
    GardenManager: Main class managing plants and watering system
"""


class GardenError(Exception):
    """Base exception for garden-related errors"""
    pass


class PlantError(GardenError):
    """Exception for plant-related problems"""
    pass


class WaterError(GardenError):
    """Exception for water-related problems"""
    pass


class GardenManager:
    """Manages a smart garden system with plants"""
    tank = 10

    def __init__(self):
        """Initialize empty garden"""
        self.plants = {}

    def add_plants(self, plant: str, water: int = 5, sun: int = 6):
        """
        Add a plant to the garden with validation

        Args:
            plant: Plant name
            water: Water level (1-10), default 5
            sun: Sunlight hours (2-12), default 6
        """
        try:
            self.check(plant, water, sun)
            self.plants[plant] = {
                'water': water,
                'sun': sun
            }
            print(f"Added {plant} successfully")
        except GardenError as e:
            print(f"Error adding plant: {e}")

    def checking_tank(self):
        if self.tank <= 0:
            raise GardenError("Not enough water in tank")

    def water_plants(self, plant: str, water: int):
        """
        Water a specific plant

        Args:
            plant: Plant name to water
            water: Amount of water
        """
        try:
            self.checking_tank()
            if plant not in self.plants:
                raise PlantError(f"Plant '{plant}' not found in garden!")

            self.plants[plant]['water'] = water
            print(f"Watering {plant} - success")
            self.tank -= water
        except PlantError as e:
            print(f"Error: {e}")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
            print("System recovered and continuing...")

    def water_all(self, water: int):
        print("Opening watering system")
        try:
            for plant in self.plants:
                self.water_plants(plant, water)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant: str):
        """
        Check and display plant health status

        Args:
            plant: Plant name to check
        """
        try:
            if plant not in self.plants:
                raise PlantError(f"Plant '{plant}' not found!")

            plant_data = self.plants[plant]
            water = plant_data['water']
            sun = plant_data['sun']

            self.check(plant, water, sun)

            print(f"{plant}: healthy (water: {water}, sun: {sun})")

        except GardenError as e:
            print(f"Error checking {plant}: {e}")

    def check(self, plant: str, water: int = 0, sun: int = 0):
        """
        Validate plant parameters

        Args:
            plant: Plant name (cannot be empty)
            water: Water level (must be 1-10)
            sun: Sunlight hours (must be 2-12)

        Raises:
            PlantError: If plant name invalid
            WaterError: If water level invalid
            GardenError: If sunlight hours invalid
        """
        if not plant:
            raise PlantError("Plant name cannot be empty!")

        if water > 10:
            raise WaterError(f"Water level {water} is too high (max 10)")
        elif water < 1:
            raise WaterError(f"Water level {water} is too low (min 1)")

        if sun > 12:
            raise GardenError(f"Sunlight hours {sun} is too high (max 12)")
        elif sun < 2:
            raise GardenError(f"Sunlight hours {sun} is too low (min 2)")


print("=== Garden Management System ===\n")

manager = GardenManager()


print("Adding plants to garden...")
manager.add_plants("tomato", water=5, sun=8)
manager.add_plants("lettuce", water=7, sun=6)
manager.add_plants("", water=5, sun=8)

print("\nWatering plants...")
manager.water_all(5)
print("\nChecking plant health...")
manager.check_plant_health("tomato")

manager.plants["lettuce"]['water'] = 15
manager.check_plant_health("lettuce")

print("\nTesting error recovery...")
manager.water_plants("tomato", 6)
print("\nGarden management system test complete!")
