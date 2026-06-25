# seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# for a, b, c in seq:
#     print(f"a= {a}, b= {b}, c= {c}")

"""
Listas são muito usadas em processamento de dados paara 
tranformar iteradores em listas reais
"""
# a = range(0, 100)

# lista = list(a)
# print(lista)

# lista = [1, 2, 3]

# lista.insert(0, "inicio")

# print(lista)

# a = [7, 2, 5, 1, 3]
# a.sort() # método sort ordena a lista.

# print(a)

# b = ["saw", "small", "He", "foxes", "six"]

# b.sort(key=len) # O parâmetro key recebe uma função que pode ser utilizada na ordeanação.)
# print(b) # nesse exemplo ele ordenou pelo tamanho das palavras.


# dicionario = {"a": 1, "b": 2, "c": 3}

# for chave, valor in dicionario.items():
#     print(chave, valor)

# lista_key = [1, 2, 3]
# lista_value = ["um", "dois", "três"]
# valores_extras = [4, 5, 6]
# dicionario = {}

# print(list(zip(lista_key, lista_value, valores_extras))) # zip é um iterador que junta os elementos de várias listas em tuplas.

# for chave, valor in zip(lista_key, lista_value):
#     dicionario[chave] = valor

# print(dicionario)

# nomes = ["Ana", "Carlos", "Maria"]
# idades = [20, 25, 30]

# dicionario = dict(zip(nomes, idades))

# print(dicionario)

# retorno_get = nomes.get("Ana", 0)

# print(retorno_get)