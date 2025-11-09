from ..engine import run_game
from ..games.gcd import generate_round

def main():
    description = "Find the greatest common divisor of given numbers."
    run_game(type('GameModule', (), {'generate_round': generate_round}), description)

if __name__ == "__main__":
    main()
