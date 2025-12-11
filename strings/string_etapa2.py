nome = "Guilherme"
idade = 28
profissao = "programador"
linguagem = "python"
saldo = 45.435

dados = {"nome": nome, "idade": idade} # dicionário

print("nome: %s idade: %d" % (nome, idade)) # antigo

print("nome: {} idade: {}".format(nome, idade)) # mais moderno

print("nome: {1} idade: {0}".format(idade, nome)) # usando índices
print("nome: {1} idade: {0} Nome {1} {1}".format(idade, nome)) # repetindo valores

print("nome: {nome} idade: {idade}".format(nome = nome, idade = idade)) # usando nomes
print("nome: {name} idade: {age} {name} {name} {age}".format(age = idade, name = nome)) # repetindo valores com nomes
print("nome: {nome} idade: {idade}".format(**dados)) # desempacotando dicionário

print(f"nome: {nome} idade: {idade}") # f-strings (mais moderno e recomendado)
# print(f"nome: {nome} idade: {idade} saldo:{saldo}") # f-string com float
print(f"nome: {nome} idade: {idade} saldo:{saldo:10.2f}") # f-string com float formatado (dá 10 espaços e mostra 2 casas decimais)
