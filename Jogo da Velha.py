#Jogo da Velha
#Autor: Felipe da Silva Sousa


linhaA = ['_','_','_']
linhaB = ['_','_','_']
linhaC = ['_','_','_']
matriz = [linhaA, linhaB, linhaC]

def check_xis():
    vencedor= " "
    if(linhaA[0] == "X") and (linhaA[1] == "X") and (linhaA[2] == "X"):
        vencedor = "X"

            
    elif(linhaB[0] == 'X') and (linhaB[1] == 'X') and (linhaB[2] == 'X'):
        vencedor = "X"

            
    elif(linhaC[0] == 'X') and (linhaC[1] == 'X') and (linhaC[2] == 'X'):
        vencedor = "X"

       
    elif(linhaA[0] == 'X') and (linhaB[0] == 'X') and (linhaC[0] == 'X'):
        vencedor = "X"

          
    elif(linhaA[1] == 'X') and (linhaB[1] == 'X') and (linhaC[1] == 'X'):
        vencedor = "X"
 
            
    elif(linhaA[2] == 'X') and (linhaB[2] == 'X') and (linhaC[2] == 'X'):
        vencedor = "X"

      
    elif(linhaA[0] == 'X') and (linhaB[1] == 'X') and (linhaC[2] == 'X'):
        vencedor = "X"

            
    elif(linhaC[0] == 'X') and (linhaB[1] == 'X') and (linhaA[2] == 'X'):
        vencedor = "X"

    return vencedor


def check_bola():
    vencedor = " "
    if(linhaA[0] == 'O') and (linhaA[1] == 'O') and (linhaA[2] == 'O'):
        vencedor = "O"

             
    elif(linhaB[0] == 'O') and (linhaB[1] == 'O') and (linhaB[2] == 'O'):
        vencedor = "O"

             
    elif(linhaC[0] == 'O') and (linhaC[1] == 'O') and (linhaC[2] == 'O'):     
        vencedor = "O"
         
    elif(linhaA[0] == 'O') and (linhaB[0] == 'O') and (linhaC[0] == 'O'):        
        vencedor = "O"

    elif(linhaA[1] == 'O') and (linhaB[1] == 'O') and (linhaC[1] == 'O'):        
        vencedor = "O"

                     
    elif(linhaA[2] == 'O') and (linhaB[2] == 'O') and (linhaC[2] == 'O'):         
        vencedor = "O"

           
    elif(linhaA[0] == 'O') and (linhaB[1] == 'O') and (linhaC[2] == 'O'):        
        vencedor = "O"


    elif(linhaC[0] == 'O') and (linhaB[1] == 'O') and (linhaA[2] == 'O'):      
        vencedor = "O"

    return vencedor

 

while True:
    #Jogador 1
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
    
 
    jogador_vencedor  =  check_xis()
    if (jogador_vencedor != " "):
        print ("FIM DE JOGO!!! JOGADOR 1 VENCEU!!!!")
        reiniciar = (input("Dseja reiniciar p jogo? [s] para sim [n] para não: "))
        if (reiniciar == "n"):
            print ("FIM DE JOGO!!!")
            break
        elif (reiniciar == "s"):
            print (linhaA) 
            print (linhaA)  
            print (linhaA)  

   
 
       

        
    
    
    #Jogador 2
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

 
    jogador_vencedor  = check_bola()
    if (jogador_vencedor != " "):
        print ("FIM DE JOGO!!! JOGADOR 2 VENCEU!!!!")
        reiniciar = (input("Dseja reiniciar o jogo? [s] para sim [n] para não: "))
        if (reiniciar == "n"):
            print ("FIM DE JOGO!!!")
            break
        else:
            print (linhaA)  
            print (linhaA)  
            print (linhaA)  


 
        

 
        
        
    
        
 
