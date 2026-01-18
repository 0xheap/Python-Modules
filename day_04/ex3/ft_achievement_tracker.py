"""
This program tracks player achievements in a game.
It analyzes which achievements are common, rare, or unique to each player.
"""

data = {
    "alice": [
        "first_blood",
        "pixel_perfect",
        "speed_runner",
        "first_blood",
        "treasure_seeker",
        "first_blood",
    ],
    "bob": [
        "level_master",
        "boss_hunter",
        "treasure_seeker",
        "level_master",
        "level_master",
    ],
    "charlie": [
        "treasure_seeker",
        "boss_hunter",
        "combo_king",
        "first_blood",
        "boss_hunter",
        "first_blood",
        "boss_hunter",
        "first_blood",
    ],
}


def two() -> list:
    """
    Returns the first two player names from the data.
    """
    elements = []
    i = 0
    for key in data.keys():
        elements.append(key) if i != 2 else ...
        i += 1
    return elements


def main() -> None:
    """
    Main function that analyzes player achievements using sets.
    """
    print("=== Achievement Tracker System ===\n")
    for key, value in data.items():
        print(f"Player {key} achievements:", set(value))

    users = two()
    print("\n=== Achievement Analytics ===")
    unique = set()

    for value in data.values():
        unique = unique.union(value)
    print("All unique achievements:", unique)
    print(f"Total unique achievements: {len(unique)}")

    common = set(data[users[0]])

    for value in data.values():
        common = common.intersection(value)
    print("\nCommon to all players:", common)

    meme = set()
    players_wit_rare = 0

    for key, achievements in data.items():
        rare = set(achievements)

        for user, value in data.items():
            if key == user:
                continue
            rare = rare.difference(value)
        if rare:
            players_wit_rare += 1
            meme.update(rare)

    print(f"Rare achievements ({players_wit_rare} player): ", meme, "\n")

    print(f"{users[0]} vs {users[1]} common: ", end="")
    common = set(data[users[0]])
    common = common.intersection(set(data[users[1]]))
    print(common)

    print(f"{users[0]} unique: ",
          set(data[users[0]]).difference(set(data[users[1]])))

    print(f"{users[1]} unique: ",
          set(data[users[1]]).difference(set(data[users[0]])))
    return


main()
