import pandas as pd

# ler arquivo CSV básico 

df = pd.read_csv('dados.csv')

# ler arquivo com delimitador de tabulação e coluna de indice

df = pd.read_csv('dados.csv', sep= '\t', index_col= 'ID')

# interpretar valores ausentes e converter colunas para datas

df = pd.read_csv('dados.csv', na_values=['NA', 'n/a'], parse_dates=['Data'])