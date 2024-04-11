"""Word Finder: finds random words from a dictionary."""

import random

"""Finds a random word from a list of words"""


class WordFinder:

    def __init__(self, fname):
        """Opens and reads the file"""
        with open(fname) as file:
            self.list = file.readlines()

    def random(self):
        """Returns random word"""
        rand_word = [word.strip() for word in self.list]
        return random.choice(rand_word)


"""Finds a random word from a list a words while avoiding words starting with the special character ('#')"""


class SpecialWordFinder(WordFinder):

    def random(self):
        """Returns random word without starting '#'"""
        rand_word = [
            word.strip()
            for word in self.list
            if word.strip() and not word.startswith("#")
        ]

        return random.choice(rand_word)
