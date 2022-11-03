# Hud Class - Holds the buttons and draws the side menus. Only one instance of this class should ever exist.
# 
#  
#

import pygame

from buildingbutton import BuildingButton
from unitbutton import UnitButton
from button import Button

class Hud():

    def __init__(self,building_list: list, natural_building_list: list, SCREEN: pygame.Surface):
        
        self.building_list = building_list
        self.natural_building_list = natural_building_list
        self.SCREEN = SCREEN
        self.buttons_list = []
        self.buttons_list = [BuildingButton(self,self.SCREEN,self.buttons_list,self.building_list,None,"images/ore_smelter.png","Building(self.SCREEN,self.building_list,'smeltry',150,'images/ore_smelter.png',[0,0])"),
        BuildingButton(self,self.SCREEN,self.buttons_list,self.building_list,None,"images/barracks.png","Building(self.SCREEN,self.building_list,'barracks',50,'images/barracks.png',[0,0])"),
        BuildingButton(self,self.SCREEN,self.buttons_list,self.building_list,None,"images/defence_tower.png","Building(self.SCREEN,self.building_list,'defence',100,'images/defence_tower.png',[0,0])")] # Buttons to be manually created
        self.state = 0
        self.change_button_0 = Button(self,SCREEN,self.buttons_list,"images/building_menu.png","",0)
        self.change_button_0.set_pos(864,50)
        self.change_button_1 = Button(self,SCREEN,self.buttons_list,"images/unit_menu.png","",0)
        self.change_button_1.set_pos(932,50)
        self.grid = None
        self.money = 5
        self.font = pygame.font.Font("fonts/C&C Red Alert [INET].ttf",24)

        self.building_string = ""
        self.is_building = False
        self.building_button = BuildingButton(self,self.SCREEN,[],self.building_list)
        # Used for placing down buildings. Stores the building creation code and whether a building is selected.



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

    def get_is_building(self) -> bool:
        return self.is_building

    def get_building_string(self):
        return self.building_string

    def get_building_button(self):
        return(self.building_button)

    def get_money(self)->int:
        return self.money


    def set_building_string(self,string):
        self.building_string = string
    
    def set_is_building(self,value:bool):
        self.is_building = value
    
    def set_building_button(self,button):
        self.building_button = button

    def set_grid(self,grid):
        self.grid = grid


    def sub_money(self,amount):
        self.money-=amount
        text = self.font.render(f"-{amount}",False,(235,30,30))
        self.SCREEN.blit(text,(890,10))

    # Other subroutines

    def on_press(self,mouse_x: int,mouse_y: int) -> None:

        for button in self.buttons_list:
            if button.get_rect().collidepoint(mouse_x,mouse_y) and button.is_available():
                pygame.draw.rect(self.SCREEN,(0,255,0),(button.get_pos()[0]-4,button.get_pos()[1]-4,40,40),2) 
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
            if self.state == 0: # Building menu
                if button.is_available():
                    if isinstance(button,BuildingButton):
                        self.SCREEN.blit(button.get_image(),button.get_rect())
            else: # Unit menu
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
        a = self.font.render(f"Funds: {self.money}",False,(140,147,168))
        self.SCREEN.blit(a,(870,30))