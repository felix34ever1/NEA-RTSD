### DefenceBuilding Class - subclass of the Building class.
#
#
#

import math
import pygame
from building import Building
from projectile import Projectile



class DefenceBuilding(Building):

    def __init__(self,hud,name,health,SCREEN,building_list,image,natural_building_list,enemy_list,range:int,projectile_list,pos: list=[0,0],rof = 1,projectile_speed: int=10,projectile_image: str = "images/default.png",projectile_damage: int = 1):
        super().__init__(SCREEN,building_list,name,health,image,pos)
        
        # Variable assignment
        self.natural_building_list = natural_building_list
        self.enemy_list = enemy_list
        self.range = range
        self.projectile_list = projectile_list
        self.rof = rof
        self.time_period = int(1000/self.rof)
        self.rof_clock = pygame.time.Clock()
        self.projectile_speed = projectile_speed
        self.projectile_image = projectile_image
        self.projectile_damage = projectile_damage



    def update(self):

        if self.time_period >0:
            self.time_period-=self.rof_clock.tick()
        if self.time_period <=0:
            closest_enemy = None
            closest_distance = 0
            for enemy in self.enemy_list:
                enemyx,enemyy = enemy.get_pos()
                distance = math.sqrt((enemyx-self.pos[0])^2-(enemyy-self.pos[1]))
                if closest_distance < self.range or closest_enemy == None: # Checks if the unit is the closest enemy unit.
                    closest_enemy = enemy
                    closest_distance = distance
            if closest_enemy != None:
                self.projectile_list.append(Projectile(self.SCREEN,self.pos,self.projectile_speed,self.projectile_image,self.projectile_list,self.natural_building_list,self.enemy_list,self.projectile_damage,[enemyx,enemyy]))
            mouse_x,mouse_y = pygame.mouse.get_pos()
            try:
                distance = math.sqrt((math.pow((mouse_x-self.pos[0]),2)+math.pow((mouse_y-self.pos[1]),2)))
                self.time_period = int(1000/self.rof)
            except:
                pass
            else:
                if distance < self.range:
                    self.projectile_list.append(Projectile(self.SCREEN,[self.pos[0]+16,self.pos[1]+16],self.projectile_speed,self.projectile_image,self.projectile_list,self.natural_building_list,self.enemy_list,self.projectile_damage,[mouse_x,mouse_y]))
                    self.time_period = int(1000/self.rof)


        self.SCREEN.blit(self.get_image(),self.get_rect())

            