def water_plants(plant_list):
    """
    Water a list of plants using the watering system.

    Args:
        plant_list: List of plant names (strings) to water.

    Returns:
        None: Function prints status messages instead of returning.
    """
    print("Opening watering system")
    success = True
    try:
        for plant in plant_list:
            if type(plant) is not str:
                raise ValueError("Error: Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as er:
        print(er)
        success = False
    finally:
        print("Closing watering system (cleanup)")

    if success:
        print("Watering completed successfully!")


def test_watering_system():
    """
    Test the watering system with valid and invalid inputs.

    Demonstrates normal operation and error handling with cleanup.
    """
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")

    valid = ["tomato", "lettuce", "carrots"]
    water_plants(valid)

    print("\nTesting with error...")

    valid = ["tomato", None, "carrots"]
    water_plants(valid)

    print("\nCleanup always happens, even with errors!")


test_watering_system()
