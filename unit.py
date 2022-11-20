### Unit Class - Only to exist in a list in main
#
#
#

import pygame
import math
from projectile import Projectile
from building import Building


class Unit():

    def __init__(self,SCREEN,name:str,health:int,unit_list:list,enemy_list:list,natural_building_list:list,projectile_list:list,projectile_speed: int=10,projectile_image: str = "images/default.png",projectile_damage: int = 1,pos:list=[0,0],image:str="images/default.png",maxdistance:int=64,rof:int=1,speed:int=5):
        self.name = name
        self.SCREEN = SCREEN
        self.health = health
        self.range = maxdistance
        self.rof = rof
        self.fire_period = 1000/self.rof
        self.clock = pygame.time.Clock()
        self.speed = speed
        self.unit_list = unit_list
        self.unit_list.append(self)
        self.enemy_list = enemy_list
        self.natural_building_list = natural_building_list

        self.projectile_list = projectile_list
        self.projectile_speed = projectile_speed
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
    
    def reduce_health(self,amount):
        self.health -= amount
        if self.health <= 0:
            self.on_death()

    # Other functions

    def move_to(self,target_pos):
        self.ordered = True
        self.target = target_pos
    
    def attack(self,target):
        self.ordered = True
        self.target = target


    def update(self):
        if self.ordered == True:
            if isinstance(self.target,list):

                # Working out x and y velocity
                target_x,target_y = self.target # Target position
                target_x = target_x-16
                target_y = target_y-16
                pos_x,pos_y = self.pos # Own position

                absolute_distance = int(math.sqrt(math.pow(target_y-pos_y,2)+math.pow(target_x-pos_x,2)))
                if absolute_distance < 10:
                    self.ordered = False

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

            elif isinstance(self.target,Unit) or isinstance(self.target,Building):
                # Working out x and y velocity
                target_x,target_y = self.target.get_pos() # Target position
                target_x = target_x-16
                target_y = target_y-16
                pos_x,pos_y = self.pos # Own position

                absolute_distance = int(math.sqrt(math.pow(target_y-pos_y,2)+math.pow(target_x-pos_x,2)))
                if absolute_distance >= self.range:                    
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

        # Shooting & projectile code
        if self.fire_period>0:
            self.fire_period-=self.clock.tick(60)
        elif not(isinstance(self.target,list)) and self.ordered == True:
            if absolute_distance < self.range:
                if self.target.get_health()<1:
                    self.ordered = False
                else:
                    Projectile(self.SCREEN,[self.pos[0],self.pos[1]],self.projectile_speed,self.projectile_image,self.projectile_list,self.natural_building_list,self.enemy_list,self.projectile_damage,[target_x,target_y])
                    self.fire_period = 1000/self.rof
        else:
            closest_enemy = None
            closest_distance = 0
            for enemy in self.enemy_list:
                target_x,target_y = enemy.get_pos()
                absolute_distance = int(math.sqrt(math.pow(target_y-self.pos[1],2)+math.pow(target_x-self.pos[0],2)))
                if absolute_distance < closest_distance or closest_distance == 0:
                    closest_distance = absolute_distance
                    closest_enemy = enemy
            if closest_distance < self.range:
                try:
                    Projectile(self.SCREEN,[self.pos[0]+int(self.rect.width/2),self.pos[1]+int(self.rect.height/2)],self.projectile_speed,self.projectile_image,self.projectile_list,self.natural_building_list,self.enemy_list,self.projectile_damage,(target_x,target_y))
                except:
                    pass

        self.SCREEN.blit(self.get_image(),self.get_rect())


    def on_death(self):
        self.unit_list.remove(self)

    


    