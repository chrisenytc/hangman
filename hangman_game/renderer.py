# -*- coding: utf-8 -*-

# System Imports
import os

# Imports
from .helpers import print_line
from .helpers import clear_window


def render_banner():
    with open("%s/assets/banner.txt" % os.getcwd(), "r") as fh:
        banner = fh.read()
    print("")
    print("")
    print(banner)
    print("")
    print("")


def render_menu():
    print("    LEVEL OF THE GAME")
    print_line()
    print("")
    print("    1- Easy")
    print("    2- Hard")
    print("")
    print_line()
    print("")


def render_invalid_level():
    print_line()
    print("    Invalid option. Try again!")
    print_line()
    print("")
    print("")


def render_scoreboard(level, player_round, player_score):
    clear_window()
    render_banner()
    print("")
    print_line()
    print("")
    print("    Level: %s" % ("Easy" if level == "1" else "Hard"))
    print("    Round: %s" % (player_round))
    print("    Points Remaining: %s" % player_score)
    print("")
    print_line()


def render_placeholder(placeholder):
    print("")
    print("    Word: %s" % placeholder)


def render_hard_win_message(word):
    print("")
    print_line()
    print("")
    print("    >> THE PLAYER 2 GUESSED ALL THE LETTERS: %s" %
          ("".join(sorted(word))))


def render_game_over(player, word):
    if player == 1:
        print("")
        print_line()
        print("")
        print("    >> THE PLAYER 1 IS THE WINNER \O/")
        print("")
        print("    >> The word was: %s" % word)
        print("")
        print("    ## GAME OVER ##")
        print("")
    if player == 2:
        print("")
        print_line()
        print("")
        print("    >> THE PLAYER 2 IS THE WINNER \O/")
        print("")
        print("    ## GAME OVER ##")
        print("")
