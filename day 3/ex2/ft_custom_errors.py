class GardenError(Exception):
    """Base exception for garden-related errors."""
    ...


class PlantError(GardenError):
    """Exception raised for plant-related issues."""
    ...


class WaterError(GardenError):
    """Exception raised for water-related issues."""
    ...


def ft_custom_errors():
    """
    Test custom exception handling for garden operations.

    Demonstrates raising and catching PlantError, WaterError,
    and the base GardenError exception.
    """
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!\n")
    except PlantError as e:
        print("Caught PlantError:", e)

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!\n")
    except WaterError as e:
        print("Caught WaterError:", e)

    print("Testing catching all garden errors...")
    for error_type in [PlantError, WaterError]:
        try:
            if error_type == WaterError:
                raise WaterError("Not enough water in the tank!")
            else:
                raise PlantError("The tomato plant is wilting!")
        except GardenError as e:
            print("Caught a garden error:", e)

    print("\nAll custom error types work correctly!")


ft_custom_errors()
