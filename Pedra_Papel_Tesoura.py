#IMPORT PARA FAZER AS PALAVRAS SEREM ALEATORIAS
import random

#IMPORT PARA LIMPAR O TERMINAL
import os
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#INICIANDO OS CONTADORES DE PONTOS
cont1 = 0
cont2 = 0

print("Vamos umas rodadas de pedra, papel ou tesoura.")
while True:
    
    oponente = ["pedra", "papel", "tesoura"]
    oponente = random.choice(oponente)
    
    opcao = input(f"Suas vitorias: {cont1}\nMinhas vitórias: {cont2}"
                  "\n Para parar de jogar escreva 'sair'. Escreva a sua escolha: ")
    #LIMPANDO O TERMINAL
    limpar_terminal()

        #PARA ENCERRAR O PROGRAMA
    if(opcao == "sair"):
        break

        #VITORIAS DO USUARIO
    elif (opcao == "pedra" and oponente == "tesoura") or (opcao == "papel" and oponente == "pedra") or(opcao == "tesoura" and oponente == "papel"):
        print(f"Você jogou {opcao} e eu {oponente}")
        cont1 += 1
                            
        #VITORIAS DO COMPUTADOR
    elif (opcao == "tesoura" and oponente == "pedra") or (opcao == "pedra" and oponente == "papel") or (opcao == "papel" and oponente == "tesoura"):
        print(f"Você jogou {opcao} e eu {oponente}")
        cont2 += 1
                                
        #EMPATE
    elif(opcao == "tesoura" and oponente == "tesoura") or (opcao == "pedra" and oponente == "pedra") or (opcao == "papel" and oponente == "papel"):
        print("Deu empate, vamos mais uma")
                        
        #SE O USUÁRIO COLOCAR UM VALOR INVALIDO
    else:
        print("Você digitou um valor invalido")

    print("\n")