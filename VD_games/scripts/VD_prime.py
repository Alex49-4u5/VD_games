#!/usr/bin/env python
"""Точка входа для игры"""
from VD_games.games import prime
from VD_games.games.engine import run_game


def main():
    run_game(prime)


if __name__ == "__main__":
    main()
