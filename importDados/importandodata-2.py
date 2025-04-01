import pandas as pd

# Ler uma aba especifica de um arquivo excel

df = pd.read_excel('dados.xlxs', sheet_name= 'Planilha1')

# Ler apenas colunas especificas