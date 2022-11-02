### Building Class - All instances contained within main.py - building_list or natural_building_list
#
#
#

import pygame


class Building():

    def __init__(self,SCREEN,building_list:list,name: str,health:int=100,image:str="images/default.png",pos:list=[0,0]):
        self.SCREEN = SCREEN
        self.building_list = building_list
        self.health = health
        self.image = pygame.image.load(image)
        self.name = name
        self.pos = pos
        self.building_list.append(self)

        self.rect = self.image.get_rect()
        self.rect.topleft = ((self.pos[0],self.pos[1]))


    # Getters & Setters

    def get_pos(self):
        return(self.pos)

    def get_image(self):
        return(self.image)

    def get_rect(self):
        return(self.rect)
    
    def get_name(self):
        return(self.name)

    def set_pos(self,x,y):
        self.pos = [x,y]
        self.rect.topleft = ((self.pos[0],self.pos[1]))
    # Other subroutines

    def reduce_health(self,number:int):
        self.health-=number

    def update(self):
        self.SCREEN.blit(self.get_image(),self.get_rect())

    def on_death(self):
        self.building_list.remove(self)
        # Removing the only reference to itself will automatically clean it up from memory