import random


def generate_round():
    """
    Генерирует вопрос и правильный ответ для игры "Калькулятор"
    """
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        correct_answer = str(num1 + num2)
    elif operator == '-':
        correct_answer = str(num1 - num2)
    else:  # operator == '*'
        correct_answer = str(num1 * num2)

    question = f"{num1} {operator} {num2}"
    return question, correct_answer
