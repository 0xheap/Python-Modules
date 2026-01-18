data = {
    "players": {
        "alice": {
            "level": 41,
            "total_score": 2824,
            "sessions_played": 13,
            "favorite_mode": "ranked",
            "achievements_count": 5,
        },
        "bob": {
            "level": 16,
            "total_score": 4657,
            "sessions_played": 27,
            "favorite_mode": "ranked",
            "achievements_count": 2,
        },
        "charlie": {
            "level": 44,
            "total_score": 9935,
            "sessions_played": 21,
            "favorite_mode": "ranked",
            "achievements_count": 7,
        },
    },
    "sessions": [
        {
            "player": "alice",
            "duration_minutes": 94,
            "region": "north",
            "score": 1831,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 32,
            "region": "central",
            "score": 1478,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 17,
            "score": 1570,
            "region": "east",
            "mode": "competitive",
            "completed": False,
        },
    ],
    "game_modes": ["casual", "competitive", "ranked"],
    "achievements": [
        "first_blood",
        "level_master",
        "speed_runner",
        "treasure_seeker",
        "boss_hunter",
        "pixel_perfect",
        "combo_king",
        "explorer",
    ],
}


def main() -> None:
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")

    high = []
    scores = []
    player_score = {}
    for key, value in data["players"].items():
        if value.get("total_score") > 2000:
            high.append(key)
        scores.append(value.get("total_score") * 2)
        player_score.update({key: value.get("total_score")})

    print("High scorers (>2000):", high)
    print("Scores doubled:", scores)

    active = []
    for dic in data["sessions"]:
        active.append(dic.get("player"))
    print("Active players:", active)

    print("\n=== Dict Comprehension Examples ===")
    print("Player scores:", player_score)

    categories = {"high": 0, "meduim": 0, "low": 0}
    for key, value in data["players"].items():
        if value.get("total_score") > 2000:
            categories["high"] += 1
        elif value.get("total_score") > 1000:
            categories["meduim"] += 1
        else:
            categories["low"] += 1
    print("Score categories: ", categories)

    achievement = {}
    for key, value in data["players"].items():
        achievement.update({key: value.get("achievements_count")})
    print("Achievement counts:", achievement)

    print("\n=== Set Comprehension Examples ===")

    unique_players = set(data["players"].keys())
    print("Unique players:", unique_players)

    unique_achievements = set(data["achievements"])
    print("Unique achievements:", unique_achievements)

    unique_region = set()
    # list -> dict -> region as a key
    for dict in data["sessions"]:
        unique_region.update({dict.get("region")})
    print("Active regions: ", unique_region)

    print("\n=== Combined Analysis ===")
    print("Total players:", len(unique_players))
    print("Total unique achievements:", len(unique_achievements))
    # {data} -> {players} -> {name: var} -> 'total_score' -> value
    total = sum(player["total_score"] for player in data["players"].values())
    average = total / len(unique_players)
    print(f"Average score: {average:.1f}")
    top_player = max(player_score, key=player_score.get)
    top_score = player_score[top_player]
    top_achievements = achievement[top_player]
    print(
        f"Top performer: {top_player} with {top_score} points, {top_achievements} achievements"
    )
    return


main()
