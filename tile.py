### Tile Class - All instances included in a Grid instance
#
#
#

import pygame


class Tile():

    def __init__(self, grid_coordinates:list):
        self.occupied = False
        self.occupier = None
        self.grid_coordinates = grid_coordinates
        self.movement_difficulty = 1

    def occupy(self, occupier: object=None):
        if occupier == None:
            self.movement_difficulty = 1
            self.occupied = False
        else:
            self.movemment_difficulty = 50
            self.occupied = True
        self.occupier = occupier
    
    def get_pos(self) -> list:
        return([self.grid_coordinates[0]*32,self.grid_coordinates[1]*32])

    def get_occupier(self) -> object:
        return(self.occupier)