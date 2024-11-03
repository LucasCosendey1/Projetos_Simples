import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import mplcyberpunk
import win32com.client as win32  # Importação correta

# Baixar dados do ticker
tickers = ["BBDC4.SA"]
D_mercado = yf.download(tickers, period="6mo")  

# Especificar coluna
D_mercado = D_mercado["Adj Close"]
print(D_mercado = D_mercado.to_frame())

# Tratamento de coluna
D_mercado.columns = ["Bradesco"]
plt.style.use("cyberpunk")
plt.plot(D_mercado["Bradesco"])

# Título do gráfico
plt.title("Bradesco")

# Salvar o gráfico no PC com a extensão correta
plt.savefig("Bradesco.png")

# Exibir o gráfico
plt.show()

# Exibir os dados
print(D_mercado)










