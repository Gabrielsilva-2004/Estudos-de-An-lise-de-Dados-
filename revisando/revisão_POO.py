
"""
Crie uma classe chamada Livro que:

Receba titulo e autor no __init__.
Armazene esses valores em atributos do objeto.
Tenha um método chamado exibir_livro() que mostre o título e o autor.
"""

# class livro:
#     def __init__(self, titulo, autor):
#         self.titulo = titulo
#         self.autor = autor
    
#     def exibir_livro(self):
#         print(
#             f"O nome do livro é: {self.titulo}"
#             f" e o autor é: {self.autor}"
#             )

# livro1 = livro("O Senhor dos Anéis", "J.R.R. Tolkien")

# livro1.exibir_livro()

"""
Atividade 2 — Métodos alterando o objeto

Crie uma classe chamada ContaBancaria que:

Receba um saldo inicial no construtor.
Tenha um método depositar(valor) que aumente o saldo.
Tenha um método mostrar_saldo() que exiba o saldo atual.

Teste sua classe criando um objeto com saldo inicial de 100 e fazendo um depósito de 50.
"""

# class Conta_Banncaria:
#     def __init__(self, salario):
#         self.salario = salario
    
#     def depositar(self, valor):
#         self.salario += valor

#     def mostra_saldo(self):
#         print(f"Seu saldo é: {self.salario}$")

# jerferson = Conta_Banncaria(100)

# jerferson.depositar(50)
# jerferson.mostra_saldo()

"""
Atividade 3 — Encapsulamento

Crie uma classe chamada Aluno que:

Receba um nome no construtor.
Possua um método mudar_nome(novo_nome).
Antes de alterar o nome, verifique se novo_nome é uma string usando isinstance.
Caso seja válido, altere o nome.
Caso contrário, não faça a alteração.
"""

# class Aluno:
#     def __init__(self, nome):
#         self.nome = nome

#     def mudar_nome(self, novo_nome):
#         if isinstance(novo_nome, str):
#             self.nome = novo_nome

# a1 = Aluno("João")

# a1.mudar_nome("Maria")

# print(a1.nome)