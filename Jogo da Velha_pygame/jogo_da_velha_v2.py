#Joogv2


import time
import sys
import pygame

pygame.init()


size = width, height = 600, 600
screen = pygame.display.set_mode(size)


black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
colors = [black, white, red, green, blue]

x = 0

xis = pygame.image.load("xis.png")
bola = pygame.image.load("bola.png")

xis = pygame.transform.scale(xis, (100,100))
bola = pygame.transform.scale(bola, (100,100))

screen.fill(white)

def desenha_jogo():
    #colunas
    pygame.draw.line(screen, black, (200,0), (200,600), 5)
    pygame.draw.line(screen, black, (400,0), (400,600), 5)
    #linhas
    pygame.draw.line(screen, black, (0,200), (600,200), 5)
    pygame.draw.line(screen, black, (0,400), (600,400), 5)
    
def bola():
    screen.blit(bola, (50, 50))
    screen.blit(bola, (50, 250))
    screen.blit(bola, (50, 450))
    screen.blit(bola, (250, 50))
    screen.blit(bola, (450, 50))
    screen.blit(bola, (50, 50))
    screen.blit(bola, (50, 50))
    screen.blit(bola, (50, 50))
    screen.blit(bola, (450,450))
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    desenha_jogo()

    pygame.display.flip()
  
    
    
