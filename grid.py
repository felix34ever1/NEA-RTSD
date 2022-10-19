### Grid Class - Only one unique instance should exist
#
# 
#

import pygame
from tile import Tile


class Grid():

    def __init__(self,SCREEN:pygame.Surface,grid_dimensions:list):
        self.SCREEN = SCREEN
        self.grid_dimensions = grid_dimensions
        self.tile_list = [] 
        # List will be used to hold the tiles making up the world in a 2d list.

        for x in range(grid_dimensions[0]):
            self.tile_list.append([])
            for y in range(grid_dimensions[1]):
                self.tile_list[x].append(Tile([x,y]))