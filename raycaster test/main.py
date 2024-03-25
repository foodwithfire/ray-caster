import pygame, sys, player
from settings import *

screen = pygame.display.set_mode(screensize)

player = player.Player([screensize[0]/2, screensize[1]/2])

clock = pygame.time.Clock()
while True:
    dt = clock.tick(60)
    screen.fill("white")

    player.update(dt)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
