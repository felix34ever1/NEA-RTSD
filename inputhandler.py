### InputHandler class - Stores functions and variables to do with unit control through player input. Only a single instance of this class should ever exist.
#
#
# Potential future problems: Troops who die who are selected may still be selected (and possibly exist) until deselection.
#

import pygame


class InputHandler():

    def __init__(self, unit_list, building_list, enemy_list):
        self.selection = [] # Object storing all objects currently selected
        self.unit_list = unit_list
        self.building_list = building_list
        self.enemy_list = enemy_list


    def update(self):
        pass 
        # Possibly display all selected units with a box around them?

    def box_select(self,pos_x,pos_y,next_pos_x,next_pos_y): # Selects all units in a rectangle shaped area defined by two coordinates. Buildings don't get selected like this. 
        self.selection = [] # Clears the selection first
        for unit in self.unit_list:
            x,y = unit.get_pos()[0],unit.get_pos()[1]
            if ((x > pos_x and x < next_pos_x) or (x < pos_x and x > next_pos_x)):
                if ((y > pos_y and y < next_pos_y) or (y < pos_y and y > next_pos_y)):
                    self.selection.append(unit)

    def select(self,pos_x,pos_y):
        self.selection = [] #Clears the selection first
        for unit in self.unit_list: #Checks units before buildings.
            if unit.get_rect().collidepoint(pos_x,pos_y):
                self.selection.append(unit)
                return
        for building in self.building_list:
            if building.get_rect().collidepoint(pos_x,pos_y):
                self.selection.append(building)
                return

    def order(self,pos_x,pos_y):
        is_attack = False
        for enemy in self.enemy_list():
            if enemy.get_rect().collidepoint(pos_x,pos_y):
                is_attack = True
                break

        if self.selection[0].isinstance(Building): # There is only one selection and it is a building, otherwise all selected are units
            if is_attack: # Buildings can only be ordered to attack.
                if self.selection[0].isinstance(DefenceBuilding):
                    self.selection[0].attack(enemy)
        else: #Selection is composed of units
            if is_attack:
                for unit in self.unit_list:
                    unit.attack(enemy):
            else:
                for unit in self.unit_list:
                    unit.move_to(pos_x,pos_y)
    
    def deselect(self):
        self.selection = []