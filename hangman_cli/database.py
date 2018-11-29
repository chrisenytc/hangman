# -*- coding: utf-8 -*-


class Database:

    def __init__(self):
        self.__game_level = None
        self.__chosen_word = ""
        self.__chosen_letter = ""
        self.__placeholders = []
        self.__hunches = []
        self.__round = 0
        self.__score = 0

    def get_level(self):
        return self.__game_level

    def set_level(self, l):
        self.__game_level = l

    def get_word(self):
        return self.__chosen_word

    def set_word(self, w):
        self.__chosen_word = w

    def get_letter(self):
        return self.__chosen_letter

    def set_letter(self, l):
        self.__chosen_letter = l

    def get_placeholders(self):
        return self.__placeholders

    def set_placeholders(self, ph):
        self.__placeholders = ph

    def put_placeholder(self, l):
        self.__placeholders.append(l)

    def update_placeholder(self, i, l):
        self.__placeholders[i] = l

    def get_hunches(self):
        return self.__hunches

    def set_hunches(self, h):
        self.__hunches = h

    def add_hunch(self, h):
        self.__hunches.append(h)

    def get_round(self):
        return self.__round

    def increase_round(self):
        self.__round += 1

    def get_score(self):
        return self.__score

    def set_score(self):
        self.__score = len(
            self.__chosen_word) if self.__score == 0 else self.__score

    def deduct_score(self):
        self.__score -= 1
