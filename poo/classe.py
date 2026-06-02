"""
Classe e como um molde onde e usado para criar vario objetos
diferentes com o mesmo molde e diferentes comportamentos.
"""
# class Cachorro:
#     pass # vazio 

# rex = Cachorro()
# print(type(rex))

"""

"""

# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome

# p1 = Pessoa("Ana")
# p2 = p1

# p2.nome = "Carlos"

# print(p1.nome)
# print(p2.nome)

"""

p1 = Pessoa("Ana")
p2 = p1 

p1 ──┐
     ├──► objeto Pessoa
p2 ──┘      nome = "Ana"

# qunado faço isso as duas variaveis ficam apontando para o mesmo objeto.

p2.nome = "Carlos" # Quando eu altero apnes um, os dois são alterados

p1 ──┐
     ├──► objeto Pessoa
p2 ──┘      nome = "Carlos"

print(p1.nome)
print(p2.nome)

# Saida:
Carlos
Carlos

Quando eu altero um valor de uma variavel e esse valor e apontado por outras variaveis a mudança será vista em todas.
"""

'''
class cachorro:
	"""
	O self e passado no parametro da função pois após chamar a função o objeto criado e automaticamente passado para o parâmetro self por trás dos panos fica assim
	Cachorro.latir(rex)
	mais e chamado assim
	rex.latir()
	"""
	def latir(self):
		print("Au au")

rex = cachorro()
rex.latir()
'''

# class Cachorro:
#     def latir(self):
#         print("Au au")

# bob = Cachorro()
# bob.latir()

# class Cachorro:
#     def latir(self):
#         print(type(self))

# bob = Cachorro()
# bob.latir()

# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome
    
#     def seu_nome(self): 
#         print(f"Seu nome é {self.nome}")

# gabriel = Pessoa("Gabriel")
# gabriel.seu_nome()

# class Calculadora():
#     def soma(self, a, b):
#         print(a + b)

# soma = Calculadora()
# soma.soma(10, 20)

# class conta:
#     def __init__(self, deve):
#         self.deve = deve

#     def aumento_divida(self, compra):
#         self.deve += compra

# ricardo = conta(100)
# ricardo.aumento_divida(100)

# print(ricardo.deve)

# atividade debug mental diga o que aconteceu linha a linha

# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome

#     def mudar_nome(self, novo_nome): 
#         """
#         Essa função modifica o nome do objeto self.nome atraves do 
#         parametro novo_nome.
#         """
#         self.nome = novo_nome

# p1 = Pessoa("Ana")
# p2 = Pessoa("Carlos")

# p1.mudar_nome("Maria") # Chama a função mudar_nome e passa 
# # o novo valor para que substitruira o atigo valor do atributo
# # self.nome. ou seja p1 aogra tem o nome de Maria

# print(p1.nome)
# print(p2.nome)

# encapsulametno

# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome

# p1 = Pessoa("Ana")

# p1.nome = "José" # isso e uma má pratica

# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome
    
#     def mudar_nome(self, novo_nome):
#         if isinstance(novo_nome, str):
#             self.nome = novo_nome

# p1 = Pessoa("Ana")
# p1.mudar_nome("Maria")

# print(p1.nome)

class Pessoa: 
    def __init__(self, nome):
        self.__nome = nome # o __ duplo underline e uma convenção
# que diz que não se deve mexer nele diretamente ou seja
# não mecher nele fora da classe como p1.__nome = "Maria"