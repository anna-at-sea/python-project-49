#!/usr/bin/env python3


from brain_games.games import prime_game
from brain_games.games_logic import any_game


def main():
    any_game(prime_game.game_rules, prime_game.list_of_questions_and_answers)


if __name__ == '__main__':
    main()