#!/usr/bin/env python3
"""
Garden Management System - Exercise 6
Simple system to manage plants and gardens.
"""


class Plant:
    """
    A basic plant in the garden.

    Every plant has a name and height.
    Plants can grow taller over time.
    """

    def __init__(self, name: str, height: int) -> None:
        """
        Create a new plant.

        Args:
            name: What to call this plant
            height: How tall it is (in cm)
        """
        self.name = name
        self.height = height

    def grow(self) -> None:
        """Make the plant grow 1cm taller."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    @staticmethod
    def validate_height(height: int) -> bool:
        """
        Check if height is good.

        Args:
            height: Height to check

        Returns:
            True if height is positive, False if negative
        """
        return height > 0

    @staticmethod
    def plant_cat() -> str:
        """Get plant type. Returns 'regular'."""
        return "regular"


class FloweringPlant(Plant):
    """
    A plant that has flowers.

    Like a regular plant but with color and blooming.
    Gets everything from Plant class plus flower stuff.
    """

    def __init__(self, name: str, height: int, flower_color: str) -> None:
        """
        Create a flowering plant.

        Args:
            name: Plant name
            height: How tall it is
            flower_color: What color are the flowers
        """
        super().__init__(name, height)
        self.color = flower_color
        self.blooming = True

    def info(self) -> str:
        """Get nice text about this plant."""
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"

    @staticmethod
    def plant_cat() -> str:
        """Get plant type. Returns 'flowering'."""
        return "flowering"


class PrizeFlower(FloweringPlant):
    """
    Special flowering plant that wins prizes.

    Like FloweringPlant but with points for competitions.
    Gets everything from FloweringPlant plus prize points.
    """

    def __init__(
        self, name: str, height: int, flower_color: str, points: int = 10
    ) -> None:
        """
        Create a prize-winning flower.

        Args:
            name: Plant name
            height: How tall it is
            flower_color: Flower color
            points: Prize points (default is 10)
        """
        super().__init__(name, height, flower_color)
        self.points = points

    def info(self) -> str:
        """Get nice text about this prize flower."""
        parent_info = super().info()
        return f"{parent_info}, Prize points: {self.points}"

    @staticmethod
    def plant_cat() -> str:
        """Get plant type. Returns 'prize'."""
        return "prize"


class GardenManager:
    """
    Manages multiple gardens with analytics.

    Tracks all gardens created and provides comprehensive
    garden management functionality.

    Attributes:
        total_gardens (int): Class variable tracking total gardens created.
    """

    total_gardens: int = 0

    class GardenStats:
        """
        Nested helper class for garden statistics.

        Tracks plant additions, growth, and categorizes plant types.

        Attributes:
            plants_added (int): Total plants added to garden.
            total_growth (int): Cumulative growth in centimeters.
            plant_types (dict): Count of each plant category.
        """

        def __init__(self) -> None:
            """Initialize garden statistics with zero values."""
            self.plants_added = 0
            self.total_growth = 0
            self.plant_types = {"regular": 0, "flowering": 0, "prize": 0}

        def update_growth(self, amount: int = 1) -> None:
            """
            Update total growth tracker.

            Args:
                amount: Growth amount in centimeters (default: 1).
            """
            self.total_growth += amount

        def add_plant(self, plant):
            """
            Record a new plant addition and categorize it.

            Args:
                plant: Plant object to add to statistics.
            """
            self.plants_added += 1
            category = plant.plant_cat()
            self.plant_types[category] += 1

    def __init__(self, owner) -> None:
        """
        Initialize a new garden for an owner.

        Args:
            owner: Name of the garden owner.
        """
        self.owner = owner
        self.plants = []
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant) -> str:
        """
        Add a plant to this garden.

        Args:
            plant: Plant object to add.
        """
        self.plants += [plant]
        self.stats.add_plant(plant)
        return f"Added {plant.name} to {self.owner}'s garden"

    def grow_all_plants(self) -> None:
        """Grow all plants in the garden and track growth."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.update_growth(1)

    def get_total_score(self) -> int:
        """
        Calculate total score based on plant heights.

        Returns:
            Sum of all plant heights in the garden.
        """
        return sum(plant.height for plant in self.plants)

    def generate_report(self) -> None:
        """Print comprehensive garden report with statistics."""
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            category = plant.plant_cat()
            if category in ["flowering", "prize"]:
                print(f"- {plant.info()}")
            else:
                print(f"- {plant.name}: {plant.height}cm")
        types = self.stats.plant_types
        print(
            f"Plants added: {self.stats.plants_added}, "
            f"Total growth: {self.stats.total_growth}cm"
        )

        print(
            f"Plant types: {types['regular']} regular, "
            f"{types['flowering']} flowering, "
            f"{types['prize']} prize flowers"
        )

    @classmethod
    def create_garden_network(cls, *names):
        """
        Create multiple gardens at once.

        Args:
            *names: Variable number of owner names.

        Returns:
            List of GardenManager instances.
        """
        return [cls(name) for name in names]

    @classmethod
    def get_total_gardens(cls) -> int:
        """
        Get total number of gardens created.

        Returns:
            Total gardens managed by the system.
        """
        return cls.total_gardens


print("=== Garden Management System Demo ===")


alice_garden, bob_garden = GardenManager.create_garden_network("Alice", "Bob")

oak = Plant("Oak Tree", 100)
rose = FloweringPlant("Rose", 25, "red")
sunflower = PrizeFlower("Sunflower", 50, "yellow")

print(alice_garden.add_plant(oak))
print(alice_garden.add_plant(rose))
print(alice_garden.add_plant(sunflower) + "\n")

bob_garden.add_plant(sunflower)

alice_garden.grow_all_plants()
print("\n")
alice_garden.generate_report()

print(
    f"Garden scores - Alice: {alice_garden.get_total_score()}, "
    f"Bob: {bob_garden.get_total_score()}"
)
print(f"Height validation test: {Plant.validate_height(oak.height)}")
print(f"\nTotal gardens managed: {GardenManager.get_total_gardens()}")
