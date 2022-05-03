import pygame
import sys
from AlienInvasion import settings

width = 800
height = 600

screen = pygame.display.set_mode((width,height))

print("test")
game_over = False

while not game_over:
    screen.blit(0,0)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit