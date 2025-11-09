import random


def is_prime(number):
    """Проверяет, является ли число простым"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    """
    Генерирует вопрос и правильный ответ для игры "Простое ли число?"
    """
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    question = str(number)
    return question, correct_answer
