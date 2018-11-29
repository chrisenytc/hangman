# -*- coding: utf-8 -*-

# Imports
from .helpers import find_occurrences
from .renderer import render_game_over


def generate_placeholder(db, word, letter):
    placeholder = ""
    for index in range(0, len(word)):
        placeholder = placeholder + "__ "
    if len(db.get_placeholders()) == 0:
        db.set_placeholders(placeholder.split())
    occurrences = find_occurrences(word, letter)
    for index in occurrences:
        db.update_placeholder(index, letter)
    return " ".join(db.get_placeholders())


def check_round_state(db):
    if db.get_score() == 0:
        render_game_over(1, db.get_word())
        exit(0)
    if db.get_word() == "".join(db.get_placeholders()):
        render_game_over(2, db.get_word())
        exit(0)
