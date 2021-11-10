line_one = ["_", "_", "_"]
line_two = ["_", "_", "_"]
line_three = ["_", "_", "_"]

matriz_jogo = [ line_one,
                line_two,
                line_three ] 
def ganhou():
            
            if matriz_jogo[0][0] =="X" and matriz_jogo[0][1] == "X" and matriz_jogo [0][2] == "X":
                return 1       
            
            if matriz_jogo[0][0] =="O" and matriz_jogo[0][1] == "O" and matriz_jogo [0][2] == "O":
                return 2       
            
            if matriz_jogo[1][0] =="X" and matriz_jogo [1][1] == "X" and matriz_jogo [1][2] =="X":
                return 1       
            
            if matriz_jogo[1][0] =="O" and matriz_jogo [1][1] == "O" and matriz_jogo [1][2] =="O":
                return 2       
            
            if matriz_jogo[2][0] =="X" and matriz_jogo[2][1] == "X" and matriz_jogo [2][2]=="X":
                return 1       
         
            if matriz_jogo[2][0] =="O" and matriz_jogo[2][1] == "O" and matriz_jogo [2][2]=="O":
                return 2       
            
            if matriz_jogo[0][0]=="X" and matriz_jogo[1][0]=="X" and matriz_jogo[2][0]=="X":
                return 1                 
               
            
            if matriz_jogo[0][0]=="O" and matriz_jogo[1][0]=="O" and matriz_jogo[2][0]=="O":
                return 2       
            
            if matriz_jogo[1][0]=="X" and matriz_jogo[1][1]=="X" and matriz_jogo[1][2]=="X":         
                return 1              
            
            if matriz_jogo[1][0]=="O" and matriz_jogo[1][1]=="O" and matriz_jogo[1][2]=="O":          
                return 2        
            
            if matriz_jogo[2][0]=="O" and matriz_jogo[2][1]=="O" and matriz_jogo[2][2]=="O":      
                return 2   
            
            if matriz_jogo[0][0]=="X" and matriz_jogo[1][1]=="X" and matriz_jogo[2][2]=="X":
                return 1 
            
            if matriz_jogo[0][0]=="O" and matriz_jogo[1][1]=="O" and matriz_jogo[2][2]=="O":
                return 2
            
            if matriz_jogo[0][0]=="X" and matriz_jogo[1][0]=="X" and matriz_jogo[2][0]=="X":
                return 1 
            
            if matriz_jogo[0][0]=="O" and matriz_jogo[1][0]=="O" and matriz_jogo[2][0]=="O":
                return 2
            
            if matriz_jogo[0][2]=="X" and matriz_jogo[1][2]=="X" and matriz_jogo[2][2]=="X":
                return 1
            
            if matriz_jogo[0][2]=="O" and matriz_jogo[1][2]=="O" and matriz_jogo[2][2]=="O":
                return 2
            
            if matriz_jogo[0][1]=="X" and matriz_jogo[1][1]=="X" and matriz_jogo[2][1]=="X":
                return 1         
            
            if matriz_jogo[0][1]=="O" and matriz_jogo[1][1]=="O" and matriz_jogo[2][1]=="O":
                return 2
            
            if matriz_jogo[0][0]=="X" and matriz_jogo[1][0]=="X" and matriz_jogo[2][0]=="X":
                return 2
            
            if matriz_jogo[0][0]=="O" and matriz_jogo[0][1]=="O" and matriz_jogo[0][2]=="O":
                return 2
            
            if matriz_jogo[0][0] == "X" and matriz_jogo[0][1] == "X" and matriz_jogo[0][2] == "X":
                return 1
            
            if matriz_jogo[0][0]== "X" and matriz_jogo[1][0]== "X" and matriz_jogo[2][0]== "X":
                return 1
            
            if matriz_jogo[0][0]== "O" and matriz_jogo[1][0]== "O" and matriz_jogo[2][0]== "O":
                return 2
            
            if matriz_jogo[0][1]=="X" and matriz_jogo[1][1]== "X" and matriz_jogo[2][1]== "X":
                return 1
            
            if matriz_jogo[0][1]=="O" and matriz_jogo[1][1]== "O" and matriz_jogo[2][1]== "O":
                return 2
            
            if matriz_jogo[0][2]== "X" and matriz_jogo[1][2]== "X" and matriz_jogo[2][2]== "X":
                return 1
            
            if matriz_jogo[0][2] == "O" and matriz_jogo[1][2] == "O" and matriz_jogo[2][2] == "O":
                return 2
            

def menu():     

    y = 0
    x = 1
    vencedor = 0
    jogadas = 0
     
    while True:

        if  x == 1:
            while True:
                jogador1_l = int(input("jogador 1: digite a linha desejada: "))
                jogador1_c = int(input("jogador 1: digite a coluna desejada: ")) 
                print("")
                if(matriz_jogo[jogador1_l][jogador1_c] == '_'):
                    matriz_jogo[jogador1_l][jogador1_c]="X"
                    jogadas = jogadas + 1
                    break
                else:
                    print('Posição Ocupada!! Selecione outra posição')


            print(line_one)
            print(line_two)
            print(line_three)
            print("")
            
            vencedor = ganhou()
            if jogadas > 9:
                break
            if vencedor == 1:
                print("parabens jogador 1 voce ganhou o jogo!")
                break
            
            x = 0
            
            
                            
        if x == 0:
            while True:
                jogador2_l = int(input("jogador 2: digite a linha desejada: "))
                jogador2_c = int(input("jogador 2: digite a coluna desejada: ")) 
                print("")
                if(matriz_jogo[jogador2_l][jogador2_c] == '_'):
                    matriz_jogo[jogador2_l][jogador2_c]="O"
                    jogadas = jogadas + 1
                    break
                else:
                    print("posição ja ocupada!")
            print(line_one)
            print(line_two)
            print(line_three)
            print("")
            vencedor = ganhou()

          
            if jogadas > 9:
                break
            if vencedor == 2:
                print("parabens jogador 2 voce ganhou o jogo!")
                break   
            x=1

while True:      
    menu()
    continuar = input('Deseja continuar [s] [n]')
    if continuar == 's':
        line_one = ["_", "_", "_"]
        line_two = ["_", "_", "_"]
        line_three = ["_", "_", "_"]

        matriz_jogo = [ line_one,
                        line_two,
                        line_three ] 
    elif continuar == 'n':
        break
