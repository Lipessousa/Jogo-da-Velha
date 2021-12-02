import pygame
import sys

pygame.init()

#Tela
tamanho = comprimento, altura = 600, 600
janela = pygame.display.set_mode(tamanho)

#Carrega imagens
xis = pygame.image.load("xis.png")
bola = pygame.image.load("bola.png")

xis = pygame.transform.scale(xis, (100,100))
bola = pygame.transform.scale(bola,(100,100))

# cores:
preto = 0, 0, 0
branco = 255, 255, 255
vermelho = 255, 0, 0
verde = 0, 255, 0
azul = 0, 0, 255
ciano = 27, 242, 213
rosa = 203, 7, 118
roxo = 158, 151, 255
roxo2 = 74, 50, 155
verdeagua = 38, 209, 175
roxo3 = 175, 163, 222

cores = [preto, branco, vermelho, verde, azul, ciano, rosa, roxo, roxo2, verdeagua, roxo3]

vez = 'X'
rodada = 0

jogo = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'] ]

#Pos quadrantes
quadrante_linha = [50 , 250, 450]
quadrante_coluna = [50, 250, 450]

#Preenche a janela (0: preto - 1: branco - 2: vermelho - 3: verde - 4:azul - 5:ciano - 6:rosa - 7:roxo - 8:roxo2 - 9:verde água - 10:roxo 3)
janela.fill(cores[10]) 

#Desenha o jogo da velha
def desenha_quadro():
    pygame.draw.line(janela, preto, (200,0),(200,600),15)
    pygame.draw.line(janela, preto, (400,0),(400,600),15)
    pygame.draw.line(janela, preto, (0,200),(600,200),15)
    pygame.draw.line(janela, preto, (0,400),(600,400),15)


#Função para inserir imagem X ou O
def faz_jogada_bola(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)
    
    if (jogo[index_coluna][index_linha] == '_'):
        janela.blit(bola,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        jogo[index_coluna][index_linha] = 'O'
        return True
    else:
        print('Posição ocupada')
        return False


def faz_jogada_xis(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)

    if (jogo[index_coluna][index_linha] == '_'):
        janela.blit(xis,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        jogo[index_coluna][index_linha] = 'X'
        return True

    else:
        print('Posição ocupada')
        return False 
        
while True:
    desenha_quadro()

    
    #Verifica eventos na janela do jogo
    for event in pygame.event.get():
        #Se for pressionado o fechar da janela o jogo é encerrado
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
                        

            if (vez=='X'):
                print("Vez de X")
                fez_jogada = faz_jogada_xis(click_pos)

                if (fez_jogada == True):
                    vez='O'
                    rodada = rodada + 1
                elif (fez_jogada == False):
                    vez = 'X'
                
            elif (vez=='O'):
                print("Vez de O")
                fez_jogada = faz_jogada_bola(click_pos)

                if (fez_jogada == True):
                    vez = 'X'
                    rodada = rodada + 1
                elif (fez_jogada == False):
                    vez = 'O'

            if (rodada>=9):
                print ('finish')
                print(jogo)
                break

    pygame.display.flip() #Atualiza a janela
