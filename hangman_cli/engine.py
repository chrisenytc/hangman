# -*- coding: utf-8 -*-

# Imports
from .database import Database
from .renderer import render_menu
from .helpers import clear_window
from .inquirer import ask_the_word
from .renderer import render_banner
from .inquirer import ask_the_level
from .inquirer import ask_the_letter
from .helpers import find_occurrences
from .renderer import render_game_over
from .renderer import render_scoreboard
from .renderer import render_placeholder
from .renderer import render_invalid_level

# Game levels
from .easy_level import check_round_state as easy_level_state_checker
from .easy_level import generate_placeholder as easy_level_placeholder
from .hard_level import check_round_state as hard_level_state_checker
from .hard_level import generate_placeholder as hard_level_placeholder

# Initialize database
database_client = Database()


def check_letter(hunches, word, letter):
    print("")
    if len(find_occurrences(hunches, letter)) >= 2:
        print("    >> The letter %s has already been used in a previous round." % letter)
    if letter not in word:
        print("    >> The letter %s is not part of the word!" % letter)


def update_score(db, word, letter):
    if db.get_score() < 1:
        return
    if letter not in word:
        db.deduct_score()


def start_round(db, already_started):
    if not already_started:
        # Set word
        db.set_word(ask_the_word())
        # Set score
        db.set_score()
    # Increase round every call
    if db.get_round() < len(db.get_word()):
        db.increase_round()
    # Render scoreboard
    render_scoreboard(db.get_level(), db.get_round(), db.get_score())
    # Render placeholder
    if db.get_level() == "1":
        render_placeholder(easy_level_placeholder(
            db, db.get_word(), db.get_letter()))
    else:
        render_placeholder(hard_level_placeholder(
            db, db.get_word(), db.get_letter()))
    # Check round state
    if db.get_level() == "1":
        easy_level_state_checker(db)
    else:
        hard_level_state_checker(db)
    # Check letter
    check_letter(db.get_hunches(), db.get_word(), db.get_letter())
    # Set letter
    db.set_letter(ask_the_letter())
    # Add letter to hunches
    db.add_hunch(db.get_letter())
    # Update score
    update_score(db, db.get_word(), db.get_letter())
    # Apply recursion
    start_round(db, True)


def start_game(show_banner):
    if show_banner:
        render_banner()
    render_menu()
    # Set the game level
    database_client.set_level(ask_the_level())
    # Game levels
    if database_client.get_level() == "1":
        clear_window()
        render_banner()
        start_round(database_client, False)
    elif database_client.get_level() == "2":
        clear_window()
        render_banner()
        start_round(database_client, False)
    else:
        clear_window()
        render_banner()
        render_invalid_level()
        start_game(False)
