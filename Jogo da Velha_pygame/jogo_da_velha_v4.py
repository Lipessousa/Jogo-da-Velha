#Joogv3

import sys
import pygame

 
pygame.init()

pygame.mixer.music.load('mantra-official-video.mp3')
pygame.mixer.music.play(-1, 0.0)


tamanho = comprimento, altura = 600, 600
tela = pygame.display.set_mode(tamanho)

xis = pygame.image.load("xis.png")
bola = pygame.image.load("bola.png")

xis = pygame.transform.scale(xis, (100,100))
bola = pygame.transform.scale(bola, (100,100))


preto = 0, 0, 0
branco = 255, 255, 255
vermelho = 255, 0, 0
verde = 0, 255, 0
azul = 0, 0, 255
cores = [preto, branco, vermelho, verde, azul]

quadrante_linha = [50, 250, 450]
quadrante_coluna = [50, 250, 450]

tela.fill(cores[0])

vez = "X"
rodada = 0

def desenha_jogo():
    #colunas
    pygame.draw.line(tela, verde, (200,0), (200,600), 5)
    pygame.draw.line(tela, verde, (400,0), (400,600), 5)
    #linhas
    pygame.draw.line(tela, verde, (0,200), (600,200), 5)
    pygame.draw.line(tela, verde, (0,400), (600,400), 5)
   
def jogada_xis(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)

    tela.blit(xis, (quadrante_linha[index_linha], quadrante_coluna[index_coluna]))

def jogada_bola(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)
    

    tela.blit(bola, (quadrante_linha[index_linha], quadrante_coluna[index_coluna]))


while True:
    desenha_jogo()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
         
            if(vez == "X"):
                jogada_xis (click_pos)
                print ("Vez de X")
                vez = "O"
                rodada = rodada +1

            elif(vez == "O"):
                jogada_bola (click_pos)
                print("Vez de O")
                vez = "X"
                rodada = rodada+1

            if (rodada == 9):
                break
            


           


    pygame.display.flip()
  
    
    
