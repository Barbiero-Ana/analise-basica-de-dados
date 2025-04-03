import pandas as pd


df = pd.read_csv('Ecommerce_Consumer_Behavior_Analysis_Data.csv')

#abrindo e acessando o arv csv
column_names = df.columns
print(column_names)

#Qual o publico alvo do ecommerce?


def qtd_compra():

    while True:
        print(f'1 - Ver a quantia de pessoas que compram\n2 - ')
        # ao clicar em um perguntar se deseja filtrar por genero, caso nao apenas mostrar a quantidade total

        decisao = int(input(f'Digite qual opção você deseja: '))

        if decisao == 1:
            try:
                op = int(input('Deseja filtrar a busca de quantidade?\n1 - Sim\n2 - Não'))
                if op == 1:
                    #inserir função de busca (ainda vou criar este caramba)
                    print()
                else:
                    print()
                    # colocar código de ver apenas a quantidade total
            except:
                print()

# quantidade de cada gênero

print(f'\nQuantidade de generos que compram no ecommerce:\n')
print(df['Gender'].value_counts())


print(f'{'=' * 70}' )

# Porcentagem de cada genero?
print(f'\nPorcentagem de cada genero:\n')
print(df['Gender'].value_counts(normalize= True) * 100)

print(f'{'=' * 70}' )
#Quantos solteiros estao presentes no arquivo?

print(f'\nQuantidade de pessoas solteiras que compram no ecommerce: {df['Marital_Status'].value_counts().get('Single', 0)}\n')

print(f'{'=' * 70}' )

# Qual a idade média dos clientes do ecommerce?
print(f'\nA idade média dos clientes que compram no ecommerce é de: {df['Age'].mean():.2f}\n')

# Qual a idade média por nivel de renda? 
print(f'Idade média por nivel de renda: {df.groupby('Income_Level')['Age'].mean().apply(lambda x: f'{x:.2f}')}\n') # essa funcao lambda ta formatando o valor para duas casas decimais, já que o simples :.2f nao funciona com series de forma direta

print(f'{'=' * 70}' )

# Qual a idade média por genero?
print(f'\nA idade média por genero é:\n{df.groupby('Gender')['Age'].mean().apply(lambda x: f'{x:.2f}' )}\n')

# Qual a proporção de clientes por nivel de renda (baixa, media, alta)

