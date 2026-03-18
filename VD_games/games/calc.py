"""Калькулятор"""
import random
import operator

DESCRIPTION = "What is the result of the expression?"

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_question_and_answer():
    """Возвращает вопрос и правильный ответ для игры"""
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op_symbol = random.choice(list(OPERATIONS.keys()))

    question = f"{num1} {op_symbol} {num2}"
    correct_answer = str(OPERATIONS[op_symbol](num1, num2))

    return question, correct_answer
