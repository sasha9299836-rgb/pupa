from ..engine import run_game
from ..games.progression import generate_round


def main():
    description = 'What number is missing in the progression?'
    run_game(type('GameModule', (), {'generate_round': generate_round}), description)


if __name__ == "__main__":
    main()
