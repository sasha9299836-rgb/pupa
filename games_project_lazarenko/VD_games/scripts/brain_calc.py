from ..engine import run_game
from ..games.calc import generate_round


def main():
    description = "What is the result of the expression?"
    run_game(type('GameModule', (), {'generate_round': generate_round}), description)

if __name__ == "__main__":
    main()
