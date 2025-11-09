import random


def generate_round():
    number = random.randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    question = str(number)
    return question, correct_answer
