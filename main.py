import pygame
import random

pygame.init()

# Display settings
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 640
SCREEN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("RTSD")

# Clock Settings
fps = 60
clock = pygame.time.Clock()

# Lists defined
unit_list = []
building_list = []
natural_building_list = []
projectile_list = []

#Ingame trackers
money = 100

#Run loop
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    SCREEN.fill((250,250,250))

    pygame.display.update()

    clock.tick(fps)