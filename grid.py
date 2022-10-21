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
        building_constructor_list = ['SCREEN,building_list,"Terrain",10000,"images/boulder_0.png"','SCREEN,building_list,"Terrain",10000,"images/boulder_1.png"','SCREEN,building_list,"Terrain",10000,"images/boulder_2.png"','SCREEN,building_list,"Terrain",10000,"images/old_tower_0.png"','SCREEN,building_list,"Terrain",10000,"images/old_tower_1.png"']
        # List will be used to hold the tiles making up the world in a 2d list.

        for x in range(grid_dimensions[0]):
            self.tile_list.append([])
            for y in range(grid_dimensions[1]):
                self.tile_list[x].append(Tile([x,y]))

        for i in range(450):
            a = random.randint(0,26)
            b = random.randint(0,17)
            if not(self.tile_list[a][b].get_occupied()):
                # Add building to tile
                c = random.randint(0,len(building_constructor_list)-1)
                exec(f"self.tile_list[{a}][{b}].occupy(Building({building_constructor_list[c]},[{a*32},{b*32}]))")
                # Above code evaluates at run time allowing for the building attributes to be dynamically edited.
