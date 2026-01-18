def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Validate plant health parameters.

    Args:
        plant_name: Name of the plant to check.
        water_level: Current water level (valid range: 1-10).
        sunlight_hours: Current sunlight hours (valid range: 2-12).

    Raises:
        ValueError: If any parameter is outside valid range.
    """
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")

    if water_level > 10:
        raise ValueError(
            f"Error: Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError(
            f"Error: Water level {water_level} is too low (min 1)")

    if sunlight_hours < 2:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")

    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    """
    Test plant health validation with various inputs.

    Tests good values, empty name, invalid water level,
    and invalid sunlight hours. Catches and prints errors.
    """
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        check_plant_health("tomato", 2, 4)
    except ValueError as err:
        print(err)

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 2, 4)
    except ValueError as err:
        print(err)

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 4)
    except ValueError as err:
        print(err)

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as err:
        print(err)

    print("\nAll error raising tests completed!")


test_plant_checks()
