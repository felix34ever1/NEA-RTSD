### UnitButton class - subclass of Button stored in hud instance
#
#
#

import pygame
from button import Button


class UnitButton(Button):

    def __init__(self,SCREEN:pygame.Surface ,button_list: list,building_list:list, building_name: str,unit_list:str,unit_name:int, image: str="images/default.png", exec_string: str="",cost:int=1):
        super().__init__(SCREEN,button_list,image,exec_string,cost)
        self.building_list = building_list
        self.building_name = building_name
        self.building_position = [0,0]

    def is_available(self):
        for building in self.building_list:
            if building.get_name() == self.building_name:
                x,y = building.get_pos()
                self.building_position = [x,y]
                return(True)
        else:
            return(False)

    def on_press(self):
        # Figure out how to create unit on button press.
        pass

        