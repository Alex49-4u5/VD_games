"""Модуль для интeрфейса командной строки игры"""
import prompt


def welcome_user():
    """Функция приветствия пользователя"""
    print("Welcome to the VD-games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


if __name__ == "__main__":
    welcome_user()
