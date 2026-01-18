"""
This program works with 3D coordinates in a game.
It calculates distances between points and shows how to parse coordinates.
"""
import math
import sys


def parse_coords(s: str) -> tuple:
    """
    Takes a string like "1,2,3" and turns it into coordinates (1, 2, 3).
    """
    parts = s.split(",")
    return (int(parts[0]), int(parts[1]), int(parts[2]))


def distance(p1: tuple, p2: tuple) -> float:
    """
    Calculates the distance between two 3D points.
    """
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2)


def main():
    """
    Main function that demonstrates coordinate parsing and distance calculation.
    """
    print("=== Game Coordinate System ===")
    origin = (0, 0, 0)
    default = [(10, 20, 5), (30, -42, 85)]
    
    for value in default :
        dist = distance(origin, value)
        print("Position created: ", value)
        print(f"Distance between {origin} and {value}: {dist:.2f}" + "\n")

    if len(sys.argv) > 1:
        coord_str = sys.argv[1]
    else:
        coord_str = "3,4,0"

    try:
        print(f'Parsing coordinates: "{coord_str}"')
        pos = parse_coords(coord_str)
        print(f"Parsed position: {pos}")
        dist = distance(origin, pos)
        print(f"Distance between {origin} and {pos}: {dist:.1f}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
        return

    try:
        print('\nParsing invalid coordinates: "abc,def,ghi"')
        parse_coords("abc,def,ghi")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")

    print("\n" + "Unpacking demonstration:")
    x, y, z = pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


main()
