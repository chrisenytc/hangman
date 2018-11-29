# -*- coding: utf-8 -*-

# Imports
from .engine import start_game
from .helpers import print_message

# Start the game
try:
    start_game(True)
# Catch exceptions
except Exception as e:
    print_message("An error has occurred during the game: %s" % e)
except KeyboardInterrupt:
    print("")
    print("\n    Game closed. See you later :)")
    print("")
    exit(0)
