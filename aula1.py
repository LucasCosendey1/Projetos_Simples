import tkinter as tk
from tkinter import messagebox

# Função para capturar os valores de num1, num2 e Calculo e realizar a operação
def calcular():
    try:
        Calculo = int(entry_calculo.get())
        if Calculo not in [1, 2, 3, 4]:
            raise ValueError("Operação inválida")
        
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if Calculo == 1:
            resultado = num1 + num2
            result_label.config(text=f"O resultado da soma é: {resultado}")
        elif Calculo == 2:
            resultado = num1 - num2
            result_label.config(text=f"O resultado da subtração é: {resultado}")
        elif Calculo == 3:
            resultado = num1 * num2
            result_label.config(text=f"O resultado da multiplicação é: {resultado}")
        elif Calculo == 4:
            if num2 == 0:
                messagebox.showerror("Erro", "Divisão por zero não é permitida.")
                return
            resultado = num1 / num2
            result_label.config(text=f"O resultado da divisão é: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para o cálculo.")

# Configuração da janela
root = tk.Tk()
root.title("MY SUPER ULTRA MEGA CALCULADORA SIMPLES")

# Layout dos elementos
tk.Label(root, text="Escolha o tipo de cálculo:\nSoma: 1\nSubtração: 2\nMultiplicação: 3\nDivisão: 4").grid(row=0, column=0, columnspan=2)
entry_calculo = tk.Entry(root)
entry_calculo.grid(row=1, column=0, columnspan=2)

tk.Label(root, text="Digite o primeiro número:").grid(row=2, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=2, column=1)

tk.Label(root, text="Digite o segundo número:").grid(row=3, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=3, column=1)

# Botão para realizar o cálculo
calc_button = tk.Button(root, text="Calcular", command=calcular)
calc_button.grid(row=4, column=0, columnspan=2)

# Exibição do resultado
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

# Executa a janela
root.mainloop()
