import pandas as pd

serie = pd.Series([10,20,30,40])

print(serie[ serie > 20]) #filtra os valores maiores que 20

print((serie[ serie > 20].sum())) #soma apenas os valores maiores que 20