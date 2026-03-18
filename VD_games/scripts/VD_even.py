#!/usr/bin/env python
"""Проверка на чётность"""
import random
from VD_games.cli import welcome_user


def is_even(number):
    """Является ли число чётным"""
    return number % 2 == 0


def play_game():
    """Основная логика игры"""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    rounds_to_win = 3

    while correct_answers < rounds_to_win:
        number = random.randint(1, 100)
        print(f"Question: {number}")

        answer = input("Your answer: ").strip().lower()
        correct_answer = "yes" if is_even(number) else "no"

        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    """Точка входа"""
    print("Welcome to the VD-games!")
    play_game()


if __name__ == "__main__":
    main()
