
"""" This module generate the map and the characters /objects on the map """

# ! /usr/bin/env python3
# coding: utf-8


class Level:
    """ Class setting up the level map 20x20 cells, spawning the objects on
        random position and managing the movements of the player
        draw of the level is on level.txt file with following parameters:
        # = Wall
        - = Path
        * = Mini virus
        P = player position
        """

    def __init__(self):

        self.coord = {}
        self.path = []
        self.grid_gen()
        

    def grid_gen(self):
        """ Generate a virtual grid with map_x and map_y coordonates
            and stock them in a dictionary.
            isolate the coordonates of the paths
            """

        map_y, map_x = 0, 0
        with open("ressource/level.txt", "r") as file:
            for line in file:
                for element in line:
                    if element != '\n':
                        map_x = map_x + 1
                        self.coord[(map_y, map_x)] = element
                    if element == '-':
                        self.path.append((map_y, map_x))
                map_y, map_x = map_y + 1, 0


if __name__ == "__main__":

    level = Level()
    print(level.coord)
    print(level.path)
    
    
