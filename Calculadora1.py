import tkinter as tk
from tkinter import messagebox


#Entrada
resultado = 0
x = 1
y = 1
def calcular():

    try:

        Calculo = int(ent_calculo.get())
        if(Calculo not in [1, 2, 3, 4]):
            raise ValueError("ERRO: insira valores numéricos válidos.")
        
        num1 = float(ent_num1.get())
        num2 = float(ent_num2.get())
        
#Processamento

        if(Calculo == 1):
            resultado = num1 + num2
            result_label.config(text=f"O resultado da Soma é: {resultado}")

        elif(Calculo == 2):
            resultado = num1 - num2
            result_label.config(text=f"O resultado da Subtração é: {resultado}")

        elif(Calculo == 3):
            resultado = num1 * num2
            result_label.config(text=f"O resultado da Multiplicação é: {resultado}")

        elif(Calculo == 4):
            resultado = num1 / num2
            result_label.config(text=f"O resultado da Divisão é: {resultado}")


    except ValueError:
        print("ERRO: insira valores numéricos válidos.")

#Configuração da janela
janela = tk.Tk()
janela.title("MINHA CALCULADORA")

#Layout dos elementos
tk.Label(janela, text="Escolha o tipo de cálculo:\nSoma: 1\nSubtração: 2\nMultiplicação: 3\nDivisão: 4").grid(row=0, column=0, columnspan=2)
ent_calculo = tk.Entry(janela)
ent_calculo.grid(row=1, column=0, columnspan=2)

tk.Label(janela, text="Digite o primeiro número:").grid(row=2, column=0)
ent_num1 = tk.Entry(janela)
ent_num1.grid(row=2, column=1)

tk.Label(janela, text="Digite o segundo número:").grid(row=3, column=0)
ent_num2 = tk.Entry(janela)
ent_num2.grid(row=3, column=1)

#Botão para realizar o cálculo
calc_button = tk.Button(janela, text="Calcular", command=calcular)
calc_button.grid(row=4, column=0, columnspan=2)

#Exibição do resultado
result_label = tk.Label(janela, text="")
result_label.grid(row=5, column=0, columnspan=2)

#Executa a janela
janela.mainloop()
