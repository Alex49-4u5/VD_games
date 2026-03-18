"""НОД"""
import random
import math

DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_question_and_answer():
    """Возвращает вопрос и правильный ответ"""
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)

    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))

    return question, correct_answer
