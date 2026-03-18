#!/usr/bin/env python
"""Точка входа для игры"""
from VD_games.games import gcd
from VD_games.games.engine import run_game


def main():
    """Запускает игру"""
    run_game(gcd)


if __name__ == "__main__":
    main()
