import pygame
import sys
import os
from pyshortcuts import make_shortcut
from sys import exit

make_shortcut('C:/Users/filac/PycharmProjects/pygame/main.py', name='nigga')

pygame.init()
screen = pygame.display.set_mode((780,350))
pygame.display.set_caption('Run my nigga')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

background = pygame.image.load('C:/Users/filac/OneDrive/Plocha/My projects/game/sky).jpg')
ground = pygame.image.load('C:/Users/filac/OneDrive/Plocha/My projects/game/ground2.jpg')
text = font.render('Waguan', False, 'Black')
char = pygame.image.load('C:/Users/filac/OneDrive/Plocha/My projects/game/dog.gif')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0,-60))
    screen.blit(ground, (0, 250))
    screen.blit(text, (325, 20))
    screen.blit(char, (325, 20))

    pygame.display.update()
    clock.tick(60)