import pygame
import random
from building import Building

pygame.init()
from hud import Hud
from inputhandler import InputHandler
from grid import Grid
from projectile import Projectile

# Display settings
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 640
SCREEN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("RTSD")

# Clock Settings
FPS = 60
clock = pygame.time.Clock()

# Lists defined
unit_list = []
enemy_list = []
building_list = []
natural_building_list = []
projectile_list = []

# One time instances defined
hud = Hud(building_list,natural_building_list,SCREEN) # Pylance error is not a problem
inputHandler = InputHandler(SCREEN,hud,unit_list,building_list,natural_building_list,enemy_list,projectile_list)
grid = Grid(SCREEN,[27,18],natural_building_list)
grid.place_grid(Building(SCREEN,building_list,"MCV",150,"images/HQ_0.png",[13*32,9*32]),[13,9])
hud.set_grid(grid)
inputHandler.set_grid(grid)

#Mouse Tracking variables
mouse_down = False
down_length = 0
mouse_x, mouse_y = 0,0


#Run loop
is_running = True
while is_running:
    
    SCREEN.fill((178, 188, 170))

    buttons_pressed = pygame.mouse.get_pressed()
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            is_running = False


    hud.update()
    for building in building_list:
        building.update()
    for building in natural_building_list:
        building.update()
    for projectile in projectile_list:
        projectile.update()
    
    # LMB Logic
    if buttons_pressed[0] == True:
        if mouse_down == False:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x > 864 or mouse_y > 576: #If mouse position in Hud:
                hud.on_press(mouse_x,mouse_y)
            else:
                mouse_down = True

        else:
            down_length+=1
            next_mouse_x, next_mouse_y = pygame.mouse.get_pos()
            if mouse_x<next_mouse_x:
                if mouse_y<next_mouse_y:
                    pygame.draw.rect(SCREEN,(255,255,0),
                    (mouse_x,mouse_y,
                    (abs(mouse_x-next_mouse_x)),
                    (abs(mouse_y-next_mouse_y))),4)
                else:
                    pygame.draw.rect(SCREEN,(255,255,0),
                    (mouse_x,next_mouse_y,
                    (abs(mouse_x-next_mouse_x)),
                    (abs(mouse_y-next_mouse_y))),4)
            else:
                if mouse_y<next_mouse_y:
                    pygame.draw.rect(SCREEN,(255,255,0),
                    (next_mouse_x,mouse_y,
                    (abs(mouse_x-next_mouse_x)),
                    (abs(mouse_y-next_mouse_y))),4)
                else:
                    pygame.draw.rect(SCREEN,(255,255,0),
                    (next_mouse_x,next_mouse_y,
                    (abs(mouse_x-next_mouse_x)),
                    (abs(mouse_y-next_mouse_y))),4)                    

 
    else:
        if mouse_down == True:
            mouse_down = False
            if down_length > 5: # Box select
                inputHandler.box_select(mouse_x,mouse_y,next_mouse_x,next_mouse_y)
                # Box select

            else:
                inputHandler.select(mouse_x,mouse_y)
                # Single select
            
            down_length = 0

    # RMB Logic
    if buttons_pressed[2] == True:
        if mouse_x < 868 or mouse_y < 580: #If mouse position not in Hud:
            inputHandler.order(mouse_x,mouse_y)
    
    inputHandler.update()
    pygame.display.update()


    clock.tick(FPS)