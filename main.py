import pygame
from parameters import *
from functions import *
import time
import random

#initialize pygame
pygame.init()
surface = pygame.display.set_mode((width, height))
font = pygame.font.SysFont("Courier", 16)

#initailize variables
clock = time.time()
frame = 0
obstacles = [400.0]
pos = 0.0 #pixels
vel = 0.0 #pixles/second

while 1:

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
    for i in range(len(obstacles)):
        obstacles[i] -= speed/FPS
    if random.randint(1,50) == 1:
        obstacles.append(float(width))

    #calculate player position
    pos += vel/FPS
    vel -= gravity/FPS
    if pos < 0:
        pos = 0.0
        vel = 0.0

    #draw the window
    draw_window(surface)
    draw_obstacles(surface, obstacles)
    draw_player(surface, pos)

    pygame.display.flip()
    clock = time.time()
    frame += 1

pygame.quit()