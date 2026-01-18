def garden_operations():
    """
    Trigger different errors based on `kind`.

    Tests and demonstrates handling of various exception types:
    ValueError, ZeroDivisionError, FileNotFoundError, and KeyError.
    """
    print("\nTesting ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        res = 10
        res /= 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("\nTesting FileNotFoundError...")
    try:
        open("missing.txt", "r")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("\nTesting KeyError...")
    try:
        plants = {"rose": 5, "sunflower": 20}
        print(plants["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing_\\plant'")

    print("\nTesting multiple errors together...")
    multiple_errs = [ZeroDivisionError, ValueError]
    for error in multiple_errs:

        try:
            if error is ZeroDivisionError:
                res = 2004
                res /= 0
            else:
                res = int("1df2")
        except (ZeroDivisionError, ValueError):
            print("Caught an error, but program continues!")
            break


def test_error_types():
    """
    Run the garden operations error demo.

    Prints a header, executes the error handling demonstrations,
    and prints a completion message.
    """
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")


test_error_types()
