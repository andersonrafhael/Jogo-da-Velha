import os
from colorama import Fore, Back, Style

jogarNovamente = "s"
cont_jogadas = 0
jogador = 0
max_jogadas = 9
tabuleiro_instrucao = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def verifica_vencedor():
    global cont_jogadas, tabuleiro

    if(tabuleiro[0][0] == "X" and tabuleiro[0][1] == "X" and tabuleiro[0][2] == "X"):
        cont_jogadas = 11
    if(tabuleiro[1][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[1][2] == "X"):
        cont_jogadas = 11
    if(tabuleiro[2][0] == "X" and tabuleiro[2][1] == "X" and tabuleiro[2][2] == "X"):
        cont_jogadas = 11
    if(tabuleiro[0][0] == "X" and tabuleiro[1][0] == "X" and tabuleiro[2][0] == "X"):
        cont_jogadas = 11
    if(tabuleiro[0][1] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][1] == "X"):
        cont_jogadas = 11
    if(tabuleiro[0][2] == "X" and tabuleiro[1][2] == "X" and tabuleiro[2][2] == "X"):
        cont_jogadas = 11
    if(tabuleiro[0][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][2] == "X"):
        cont_jogadas = 11
    if(tabuleiro[0][2] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][0] == "X"):
        cont_jogadas = 11
    if(tabuleiro[0][0] == "O" and tabuleiro[0][1] == "O" and tabuleiro[0][2] == "O"):
        cont_jogadas = 12
    if(tabuleiro[1][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[1][2] == "O"):
        cont_jogadas = 12
    if(tabuleiro[2][0] == "O" and tabuleiro[2][1] == "O" and tabuleiro[2][2] == "O"):
        cont_jogadas = 12
    if(tabuleiro[0][0] == "O" and tabuleiro[1][0] == "O" and tabuleiro[2][0] == "O"):
        cont_jogadas = 12
    if(tabuleiro[0][1] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][1] == "O"):
        cont_jogadas = 12
    if(tabuleiro[0][2] == "O" and tabuleiro[1][2] == "O" and tabuleiro[2][2] == "O"):
        cont_jogadas = 12
    if(tabuleiro[0][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][2] == "O"):
        cont_jogadas = 12
    if(tabuleiro[0][2] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][0] == "O"):
        cont_jogadas = 12

def instrucao():
    os.system("clear")
    print("\n\n\t\t"+ Fore.GREEN + "### Bem-Vindo ao Jogo da Velha Bolado ###\n\n\n" + Fore.RESET)
    print(Fore.YELLOW + "Instruções do Jogo:\n")
    print("1) Indique o valor da LINHA que deseja jogar")
    print("2) Indique o valor da COLUNA que deseja jogar")
    print("2) Pressione Enter" + Fore.RESET)
    print("\nAs posições do tabuleiro estão distribuídas da seguinte forma:\n\n")
    print("\t\t    0   1   2")
    print("\t\t0:  " + tabuleiro[0][0] + " | " + tabuleiro[0][1] + " | " + tabuleiro[0][2])
    print("\t\t   -----------")
    print("\t\t1:  " + tabuleiro[1][0] + " | " + tabuleiro[1][1] + " | " + tabuleiro[1][2])
    print("\t\t   -----------")
    print("\t\t2:  " + tabuleiro[2][0] + " | " + tabuleiro[2][1] + " | " + tabuleiro[2][2])
    print("\n\nPara iniciar, pressione qualquer tecla...")
    input()

def tela():
    global tabuleiro, cont_jogadas

    os.system("clear")
    print("\nNúmero de Jogadas: " + Fore.GREEN + str(cont_jogadas) + Fore.RESET)
    print("\n\n\t\t    0   1   2")
    print("\t\t0:  " + tabuleiro[0][0] + " | " + tabuleiro[0][1] + " | " + tabuleiro[0][2])
    print("\t\t   -----------")
    print("\t\t1:  " + tabuleiro[1][0] + " | " + tabuleiro[1][1] + " | " + tabuleiro[1][2])
    print("\t\t   -----------")
    print("\t\t2:  " + tabuleiro[2][0] + " | " + tabuleiro[2][1] + " | " + tabuleiro[2][2])
    
    
instrucao()
tela()

while True:

    cont_jogadas = 1
    jogador = 0

    for i in range(3):
        for j in range(3):
            tabuleiro[i][j] = " "

    while True:
        tela()

        if(jogador%2 == 0):
            print("\nVez do Jogador 1 -->" + Fore.GREEN + " X " + Fore.RESET + "<--\n")
            linha = int(input("Digite a linha que deseja jogar: "))
            coluna = int(input("Digite a coluna que deseja jogar: "))
        else:
            print("\nVez do Jogador 2 -->" + Fore.GREEN + " O " + Fore.RESET + "<--\n")
            linha = int(input("Digite a linha que deseja jogar: "))
            coluna = int(input("Digite a coluna que deseja jogar: "))

        if(linha < 0 or linha > 2 or coluna < 0 or coluna > 2): 
            print("Digite uma posição válida!")
            input()
        elif(tabuleiro[linha][coluna] != " "):
            linha = 0
            coluna = 0
            print("\nEssa posição já está preenchida! Tente novamente \n")
            input()
        else:
            if(jogador % 2 == 0):
                tabuleiro[linha][coluna] = "X"
            else:
                tabuleiro[linha][coluna] = "O"
            jogador += 1
            cont_jogadas += 1
        
        verifica_vencedor()

        if(cont_jogadas > 9):
            break

    tela()

    if(cont_jogadas == 11):
        print("\n\t\t" + Fore.RED + " Fim de Jogo!")
        print("\n\t\t" + Fore.YELLOW + "** PARABÉNS **\n\n\tO JOGADOR > X < É O VENCEDOR!!\n")
    elif(cont_jogadas == 12):
        print("\n\t\t" + Fore.YELLOW + "** PARABÉNS **\n\n\tO JOGADOR > O < É O VENCEDOR!!\n")
    else:
        print("\n\t" + Fore.YELLOW + "** OPS, PARECE QUE DEU VELHA **")

    jogar_novamente = input("\n" + Fore.BLUE + "Deseja jogar novamente? [S/N]" + Fore.RESET + "\n")

    if(jogar_novamente == "N" or jogar_novamente == "n"):
        break
os.system("clear")
print("\n\t\t" + Fore.YELLOW + "** That's All, Folks **\n\n")
