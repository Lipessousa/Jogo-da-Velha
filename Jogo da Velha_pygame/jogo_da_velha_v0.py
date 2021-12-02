#Joogv0
import time
import sys
import pygame

pygame.init()

size = width, height = 600, 600

screen = pygame.display.set_mode(size)

black = 0, 0, 0
white = 255, 255, 255
x = 0

xis = pygame.image.load("xis.png")
bola = pygame.image.load("bola.png")
xis = pygame.transform.scale(xis, (100,100))
bola = pygame.transform.scale(bola, (100,100))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if(x == 0):
        screen.fill(white)
        x = 1
        screen.blit(xis, (0,0))
        screen.blit(xis, (100,0))
        screen.blit(xis, (0,100))
    else:
        screen.fill(black)
        x = 0
        screen.blit(bola, (0,0))

    time.sleep(5)
    pygame.display.flip()
    pygame.transform.scale(xis, (100,100))
    pygame.transform.scale(bola, (100,100))
    
    
