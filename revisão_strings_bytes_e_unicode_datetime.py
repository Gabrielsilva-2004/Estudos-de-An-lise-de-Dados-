'''
c = """
Aspas tiriplas permite fazer varias linhas
onde automaticamente quando você da um enter
ele cria um quebra de linha na saida do terminal
"""

print(c.count("\n")) # count conta quantos caracteres passado no parametro tem

'''

#------------

""" ipython
Strings em python são tipos imutaveis mas e possível pegar
uma já existente e criar um nova em cima da que já existe.


In [1]: a = "Meu nome e gabriel"

In [2]: b = a.replace("gabriel", "José")
"""
"""
strings são um sequencia de caracteres unicode, posso 
pegar uma string e transformar em um dicionario
"""

#-------------

"""
tipo byte
In [12]: b"ola" # representado por um b"".
Out[12]: b'ola'

In [13]: b'olá'
  Cell In[13], line 1
    b'olá'
    ^
SyntaxError: bytes can only contain ASCII literal 
characters

O tipo byte só reconhece caracteres ASCII caso contrario 
ele quebra. O tipo byte são bytes literais

In [14]: a = "Olá".encode("utf-8") # encode converteu o 
Olá para o tipo byte usando o método de códificação UTF-8

In [15]: a
Out[15]: b'Ol\xc3\xa1'


In [16]: b = a.decode("utf-8") # o decode fez o inverso
pegou o tipo byte e converteu para unicode

In [17]: b
Out[17]: 'Olá'

"""

#--------------

"""
In [2]: b = bool(0) # Zero convertido em bool vira False
pois 0 zero e um valor em python que equivale a False

In [3]: b
Out[3]: False

In [4]: a = bool(1)# qualquer valor no python que não seja zero
ou null será equivalente a a True

In [5]: a
Out[5]: True 
"""
#--------------
"""
from datetime import datetime, date, time

data_hora = datetime(2010, 8, 20, 9, 11, 30)

print(data_hora.date())
print(data_hora.time())
print(data_hora.day)
print(data_hora.month)
print()
print(data_hora)

print(data_hora.strftime("%d-%m-%y %Hh:%M"))
"""
