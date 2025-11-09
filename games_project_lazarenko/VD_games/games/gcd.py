import random
import math

def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = str(math.gcd(num1, num2))
    question = f"{num1} {num2}"
    return question, correct_answer
