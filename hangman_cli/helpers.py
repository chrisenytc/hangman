# -*- coding: utf-8 -*-

# Imports
import os


def print_line():
    print("    ----------------------------------------------------------------------")


def print_message(message):
    print_line()
    print("")
    print("    %s" % message)
    print("")
    print_line()
    print("")


def clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')


def find_occurrences(string, character):
    return [i for i, letter in enumerate(string) if letter == character]
