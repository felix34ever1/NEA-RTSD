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

#Mouse Tracking variables
mouse_down = False
down_length = 0

#Run loop
is_running = True
while is_running:
    
    SCREEN.fill((250,250,250))

    buttons_pressed = pygame.mouse.get_pressed()
    
    # LMB Logic
    if buttons_pressed[0] == True:
        if mouse_down == False:
            mouse_down = True
            mouse_x, mouse_y = pygame.mouse.get_pos()
        else:
            down_length+=1
            next_mouse_x, next_mouse_y = pygame.mouse.get_pos()
            pygame.draw.rect(SCREEN,(255,255,0),
            (mouse_x,mouse_y,
            (abs(mouse_x-next_mouse_x)),
            (abs(mouse_y-next_mouse_y))),4)
 
    else:
        if mouse_down == True:
            mouse_down = False
            if down_length > 5: # Box select
                pass # Box select

            else:
                pass # Single select
            
            down_length = 0

    # RMB Logic
    if buttons_pressed[1] == True:
        pass # Order


    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            is_running = False


    pygame.display.update()

    clock.tick(fps)