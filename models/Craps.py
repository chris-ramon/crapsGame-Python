import random

class Craps:
    '''Represent a dice with a 1 side for the game'''
    def __init__(self):
        self.side = random.randint(1,6)
