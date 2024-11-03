import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        escolha = var.get()

        if escolha == 1:  # Adição
            resultado = num1 + num2
            messagebox.showinfo("Resultado", f"{num1} + {num2} = {resultado}")

        elif escolha == 2:  # Subtração
            resultado = num1 - num2
            messagebox.showinfo("Resultado", f"{num1} - {num2} = {resultado}")

        elif escolha == 3:  # Multiplicação
            resultado = num1 * num2
            messagebox.showinfo("Resultado", f"{num1} * {num2} = {resultado}")

        elif escolha == 4:  # Divisão
            if num2 != 0:
                resultado = num1 / num2
                messagebox.showinfo("Resultado", f"{num1} / {num2} = {resultado}")
            else:
                messagebox.showerror("Erro", "Divisão por zero não é permitida.")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

# Cria a janela principal
root = tk.Tk()
root.title("Calculadora Simples")

# Cria e posiciona os widgets
tk.Label(root, text="Primeiro Número:").grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

tk.Label(root, text="Segundo Número:").grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

var = tk.IntVar()
tk.Radiobutton(root, text="Adição", variable=var, value=1).grid(row=2, column=0, sticky='w')
tk.Radiobutton(root, text="Subtração", variable=var, value=2).grid(row=3, column=0, sticky='w')
tk.Radiobutton(root, text="Multiplicação", variable=var, value=3).grid(row=4, column=0, sticky='w')
tk.Radiobutton(root, text="Divisão", variable=var, value=4).grid(row=5, column=0, sticky='w')

tk.Button(root, text="Calcular", command=calcular).grid(row=6, columnspan=2)

# Inicia a interface gráfica
root.mainloop()
