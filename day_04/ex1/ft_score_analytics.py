"""
This program analyzes player scores from command line arguments.
It calculates stats like total, average, high score, and low score.
"""
import sys


def help() -> str:
    """
    Returns help message when no scores are given.
    """
    return (
        "No scores provided. Usage: "
        "python3 ft_score_analytics.py <score1> <score2> ..."
    )


def main() -> None:
    """
    Main function that processes scores and shows statistics.
    """
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print(help())
        return

    scores = []
    invalid_inputs = []

    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            invalid_inputs.append(arg)

    if invalid_inputs:
        for invalid in invalid_inputs:
            print(f"oops, I typed '{invalid}' instead of a valid number")
            return

    if scores:
        print("Scores processed:", scores)
        print("Total players:", len(scores))
        print("Total score:", sum(scores))
        print("Average score:", sum(scores) / len(scores))
        print("High score:", max(scores))
        print("Low score:", min(scores))
        print("Score range:", max(scores) - min(scores))


main()
