### InputHandler class - Stores functions and variables to do with unit control through player input. Only a single instance of this class should ever exist.
#
#
# Potential future problems: Troops who die who are selected may still be selected (and possibly exist) until deselection.
#

import pygame
from building import Building
from economybuilding import EconomyBuilding
from defencebuilding import DefenceBuilding
from unitbuilding import UnitBuilding


class InputHandler():

    def __init__(self, grid,SCREEN,hud, unit_list, building_list,natural_building_list, enemy_list, projectile_list):
        self.selection = [] # Object storing all objects currently selected
        self.unit_list = unit_list
        self.building_list = building_list
        self.natural_building_list = natural_building_list
        self.projectile_list = projectile_list
        self.enemy_list = enemy_list
        self.SCREEN = SCREEN
        self.hud = hud
        self.grid = grid
        self.grid = None
        self.green_building = Building(self.grid,self.SCREEN,[],"temp",1000,"images/green_blueprint.png")
        self.red_building = Building(self.grid,self.SCREEN,[],"temp",1000,"images/red_blueprint.png")
        self.building = Building(self.grid,self.SCREEN,[],"debug",1000,"images/default2.png") 
        # This specific building should be replaced immediately but its just a placeholder

    def set_grid(self,grid):
        self.grid = grid

    def update(self):
        for entity in self.selection:
            x,y = entity.get_pos()
            pygame.draw.rect(self.SCREEN,(255,255,0),(x-4,y-4,40,40),2)
        if self.hud.get_is_building():
            pos_x, pos_y = pygame.mouse.get_pos()
            if pos_x < 864 and pos_y<576:
                if self.grid.get_grid(pos_x,pos_y).get_occupied():
                    self.red_building.set_pos(((pos_x//32)*32),((pos_y//32)*32))
                    self.red_building.update()
                else:
                    self.green_building.set_pos(((pos_x//32)*32),((pos_y//32)*32))
                    self.green_building.update()

        # Displays box around all selected things

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
        # checks the buildings.
        for building in self.building_list:
                if building.get_rect().collidepoint(pos_x,pos_y):
                    self.selection.append(building)
                    return
                
        # If the hud is building.
        if self.hud.get_is_building():
            if not(self.grid.get_grid(pos_x,pos_y).get_occupied()) and (self.hud.get_money()-self.hud.get_building_button().get_cost()>=0) :
                # Checks if the tile is occupied and that there is enough money to perform the transaction.
                exec_string = self.hud.get_building_string()
                exec("self.building ="+exec_string)
                self.building.set_pos((pos_x//32)*32,(pos_y//32)*32)
                self.grid.place_grid(self.building,[pos_x//32,pos_y//32])
                self.hud.set_is_building(False)
                self.hud.sub_money(self.hud.get_building_button().get_cost())


    def order(self,pos_x,pos_y):
        if self.hud.get_is_building():
            self.hud.set_is_building(False)
        is_attack = False
        for enemy in self.enemy_list:
            if enemy.get_rect().collidepoint(pos_x,pos_y):
                selected_enemy = enemy
                is_attack = True
                break
        
        if len(self.selection)>0:
            if isinstance(self.selection[0],Building): # There is only one selection and it is a building, otherwise all selected are units
                if is_attack: # Buildings can only be ordered to attack.
                    if isinstance(self.selection[0],DefenceBuilding):
                        if 'selected_enemy' in locals(): # If the variable is initialised in 
                            self.selection[0].attack(selected_enemy)
            else: #Selection is composed of units
                if is_attack:
                    for unit in self.selection:
                        unit.attack(enemy)
                else:
                    for unit in self.selection:
                        unit.move_to([pos_x,pos_y])

    def deselect(self):
        self.selection = []