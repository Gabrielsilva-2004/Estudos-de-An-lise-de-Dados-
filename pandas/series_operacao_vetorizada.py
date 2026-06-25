import pandas as pd
# # Um valor pode ser repetido e varios indices
# coluna3 = pd.Series(100, index=["a", "b", "c"]) # index nomeia os indices
# print(coluna3)

# print()

# coluna3["a"] # Com indice sendoo nomes posso acessar pelo nome
# print(coluna3.loc["a"])


# lista = [20, 30, 40]

# dicionario = {
#     "Ana": 20,
#     "Carlos": 25,
#     "Maria": 30
# }

# dados = pd.Series(lista)
# dados2 = pd.Series(dicionario)

# print(dados.iloc[0]) # pegando linha pela posição
# print()
# print(dados2)


# dados3 = pd.Series([20, 30, 40], index=["a", "b", "c"])
# print(dados3)

# idades = pd.Series([21, 22, 25])

# idades_menores_que_23 = idades[idades < 23] 

# print(idades_menores_que_23)

df = pd.DataFrame({
    "nome": ["Ana", "Carlos", "Maria"],
    "idade": [20, 25, 30]
})

# print(df)
import json
with open("pandas/dec.json", "r") as arquivo :
    dados = json.load(arquivo)
print(dados)