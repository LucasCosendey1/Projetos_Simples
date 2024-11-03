#MY SUPER ULTRA MEGA CALCULADORA SIMPLES

#Entrada

resultado = 0
x = 1
y = 1

while(y==1):

    try:

        Calculo = int(input(": Pressione a tecla do tipo de calculo que você deseja fazer:\n"
     "Soma: 1\n"
     "Subtração: 2\n"
     "Multiplicação: 3\n"
     "Divisão: 4\n"
     "Digite o valor aqui: "))
        
        if(Calculo in [1, 2, 3, 4]):
            y=2
    
    except ValueError:
        print()

while(x==1):
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        x = 2  #Se "num1" e "num2" forem float o While será quebrado
    
    except ValueError:
        print("ERRO: insira valores numéricos válidos.")



#processamento e exibição

if(Calculo == 1):
    resultado = num1 + num2
    print("O resultado da soma é ", resultado)

elif(Calculo == 2):
    resultado = num1 - num2
    print("O resultado da subtração ", resultado)

elif(Calculo == 3):
    resultado = num1 * num2
    print("O resultado da multiplicação é ", resultado)

elif(Calculo == 4):
    resultado = num1 / num2
    print("O resultado da divisão é  ", resultado)


