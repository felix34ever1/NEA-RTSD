### Tile Class - All instances included in a Grid instance
#
#
#

import pygame
from building import Building

class Tile():

    def __init__(self, grid_coordinates:list):
        self.occupied = False
        self.occupier = None
        self.grid_coordinates = grid_coordinates
        self.movement_difficulty = 1

    # Getters & Setters

    def get_pos(self) -> list:
        return([self.grid_coordinates[0]*32,self.grid_coordinates[1]*32])

    def get_occupier(self) -> object:
        return(self.occupier)

    def get_occupied(self) -> bool:
        return(self.occupied)

    # Other subroutines

    def occupy(self, new_occupier: object=None):
        if self.occupier == None: # If it's empty before being assigned:
            if new_occupier == None:
                self.movement_difficulty = 1
                self.occupied = False
            else:
                self.movemment_difficulty = 50
                self.occupied = True
            self.occupier = new_occupier
        else: # if not empty already:
            self.occupier.on_death() # All buildings will have this method
            if new_occupier == None:
                self.movement_difficulty = 1
                self.occupied = False
            else:
                self.movemment_difficulty = 50
                self.occupied = True
            self.occupier = new_occupier            