### BuildingButton Class - Subclass of Button
# 
# 
#

import pygame
from button import Button


class BuildingButton(Button):

    def __init__(self,SCREEN:pygame.Surface ,button_list: list, building_list,unit:object=None,  image: str="images/default.png", exec_string:str="",cost:int=1):
        super().__init__(SCREEN,button_list,image,exec_string,cost)
        self.building_list = building_list
    
    def is_available(self):
        return(True) # Building buttons should always be visible
        
    def on_press(self):
        pass