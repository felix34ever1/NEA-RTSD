### UnitButton class - subclass of Button stored in hud instance
#
#
#

import pygame
from button import Button
from unit import Unit


class UnitButton(Button):

    def __init__(self,hud,grid,SCREEN:pygame.Surface ,unit_list,projectile_list,enemy_list,button_list: list,building_list:list, natural_building_list, building_name: str,unit_name:str, image: str="images/default.png", exec_string: str="",cost:int=1):
        super().__init__(hud,SCREEN,button_list,image,exec_string,cost)
        self.building_list = building_list
        self.grid = grid
        self.natural_building_list = natural_building_list
        self.building_name = building_name # Building that the button searches for to spawn units at
        self.building_position = [0,0] # Spawn point for unit
        self.unit_name = unit_name # Name of spawned unit
        self.unit_list = unit_list
        self.projectile_list = projectile_list
        self.enemy_list = enemy_list

    def is_available(self):
        for building in self.building_list:
            if building.get_name() == self.building_name:
                x,y = building.get_pos()
                self.building_position = [x,y]
                return(True)
        else:
            return(False)

    def get_unit_name(self):
        return(self.unit_name)

    def set_spawn_point(self,pos):
        self.building_position = [pos[0],pos[1]]

    def on_press(self):
        exec_string = self.exec_string+str(self.building_position)+")"
        print(exec_string)
        exec(exec_string)


        