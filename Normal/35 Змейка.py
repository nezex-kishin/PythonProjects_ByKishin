import time
import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dis=pygame.display.set_mode((500,400))
pygame.display.update()
pygame.display.set_caption('Змейка')

x1 = 300
y1 = 300
x1_change = 0
y1_change = 0
clock = pygame.time.Clock()

game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()
quit()