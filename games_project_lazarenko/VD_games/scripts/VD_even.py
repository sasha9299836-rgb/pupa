from ..engine import run_game
from ..games.even import generate_round


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(type('GameModule', (), {'generate_round': generate_round}), description)


if __name__ == "__main__":
    main()
