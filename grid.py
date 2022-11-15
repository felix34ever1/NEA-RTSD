### Grid Class - Only one unique instance should exist
#
# 
#

import math
import pygame
from tile import Tile
from building import Building
import random

class Grid():

    def __init__(self,SCREEN:pygame.Surface,grid_dimensions:list,building_list: list):
        self.SCREEN = SCREEN
        self.grid_dimensions = grid_dimensions
        self.tile_list = [] 
        building_constructor_list = ['SCREEN,building_list,"Terrain",10000,"images/boulder_0.png"',
        'SCREEN,building_list,"Terrain",10000,"images/boulder_1.png"',
        'SCREEN,building_list,"Terrain",10000,"images/boulder_2.png"',
        'SCREEN,building_list,"Terrain",10000,"images/old_tower_0.png"',
        'SCREEN,building_list,"Terrain",10000,"images/old_tower_1.png"',
        'SCREEN,building_list,"Terrain",10000,"images/rubble_0.png"',
        'SCREEN,building_list,"Terrain",10000,"images/rubble_1.png"',
        'SCREEN,building_list,"Terrain",10000,"images/rubble_2.png"']
        # List will be used to hold the tiles making up the world in a 2d list.
        economy_constructor_list = ['SCREEN,building_list,"Mine",10000,"images/mine_0.png"','SCREEN,building_list,"Mine",10000,"images/mine_1.png"']

        for x in range(grid_dimensions[0]):
            self.tile_list.append([])
            for y in range(grid_dimensions[1]):
                self.tile_list[x].append(Tile([x,y]))

        # Generate mines
        counter = 0
        while counter!=2:
            a = random.randint(6,21)
            b = random.randint(4,15)
            if not(self.tile_list[a][b].get_occupied()):
                counter+=1
                # Add building to tile
                c = random.randint(0,len(economy_constructor_list)-1)
                exec(f"self.tile_list[{a}][{b}].occupy(Building({economy_constructor_list[c]},[{a*32},{b*32}]))")
                # Above code evaluates at run time allowing for the building attributes to be dynamically edited.

            
        # Generate terrain blockers
        for i in range(random.randint(20,60)):
            a = random.randint(0,26)
            b = random.randint(0,17)
            if not(self.tile_list[a][b].get_occupied()):
                # Add building to tile
                c = random.randint(0,len(building_constructor_list)-1)
                exec(f"self.tile_list[{a}][{b}].occupy(Building({building_constructor_list[c]},[{a*32},{b*32}]))")
                # Above code evaluates at run time allowing for the building attributes to be dynamically edited.

    # Getters and Setters

    def get_tile_list(self)->list:
        return self.tile_list

    # Other subroutines

    def place_grid(self,item:object,pos:list=[0,0]):
        self.tile_list[pos[0]][pos[1]].occupy(item)

    def place_pixel(self,item:object,pos:list=[0,0]):
        pos = [pos[0]//32,pos[1]//32]
        self.tile_list[pos[0]][pos[1]].occupy(item)

    def get_grid(self,pos_x,pos_y)->None:
        return self.tile_list[pos_x//32][pos_y//32]
