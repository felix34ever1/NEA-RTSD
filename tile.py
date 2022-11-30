### Tile Class - All instances included in a Grid instance
#
#
#

import pygame
from building import Building
from unitbuilding import UnitBuilding

class Tile():

    def __init__(self,grid , grid_coordinates:list,grid_size:list):
        self.occupied = False
        self.occupier = None
        self.grid = grid
        self.grid_coordinates = grid_coordinates
        self.movement_difficulty = 1
        self.row = grid_coordinates[1]//32
        self.column = grid_coordinates[0]//32
        self.total_rows, self.total_columns = grid_size

    # Getters & Setters

    def get_pos(self) -> list:
        return([self.grid_coordinates[0]*32,self.grid_coordinates[1]*32])

    def get_occupier(self) -> object:
        return(self.occupier)

    def get_occupied(self) -> bool:
        return(self.occupied)

    def get_difficulty(self) -> int:
        return(self.movement_difficulty)

    # Other subroutines
    def update_neighbours(self, grid):
        self.neighbours = []
        if (
            self.row < self.total_rows - 1
            and not grid[self.row + 1][self.column].get_difficulty() > 1
        ):  # DOWN
            self.neighbours.append(grid[self.row + 1][self.column])

        if self.row > 0 and not grid[self.row - 1][self.column].get_difficulty() > 1:  # UP
            self.neighbours.append(grid[self.row - 1][self.column])

        if (
            self.column < self.total_rows - 1
            and not grid[self.row][self.column + 1].get_difficulty() > 1
        ):  # RIGHT
            self.neighbours.append(grid[self.row][self.column + 1])

        if self.column > 0 and not grid[self.row][self.column - 1].get_difficulty() > 1:  # LEFT
            self.neighbours.append(grid[self.row][self.column - 1])



    def occupy(self, new_occupier: object=None):
        if self.occupier == None: # If it's empty before being assigned:
            if new_occupier == None:
                self.movement_difficulty = 1
                self.occupied = False
            else:
                if isinstance(new_occupier,UnitBuilding):
                    self.movemment_difficulty = 1
                else:
                    self.movement_difficulty = 50
                self.occupied = True
            self.occupier = new_occupier
        else: # if not empty already:
            if new_occupier == None:
                self.movement_difficulty = 1
                self.occupied = False
            else:
                if isinstance(new_occupier,UnitBuilding):
                    self.movemment_difficulty = 1
                else:
                    self.movement_difficulty = 50
                self.occupied = True
            self.occupier = new_occupier            