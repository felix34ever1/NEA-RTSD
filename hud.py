# Hud Class - Holds the buttons and draws the side menus. Only one instance of this class should ever exist.
# 
#  
#

import pygame

from buildingbutton import BuildingButton
from unitbutton import UnitButton
from button import Button

class Hud():

    def __init__(self, building_list: list, natural_building_list: list, SCREEN: pygame.Surface):
        
        self.building_list = building_list
        self.natural_building_list = natural_building_list
        self.SCREEN = SCREEN
        self.buttons_list = []
        self.buttons_list = [BuildingButton(self.SCREEN,self.buttons_list,self.building_list),BuildingButton(self.SCREEN,self.buttons_list,self.building_list),BuildingButton(self.SCREEN,self.buttons_list,self.building_list)] # Buttons to be manually created
        self.state = 0
        self.change_button_0 = Button(SCREEN,self.buttons_list,"images/building_menu.png","",0)
        self.change_button_0.set_pos(864,50)
        self.change_button_1 = Button(SCREEN,self.buttons_list,"images/unit_menu.png","",0)
        self.change_button_1.set_pos(932,50)



        unit_counter = 1
        building_counter = 1
        for button in self.buttons_list: # Assigns all buttons correct position on the hud.
            if isinstance(button,UnitButton):
                if unit_counter%2 == 0:
                    posx = 944
                else:
                    posx = 888
                posy = 100 + 40*(unit_counter//2)
                unit_counter+=1
                button.set_pos(posx,posy)
            else:
                if building_counter%2 == 0:
                    posx = 944
                else:
                    posx = 888
                posy = 100 + 100*((building_counter-1)//2)
                building_counter+=1
                button.set_pos(posx,posy)

    #Getters & Setters

    def get_buttons_list(self) -> list:
        return self.buttons_list

    # Other subroutines

    def on_press(self,mouse_x: int,mouse_y: int) -> None:

        for button in self.buttons_list:
            if button.get_rect().collidepoint(mouse_x,mouse_y) and button.is_available():
                pygame.draw.rect(self.SCREEN,(0,255,0),(button.get_pos()[0]-4,button.get_pos()[1]-4,40,40),0) 
                # Gets covered up by the update so will have to find workaround if I care enough
                button.on_press()
                break

        if self.change_button_0.get_rect().collidepoint(mouse_x,mouse_y):
            self.change_state(0)
        if self.change_button_1.get_rect().collidepoint(mouse_x,mouse_y):
            self.change_state(1)

    def change_state(self,input:int) -> None:
        if input == 0 or input == 1:
            self.state = input
        else:
            pass

    def update(self):
        pygame.draw.rect(self.SCREEN,(200,200,200),(864,0,232,640),0)
        pygame.draw.rect(self.SCREEN,(150,160,170),(0,576,1000,64))
        self.SCREEN.blit(self.change_button_0.get_image(),self.change_button_0.get_rect())
        self.SCREEN.blit(self.change_button_1.get_image(),self.change_button_1.get_rect())

        for button in self.buttons_list:
            if self.state == 0: #Building menu
                if button.is_available():
                    if isinstance(button,BuildingButton):
                        self.SCREEN.blit(button.get_image(),button.get_rect())
            else:
                if button.is_available():
                    if isinstance(button,UnitButton):
                        self.SCREEN.blit(button.get_image(),button.get_rect())

            if isinstance(button,UnitButton): # Updates unit producing buttons to see if they're allowed to be active.
                for building in self.building_list:
                    # if building.isinstance(UnitProducer):
                    # Not implemented yet but when implemented, will be enabled

                        unit_list = building.get_units()
                        for unit in unit_list:
                            if unit == button.get_unit():
                                x, y = building.get_pos()[0].building.get_pos[1]
                                button.set_spawn_pos(x,y)
                                break
            