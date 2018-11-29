# -*- coding: utf-8 -*-

# Imports
from .helpers import print_line
from .helpers import clear_window
from .renderer import render_banner


def ask_the_level():
    return input("    Choose the level: ")


def ask_the_word():
    print("")
    print_line()
    print("")
    chosen_word = input(
        "    PLAYER 1> Choose a word with at least 7 letters: ").upper().strip()
    if len(chosen_word) < 7:
        clear_window()
        render_banner()
        print("")
        print_line()
        print("")
        print("    You need to write a word with at least 7 letters. Try again!")
        ask_the_word()
    return chosen_word


def ask_the_letter():
    print_line()
    print("")
    return input("    PLAYER 2> Enter a letter: ").upper().strip()


def ask_final_guess():
    print("")
    print_line()
    print("")
    return input("    PLAYER 2> What is the word? ").upper().strip()
