#Joogv3

import sys
import pygame

 
pygame.init()

pygame.mixer.music.load('mantra-official-video.mp3')
pygame.mixer.music.play(-1, 0.0)

#dimansões da tela
tamanho = comprimento, altura = 600, 600
tela = pygame.display.set_mode(tamanho)

#carrega imagens
xis = pygame.image.load("xis.png")
bola = pygame.image.load("bola.png")

xis = pygame.transform.scale(xis, (100,100))
bola = pygame.transform.scale(bola, (100,100))

#cores
preto = 0, 0, 0
branco = 255, 255, 255
vermelho = 255, 0, 0
verde = 0, 255, 0
azul = 0, 0, 255

#lista de cores
cores = [preto, branco, vermelho, verde, azul]

 
#preenche a tela cor a cor escolhida na lista
tela.fill(cores[0])

vez = "X"
rodada = 0
vencedor_geral = " "
matriz = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"] ]

#posição por quadrante
quadrante_linha = [50, 250, 450]
quadrante_coluna = [50, 250, 450]

#desenha o jogo
def desenha_jogo():
    #colunas
    pygame.draw.line(tela, verde, (200,0), (200,600), 5)
    pygame.draw.line(tela, verde, (400,0), (400,600), 5)
    #linhas
    pygame.draw.line(tela, verde, (0,200), (600,200), 5)
    pygame.draw.line(tela, verde, (0,400), (600,400), 5)

#faz a jogada de X
def jogada_bola(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)
    
    if (matriz[index_linha][index_coluna] == "_"):
        tela.blit(bola,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        matriz[index_linha][index_coluna] = "O"
        return True

    
    else:
        ("posição ocupada")
        return False

#faz a jogada de O
def jogada_xis(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)
    
    if (matriz[index_linha][index_coluna] == "_"):
        tela.blit(xis,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        matriz[index_linha][index_coluna] = "X"
        return True

    
    else:
        print("posição ocupada")
        return False

def check_xis():
    vencedor = " "
    
    #varredura das linhas
    if (matriz[0][0] == "X") and (matriz[0][1] == "X") and (matriz[0][2] == "X"):
        vencedor = "X"
        pygame.draw.line(tela, branco, (0, 100), (600, 100), 5) 
        print ("jogador X venceu!")

    elif (matriz[1][0] == "X") and (matriz[1][1] == "X") and (matriz[1][2] == "X"):
        vencedor = "X"
        pygame.draw.line(tela, branco, (0, 300), (600, 300), 5)
        print ("jogador X venceu!")

    elif (matriz[2][0] == "X") and (matriz[2][1] == "X") and (matriz[2][2] == "X"):
        vencedor = "X"
        pygame.draw.line(tela, branco, (0, 500), (600, 500), 5)
        print ("jogador X venceu!")

    #varredura das colunas
    elif (matriz[0][0] == "X") and (matriz[1][0] == "X") and (matriz[2][0] == "X"):
        vencedor = "X"
        pygame.draw.line(tela, branco, (100, 0), (100, 600), 5)
        print ("jogador X venceu!")

    elif (matriz[0][1] == "X") and (matriz[1][1] == "X") and (matriz[2][1] == "X"):
        vencedor = "X"
        pygame.draw.line(tela, branco, (300, 0), (300, 600), 5)
        print ("jogador X venceu!")

    elif (matriz[0][2] == "X") and (matriz[1][2] == "X") and (matriz[2][2] == "X"):
        vencedor = "X"
        pygame.draw.line(tela, branco, (500, 0), (500, 600), 5)
        print ("jogador X venceu!")

    #varredura das diagonais
    elif (matriz[0][0] == "X") and (matriz[1][1] == "X") and (matriz[2][2] == "X"):
        vencedor = "X"
        pygame.draw.line(tela, branco, (0, 0), (600, 600), 5)
        print ("jogador X venceu!")

    elif (matriz[2][0] == "X") and (matriz[1][1] == "X") and (matriz[0][2] == "X"):
        vencedor = "X"
        pygame.draw.line(tela, branco, (0, 600), (600, 0), 5)
        print ("jogador X venceu!")

    return vencedor

def check_bola():
    vencedor = " "
    
    #varredura das linhas
    if (matriz[0][0] == "O") and (matriz[0][1] == "O") and (matriz[0][2] == "O"):
        vencedor = "O"
        #pygame.draw.line(tela, branco, (0, 100), (600, 100), 5) 
        print ("jogador X venceu!")

    elif (matriz[1][0] == "O") and (matriz[1][1] == "O") and (matriz[1][2] == "O"):
        vencedor = "O"
        #pygame.draw.line(tela, branco, (0, 300), (600, 300), 5)
        print ("jogador X venceu!")

    elif (matriz[2][0] == "O") and (matriz[2][1] == "O") and (matriz[2][2] == "O"):
        vencedor = "O"
        #pygame.draw.line(tela, branco, (0, 500), (600, 500), 5)
        print ("jogador X venceu!")

    #varredura das colunas
    elif (matriz[0][0] == "O") and (matriz[1][0] == "O") and (matriz[2][0] == "O"):
        vencedor = "O"
        #pygame.draw.line(tela, branco, (100, 0), (100, 600), 5)
        print ("jogador X venceu!")

    elif (matriz[0][1] == "O") and (matriz[1][1] == "O") and (matriz[2][1] == "O"):
        vencedor = "O"
        #pygame.draw.line(tela, branco, (300, 0), (300, 600), 5)
        print ("jogador X venceu!")

    elif (matriz[0][2] == "O") and (matriz[1][2] == "O") and (matriz[2][2] == "O"):
        vencedor = "O"
        #pygame.draw.line(tela, branco, (500, 0), (500, 600), 5)
        print ("jogador X venceu!")

    #varredura das diagonais
    elif (matriz[0][0] == "O") and (matriz[1][1] == "O") and (matriz[2][2] == "O"):
        vencedor = "O"
        #pygame.draw.line(tela, branco, (0, 0), (600, 600), 5)
        print ("jogador X venceu!")

    elif (matriz[2][0] == "O") and (matriz[1][1] == "O") and (matriz[0][2] == "O"):
        vencedor = "O"
        #pygame.draw.line(tela, branco, (0, 600), (600, 0), 5)
        print ("jogador X venceu!")

    return vencedor
   





while True:
    desenha_jogo()

    #Verifica os eventos do jogo
    for event in pygame.event.get():

        #se for preessionadoo botão fechar o jogo é encerrado
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()

            #jogador_xis 
            if(vez == "X"):
                print ("Vez de X")
                jogada = jogada_xis(click_pos)
                vencedor_geral = check_xis()
                if (jogada == True):
                    vez = "O"
                    rodada = rodada +1
                elif (jogada == False):
                    vez = "X"



            #jogador_bola
            elif(vez == "O"):
                print("Vez de O")
                jogada = jogada_bola(click_pos)
                vencedor_geral = check_bola()
                if (jogada == True):
                    vez = "X"
                    rodada = rodada+1
                elif (jogada == False):
                    vez = "O"

    #Atualiza a tela a cada evento no jogo
    pygame.display.flip()
    if (rodada >=9) or (vencedor_geral != " "):
        print("fim de jogo")
        print (matriz)
        break
            
           

 
  
    
    
