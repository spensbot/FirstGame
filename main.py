import pygame
from parameters import *
from functions import *
import time
import random
from classes import GameMenu


#initialize pygame
pygame.init()
surface = pygame.display.set_mode((width, height))
font = pygame.font.SysFont("Courier", )

#initailize variables
clock = time.time()
frame = 0
obstacles = [[400.0, 200]]
pos = 0.0 #pixels
vel = 0.0 #pixles/second
spawn_chance = initial_spawn_chance

while mainloop:

    #restrict framerate to specified FPS
    delta = int(period - (time.time() - clock))
    pygame.time.wait(delta)

    #handle user input
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        break
    elif ev.type == pygame.KEYDOWN:
        key = ev.dict["key"]
        if key == 32:
            vel = jump_vel

    #Generate and move obstacles
    if frame % spawn_chance_increment == 0:
        spawn_chance -= 1
        if spawn_chance < 1:
            spawn_chance = 1
        print(delta)
    for i in range(len(obstacles)):
        obstacles[i][0] -= speed/FPS
    if random.randint(1,spawn_chance) == 1:
        obstacles.append([float(width), random.randint(1,height-obstacle_height)])

    #calculate player position
    pos += vel/FPS
    vel -= gravity/FPS
    if pos < 0:
        pos = 0.0
        vel = 0.0
    elif pos > height-player_height:
        pos = height-player_height
        vel = 0.0

    #check for a collision
    for i in range(len(obstacles)):
        if player_offset-obstacle_width < obstacles[i][0] < player_offset+player_width:
            if pos < height - obstacles[i][1] < pos + player_height + obstacle_height:
                print("HIT")

    #draw the window
    draw_window(surface)
    draw_obstacles(surface, obstacles)
    draw_player(surface, pos)

    pygame.display.flip()
    clock = time.time()
    frame += 1

pygame.quit()


