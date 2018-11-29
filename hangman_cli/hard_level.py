# -*- coding: utf-8 -*-

# Imports
from .helpers import find_occurrences
from .inquirer import ask_final_guess
from .renderer import render_game_over
from .renderer import render_hard_win_message


def generate_placeholder(db, word, letter):
    occurrences = find_occurrences(word, letter)
    for _ in occurrences:
        db.put_placeholder(letter)
        db.set_placeholders(sorted(db.get_placeholders()))
    return "".join(db.get_placeholders())


def check_round_state(db):
    if db.get_score() == 0:
        render_game_over(1, db.get_word())
        exit(0)
    if sorted(db.get_word()) == db.get_placeholders():
        render_hard_win_message(db.get_word())
        final_guess = ask_final_guess()
        if final_guess == db.get_word():
            render_game_over(2, db.get_word())
            exit(0)
        else:
            render_game_over(1, db.get_word())
            exit(0)
