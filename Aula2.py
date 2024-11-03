from datetime import datetime, date
from matplotlib import pyplot as plt
import numpy as np


capital = float(input("Digite o capital investido: "))
frequencia = input("Digite a frequência do período (Y, N, D): ")
inicio = input("Digite a data inicial maior que 1995/01/01 no formato YYYY/MM/DD: ")
final = input("Digite a data final no seguinte formato YYYY/MM/DD: ")


data_inicial = datetime.strptime(inicio, "%/%m/%d").date()
data_final = datetime.strptime(inicio, "%/%m/%d").date()

data_inicial


taxa_selic = sgs.get({"selic": 11})


