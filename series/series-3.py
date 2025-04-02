import pandas as pd

serie = pd.Series([10,20,30,40])

print(serie + 5) # adiciona 5 a todos os elementos da lista


print( serie * 2) # Multiplica todos os elementos por 2


# ----------------------------------------------------------

print(serie.sum()) # soma total dos componentes (elementos)

print(serie.mean()) #pega a média dos elementos 

print(serie.median()) # pega a mediana dos elementos da lista

print(serie.std()) # Desvio padrao dos elementos

print(serie.min()) # pega o valor minimo dos elementos

print(serie.max()) #pega o valor máximo dos elementos 