# Hud Class - Holds the buttons and draws the side menus. Only one instance of this class should ever exist.
# 
#  
#

import pygame


class Hud():

    def __init__(self, building_list: list, natural_building_list: list, SCREEN: pygame.Surface):
        
        self.building_list = building_list
        self.natural_building_list = natural_building_list
        self.SCREEN = SCREEN
        self.buttons_list = [] # Buttons to be manually created
        self.state = 0

    #Getters & Setters

    def get_buttons_list(self) -> list:
        return self.buttons_list

    # Other subroutines

    def on_press(self,mouse_x: int,mouse_y: int) -> None:

        for button in self.buttons_list:
            if button.get_rect().collidepoint(mouse_x,mouse_y) and button.is_available():
                button.on_press()
                break

    def change_state(self,input:int) -> None:
        if input == 0 or input == 1:
            self.state = input
        else:
            pass

    def update(self):
        pygame.draw.rect(self.SCREEN,(200,200,200),(868,0,232,640),0)
        pygame.draw.rect(self.SCREEN,(150,160,170),(0,580,1000,64))

        for button in self.buttons_list:
            if button.is_available():
                self.SCREEN.blit(button.get_rect(),button.get_pos())

            if button.isinstance(UnitButton): # Updates unit producing buttons to see if they're allowed to be active.
                for building in self.building_list:
                    if building.isinstance(UnitProducer):
                        unit_list = building.get_units()
                        for unit in unit_list:
                            if unit == button.get_unit():
                                x, y = building.get_pos()[0].building.get_pos[1]
                                button.set_spawn_pos(x,y)
                                break
                    