### EconomyBuilding Class - subclass of Building class.
#
# Is used to represent the buildings that can make use of the economy
#

from building import Building
import pygame

class EconomyBuilding(Building):

    def __init__(self,SCREEN,building_list:list,name: str, grid,hud,natural_building_list,health:int=100,image:str="images/default.png",pos:list=[0,0],economy_period:int=1000,economy_tick:int=100):
        super().__init__(SCREEN,building_list,name,health,image,pos)
        self.grid = grid
        self.hud = hud
        self.natural_building_list = natural_building_list
        self.economy_period = economy_period # Amount of time (in miliseconds) between economy ticks
        self.economy_time_value = self.economy_period # Keeps track of the actual timer that ticks down.
        self.economy_tick = economy_tick # Amount of money gained each time the economy ticks.
        self.economy_clock = pygame.time.Clock()
        self.next_to_mine = False
        grid_pos = self.grid.get_grid(self.pos[0],self.pos[1])
        self.tile_list = self.grid.get_tile_list()
        for tileset in self.tile_list:
            for tile in tileset:
                if tile.get_occupied():
                    if tile.get_occupier().get_name() == "mine":
                        gridx,gridy = tile.get_pos()
                        gridx = gridx//32
                        gridy = gridy//32
                        # Going to check if mine is more than 2 distance apart.
                        if abs((self.pos[0]//32)-gridx)+abs((self.pos[1]//32)-gridy) <= 2:
                            self.next_to_mine = True
                            break
                        
    def set_pos(self,x,y): # Override from super
        self.pos = [x,y]
        self.rect.topleft = ((self.pos[0],self.pos[1]))
        self.next_to_mine = False
        grid_pos = self.grid.get_grid(self.pos[0],self.pos[1])
        for tileset in self.tile_list:
            for tile in tileset:
                if tile.get_occupied():
                    if tile.get_occupier().get_name() == "Mine":
                        gridx,gridy = tile.get_pos()
                        gridx = gridx//32
                        gridy = gridy//32
                        # Going to check if mine is more than 2 distance apart.
                        if abs((self.pos[0]//32)-gridx)+abs((self.pos[1]//32)-gridy) <= 2:
                            self.next_to_mine = True
                            break

    def update(self):
        # Will keep a timer going if the building is next to a mine
        if self.next_to_mine:
            self.economy_time_value-=self.economy_clock.tick()
            if self.economy_time_value <= 0:
                self.hud.sub_money(-(self.economy_tick))
                self.economy_time_value = self.economy_period
        
        self.SCREEN.blit(self.get_image(),self.get_rect())
