### Grid Class - Only one unique instance should exist
#
# 
#

import pygame
from tile import Tile
from building import Building
import random

class Grid():

    def __init__(self,SCREEN:pygame.Surface,grid_dimensions:list,building_list: list):
        self.SCREEN = SCREEN
        self.grid_dimensions = grid_dimensions
        self.tile_list = [] 
        self.building_constructor_list = [(SCREEN,building_list,health = 10000)]
        # List will be used to hold the tiles making up the world in a 2d list.

        for x in range(grid_dimensions[0]):
            self.tile_list.append([])
            for y in range(grid_dimensions[1]):
                self.tile_list[x].append(Tile([x,y]))

        for i in range(10):
            a = random.randint(0,26)
            b = random.randint(0,17)
            if not (self.tile_list[a][b].isoccupied()):
                # Add building to tile
                pass
