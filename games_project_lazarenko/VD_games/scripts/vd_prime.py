from ..engine import run_game
from ..games.prime import generate_round


def main():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(type('GameModule', (), {'generate_round': generate_round}), description)


if __name__ == "__main__":
    main()
