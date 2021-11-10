#Jogo da Velha

linhaA = ['_','_','_']
linhaB = ['_','_','_']
linhaC = ['_','_','_']
matriz = [linhaA, linhaB, linhaC]

def check_xis():
    if(linhaA[0] == "X") and (linhaA[1] == "X") and (linhaA[2] == "X"):
        vencedor1()

            
    elif(linhaB[0] == 'X') and (linhaB[1] == 'X') and (linhaB[2] == 'X'):
        vencedor1()

            
    elif(linhaC[0] == 'X') and (linhaC[1] == 'X') and (linhaC[2] == 'X'):
        vencedor1()

       
    elif(linhaA[0] == 'X') and (linhaB[0] == 'X') and (linhaC[0] == 'X'):
        vencedor1()

          
    elif(linhaA[1] == 'X') and (linhaB[1] == 'X') and (linhaC[1] == 'X'):
        vencedor1()
 
            
    elif(linhaA[2] == 'X') and (linhaB[2] == 'X') and (linhaC[2] == 'X'):
        vencedor1()

      
    elif(linhaA[0] == 'X') and (linhaB[1] == 'X') and (linhaC[2] == 'X'):
        vencedor1()

            
    elif(linhaC[0] == 'X') and (linhaB[1] == 'X') and (linhaA[2] == 'X'):
        vencedor1()


def check_bola():
    if(linhaA[0] == 'O') and (linhaA[1] == 'O') and (linhaA[2] == 'O'):
        vencedor2()

             
    elif(linhaB[0] == 'O') and (linhaB[1] == 'O') and (linhaB[2] == 'O'):
        vencedor2()

             
    elif(linhaC[0] == 'O') and (linhaC[1] == 'O') and (linhaC[2] == 'O'):
        vencedor2()
         
    elif(linhaA[0] == 'O') and (linhaB[0] == 'O') and (linhaC[0] == 'O'):
        vencedor2()

    elif(linhaA[1] == 'O') and (linhaB[1] == 'O') and (linhaC[1] == 'O'):
        vencedor2()

                     
    elif(linhaA[2] == 'O') and (linhaB[2] == 'O') and (linhaC[2] == 'O'):
        vencedor2()

           
    elif(linhaA[0] == 'O') and (linhaB[1] == 'O') and (linhaC[2] == 'O'):
        vencedor2()


    elif(linhaC[0] == 'O') and (linhaB[1] == 'O') and (linhaA[2] == 'O'):
        vencedor1()


def vencedor1():
    print ("VELHA!!! JOGADOR 1 VENCEU!!!")
    

def vencedor2():
    print ("VELHA!!! JOGADOR 2 VENCEU!!!")

def empate():
    print ("EMPATE!!! MUITO BURROS ;-;")

while True:
    
    while True:
        linhaJ1 = int(input("jogador 1 - Insira a linha: "))
        colunaJ1 = int(input("jogador 1 - Insira a coluna: "))
        if (matriz[linhaJ1][colunaJ1] == "X") or (matriz[linhaJ1][colunaJ1] == "O"):
            print ("Essa posição já está preenchida, escolha outra!!!")
                
        else:
            matriz[linhaJ1][colunaJ1] = "X"
            break
            
        
    print (linhaA)
    print (linhaB)
    print (linhaC)
    
    check_xis()
    
    while True:
        linhaJ2 = int(input("jogador 2 - Insira a linha: "))
        colunaJ2 = int(input("jogador 2 - Insira a coluna: "))
        if (matriz[linhaJ2][colunaJ2] == "X") or (matriz[linhaJ2][colunaJ2] == "O"):
            print ("Essa posição já está preenchida, escolha outra!!!")

        else:
            matriz[linhaJ2][colunaJ2] = "O"
            break

    print (linhaA)
    print (linhaB)
    print (linhaC)

    check_bola()
    
    

         

 
                

   

    

    
 
    
    




 
            
            
        
    




 
 
