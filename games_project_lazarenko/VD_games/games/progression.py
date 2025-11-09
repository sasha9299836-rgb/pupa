import random


def generate_round():
    """
    Генерирует вопрос и правильный ответ для игры "Арифметическая прогрессия"
    """
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    hidden_index = random.randint(0, length - 1)

    progression = []
    for i in range(length):
        progression.append(str(start + i * step))

    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(progression)

    return question, correct_answer
