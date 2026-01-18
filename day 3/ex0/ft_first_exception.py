def check_temperature(temp_str: str) -> str:
    """
    Validates a temperature value for plants.

    Args:
        temp_str (str): A string representation of a temperature value.

    Returns:
        str: Message indicating if temperature is valid, too hot, or too cold.
        Returns an error message if the input is not a valid number.
    """
    try:
        temp_int = int(temp_str)
    except BaseException:
        return f"Error: '{temp_str}' is not a valid number"
    if temp_int > 40:
        return f"Error: {temp_int}°C is too hot for plants (max 40°C)"
    elif temp_int < 0:
        return f"Error: {temp_int}°C is too cold for plants (min 0°C)"
    return f"Temperature {temp_int}°C is perfect for plants!"


def test_temperature_input() -> None:
    """
    Tests the temperature checking functionality with user input.

    Prompts the user to input 4 temperature values for testing.
    Prints the result of each temperature check.
    """
    print("=== Garden Temperature Checker ===\n")
    for i in range(1, 5):
        str = input("Testing temperature: ")
        print(check_temperature(str) + '\n')
    print("All tests completed - program didn't crash!")


test_temperature_input()
