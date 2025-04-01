import pandas as pd

# ler arquivo CSV básico 

df = pd.read_csv('Ecommerce_Consumer_Behavior_Analysis_Data.csv')

# ler arquivo com delimitador de tabulação e coluna de indice

df = pd.read_csv('Ecommerce_Consumer_Behavior_Analysis_Data.csv', index_col= 'Customer_ID')
print(df)

# interpretar valores ausentes e converter colunas para datas

# df = pd.read_csv('Ecommerce_Consumer_Behavior_Analysis_Data.csv', na_values=['NA', 'n/a'], parse_dates=['Data'])