### EnemyAI Class - Only single instance should exist.
#
#
#

import pygame
import random



class EnemyAI():

    def __init__(self,grid,hud,player_unit_list,player_building_list,projectile_list,natural_building_list):
        self.grid = grid
        self.hud = hud
        self.player_unit_list = player_unit_list
        self.player_building_list = player_building_list
        self.projectile_list = projectile_list
        self.natural_building_list = natural_building_list
        
        self.unit_blueprint_list = [] # List containing blueprints of usable enemy units and their cost in format [enemy,cost].
        self.group_blueprint_list = [] # List containing groups of units that haven't been called yet
        self.unit_list = [] # List containing active enemies
        
        self.wave_time = 30000
        self.wave_time_left = self.wave_time
        self.wave_timer = pygame.time.Clock()
        self.point_limit = 100

    
    def construct_group(self,current_points,target): #Creates a group with an order and a group of enemies
        base_unit = self.unit_blueprint_list[random.randint(0,len(self.unit_blueprint_list)-1)]
        complement_unit = self.unit_blueprint_list[random.randint(0,len(self.unit_blueprint_list)-1)]
        
        base_unit_amount = random.randint(1,(current_points//base_unit[1]))
        current_points-=base_unit[1]*base_unit_amount
       
        complement_unit_amount = current_points//complement_unit[1]

        target_x, target_y = target.get_pos()




    def on_wave(self):
        self.point_limit += random.randint(20,100)
        current_points = self.point_limit
        self.wave_time_left = self.wave_time
        for building in self.player_building_list: # MCV attack logic (Main attack group)
            if building.get_name() == "MCV":
                if current_points < 300:
                    self.construct_group(current_points,building)
                else:
                    points = random.randint(0,current_points)
                    current_points-=points
                    self.construct_group(points,building)
        while current_points > 30:
            points = random.randint(0,current_points)
            current_points-=points
            for building in self.player_building_list:
                if building.get_name() == "smeltry":
                    self.construct_group(points,building)



