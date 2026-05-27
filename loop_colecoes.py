""" for loops
dados = [
    (1, 2, 3),
    (4, 5, 6)
]
# Se os elementos de coleção forem sequenciais e tiverem o
# mesmo tamanho e possível desempacotar direto no loop.
for a, b, c in dados:
    print(a, b, c)
"""

""" pass
numero = 0

if numero == 0:
    pass # pass serve para que uma estrutura de controle 
# como for/if/while vazia não quebre o código então ele basicamente não faz nada
"""

"""range
retorno = range(0, 10) # range retorna um objeto do tipo range e eu posso convertelo para uma coleção
#saida: range(0, 10)
lista = list(retorno)
#saida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# mesmo com valores grande range consome pouca memoria
"""

"""
In [4]: tupla = tuple("Gabriel") # posso converter uma string para tupla

In [5]: tupla
Out[5]: ('G', 'a', 'b', 'r', 'i', 'e', 'l')

# tuplas são imutaveis você não pode alterar o seu valor
# mas se um objeto dentro dela for mutavel ele pode ser
# alterado

In [1]: tupla = (1, 2, 3, [1, 2])
   ...: 
   ...: tupla[3].append(3)

In [2]: tupla
Out[2]: (1, 2, 3, [1, 2, 3])
"""






