""" this module runs the algorithme of the game """

# ! /usr/bin/env python3
# coding: utf-8

from player import Player
from level import Level

class Algorithme:
    "this class run de algoritme of the game"

    def __init__(self):
        
        self.player = None
        self.level = Level()

    def spawn_elements(self):

        for key, val in self.level.coord.items():
            if val == "P":
                self.player = Player("scientist", key[0], key[1])

    def control_pos(self):

        if self.player.new_coo in self.level.coord:
            new_cell_content = self.level.coord[self.player.new_coo]

            if new_cell_content == '-':
                self.level.coord[(self.player.coo_y, self.player.coo_x)] = "-"
                self.level.coord[self.player.new_coo] = 'M'
                self.player.coo_y = self.player.new_coo[0]
                self.player.coo_x = self.player.new_coo[1]
                
    def print_grid(self):  # print la grille self.level.coord de manière représentative sur 20x20

        count = 0
        for val in self.level.coord.values():
            print(val, end='')  # end = '' permet de print sur une seule ligne
            count = count + 1
            if count % 20 == 0:
                print("\n")
        
if __name__ == "__main__":
    algo = Algorithme()
    print(algo.print_grid())
    print(algo.player.moove("right"))
