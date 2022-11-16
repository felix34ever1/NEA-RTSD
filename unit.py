### Unit Class - Only to exist in a list in main
#
#
#

import pygame
import math


class Unit():

    def __init__(self,SCREEN,name:str,health:int,unit_list:list,enemy_list:list,natural_building_list:list,projectile_list:list,projectile_speed: int=10,projectile_image: str = "images/default.png",projectile_damage: int = 1,pos:list=[0,0],image:str="images/default.png",range:int=64,rof:int=1,speed:int=5):
        self.name = name
        self.SCREEN = SCREEN
        self.health = health
        self.range = range
        self.rof = rof
        self.speed = speed
        self.unit_list = unit_list
        self.unit_list.append(self)
        self.enemy_list = enemy_list
        self.natural_building_list = natural_building_list

        self.projectile_list = projectile_list
        self.projecitle_speed = projectile_speed
        self.projectile_image = projectile_image
        self.projectile_damage = projectile_damage

        self.pos = pos
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (tuple(pos))
        
        self.ordered = False
        self.target = [0,0]

    def get_name(self):
        return(self.name)
    
    def get_health(self):
        return(self.health)
    
    def get_pos(self):
        return(self.pos)
    
    def get_rect(self):
        return(self.rect)
    
    def get_image(self):
        return(self.image)

    def set_pos(self,pos:list):
        self.pos = pos
        self.rect.topleft = (tuple(pos))
    
    def sub_health(self,amount):
        self.health -= amount
        if self.health <= 0:
            self.on_death()

    # Other functions

    def move_to(self,target_pos):
        self.ordered = True
        self.target = target_pos


    def update(self):
        if self.ordered == True:
            if isinstance(self.target,list):

                # Working out x and y velocity
                target_x,target_y = self.target # Target position
                pos_x,pos_y = self.pos # Own position
                
                try:
                    self.theta = math.atan(abs(target_y-pos_y)/abs(target_x-pos_x))
                except ZeroDivisionError:
                    self.theta = math.pi/2
                # Get angle between self and target assuming target is in bottom left of projectile. 
                if pos_x > target_x:
                    if pos_y > target_y:
                        self.speed_x = -(math.cos(self.theta)*self.speed)
                        self.speed_y = -(math.sin(self.theta)*self.speed)
                    else:
                        self.speed_x = -(math.cos(self.theta)*self.speed)
                        self.speed_y = math.sin(self.theta)*self.speed
                else:
                    if pos_y < target_y:
                        self.speed_x = math.cos(self.theta)*self.speed
                        self.speed_y = math.sin(self.theta)*self.speed
                    else:
                        self.speed_x = math.cos(self.theta)*self.speed
                        self.speed_y = -(math.sin(self.theta)*self.speed)
                self.set_pos([self.pos[0]+self.speed_x,self.pos[1]+self.speed_y])

                    # Stands in for advanced movement
        self.SCREEN.blit(self.get_image(),self.get_rect())


    def on_death(self):
        self.unit_list.remove(self)

    


    