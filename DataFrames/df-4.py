import pandas as pd


df = pd.DataFrame({
    'Produto' : ['A', 'B', 'C'],
    'Preco' : [100, 200, 300],
    'Quantidade' : [2, 3, 5]
})

# Aqui estou criando uma coluna 'total'
df['Total'] = df['Preco'] * df['Quantidade'] 


# Estatistica descritiva para colunas de valor numérico

# print(df.describe())

#- >  print(df['Preco'].mean())  # média da coluna preco
#- > print(df['Quantidade'].sum())  #Soma da coluna quantidade

# Utilizar o axis=1 para realizar calculos em cada linha

df['Lucro'] = df.apply(lambda row: row['Total'] * 0.2, axis= 1) #calcula o lucrom de cada produto (20% do total)


# filtranfo produtos com preco maior que $150

produtos_caros = df[df['Preco'] > 150]

# somando a quantidade dos produtos filtrados

print(produtos_caros['Quantidade'].sum())