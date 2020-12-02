""" This module generate the scientist"""

# ! /usr/bin/env python3
# coding: utf-8


class Player:
    """Class setting up the main human player """

    def __init__(self, name, coo_y, coo_x):
        self.player = name
        self.life = 100
        self.inventory = []
        self.coo_x = coo_x
        self.coo_y = coo_y
        self.new_coo = ()

    def moove(self, direction):

        if direction == "right":
            self.new_coo = (self.coo_y, self.coo_x+1)
        elif direction == "left":
            self.new_coo = (self.coo_y, self.coo_x-1)
        elif direction == "up":
            self.new_coo = (self.coo_y-1, self.coo_x)
        elif direction == "down":
            self.new_coo = (self.coo_y+1, self.coo_x)


