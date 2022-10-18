### Button class - All instances should exist in a hud instance.
#
#
#

import pygame


class Button():

    def __init__(self,SCREEN:pygame.Surface ,button_list: list, image: str="images/default.png", exec_string: str="",cost:int=1):
        self.SCREEN = SCREEN
        self.image = pygame.image.load(image)
        self.availability = False
        self.exec_string = exec_string # Used as the command that creates a unit/building.
        self.cost = cost
        self.pos = [30,60]
        self.button_list = button_list
        
        self.rect = self.image.get_rect()
        self.rect.topleft = ((self.pos[0],self.pos[1]))

    # Getters & Setters

    def is_available(self):
        return(self.availability)
    
    def get_rect(self):
        return(self.rect)
    
    def get_image(self):
        return(self.image)

    def get_pos(self):
        return(self.pos)

    def set_pos(self,x,y):
        self.pos = [x,y]
        self.rect.topleft = ((self.pos[0],self.pos[1]))

    # Other subroutines

    def on_press(self):
        
        pass

