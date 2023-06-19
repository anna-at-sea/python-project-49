#!/usr/bin/env python3


from brain_games.games import progression_game
from brain_games.games_logic import any_game


rules = progression_game.game_rules
q_a = progression_game.question_and_answer


def main():
    any_game(rules, q_a)


if __name__ == '__main__':
    main()
