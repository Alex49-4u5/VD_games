"""Арифметическая прогрессия"""
import random

DESCRIPTION = "What number is missing in the progression?"


def get_question_and_answer():
    start = random.randint(1, 10)
    step = random.randint(2, 5)
    length = random.randint(5, 10)
    hidden_position = random.randint(0, length - 1)

    progression = []
    for i in range(length):
        progression.append(str(start + i * step))

    correct_answer = progression[hidden_position]
    progression[hidden_position] = ".."
    question = " ".join(progression)

    return question, correct_answer
