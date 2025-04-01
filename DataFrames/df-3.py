import pandas as pd


df = pd.DataFrame({
    'Produto' : ['A', 'B', 'C'],
    'Preco' : [100, 200, 300],
    'Quantidade' : [2, 3, 5]
})

# Aqui estou criando uma coluna 'total'
df['Total'] = df['Preco'] * df['Quantidade'] 


# Estatistica descritiva para colunas de valor numérico

print(df.describe())

print(df['Preco'].mean())  # média da coluna preco
print(df['Quantidade'].sum())  #Soma da coluna quantidade
