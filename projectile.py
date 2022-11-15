### Projectile Class - Should only be referenced in projectile_list in main
#
# This will be an object that will barrel towards a destination and if colliding with anything along the way, will hit it.
#

import pygame
import math


class Projectile():

    def __init__(self,SCREEN,pos:list,speed:float,image:str,projectile_list,enemy_building_list,enemy_list,damage,target_pos):
        
        # Variable assignment
        self.SCREEN = SCREEN
        self.speed = speed
        self.image = pygame.image.load(image)
        self.rect = pygame.rect
        self.pos = pos
        self.damage = damage
        
        # Lists
        self.projectile_list = projectile_list
        self.projectile_list.append(self)
        self.enemy_building_list = enemy_building_list
        self.enemy_list = enemy_list
        self.target_pos = target_pos
        
        # Rectangle assignment
        self.rect = self.image.get_rect()
        self.rect.topleft = ((self.pos[0],self.pos[1]))

        # Working out x and y velocity
        target_x,target_y = self.target_pos # Target position
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

    def get_image(self):
        return(self.image)

    def get_rect(self):
        return(self.rect)

    def on_death(self):
        self.projectile_list.remove(self)
        # Removing the only reference to itself will automatically clean it up from memory

    def update(self):
        self.pos = [self.pos[0]+self.speed_x,self.pos[1]+self.speed_y]
        self.rect.topleft = ((self.pos[0],self.pos[1]))  # type: ignore
        
        # Checks for collisions 
        for enemy_building in self.enemy_building_list:
            if enemy_building.get_rect().colliderect(self.get_rect()):
                enemy_building.reduce_health(self.damage)
                self.on_death()
        for enemy in self.enemy_list:
            if enemy.get_rect().colliderect(self.get_rect()):
                enemy.reduce_health(self.damage)
                self.on_death()
        if self.pos[0] < 0 or self.pos[0] > 864 or self.pos[1] < 0 or self.pos[1] > 576: 
            # Checks if out of boundry, useful for keeping memory usage low.
            self.on_death()
                
        self.SCREEN.blit(self.get_image(),self.get_rect())
    