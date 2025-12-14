linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()

print(linguagens) #>>>['csharp', 'java', 'c', 'js', 'python']

#Ordem reversa:

linguagens.sort(reverse=True)
#>>> ['python', 'js', 'java', 'csharp', 'c']

#Ordenar por tamanho da palavra:
linguagens.sort(key=lambda x: len(x)) # faz a ordenação pela quantidade de caracteres, lambda é uma função anônima que a cada item da lista retorna o tamanho do item
#>>> ['c', 'js', 'java', 'python', 'csharp'] -- no caso de python, tem 6 caracteres, csharp 6 caracteres, mas python vem antes de csharp por ordem alfabética

#Tamanho + reverso:
linguagens.sort(key=lambda x: len(x), reverse=True) # faz a ordenação pela quantidade de caracteres em ordem reversa
#>>> ['python', 'csharp', 'java', 'js', 'c'] -- no caso de python, tem 6 caracteres, csharp 6 caracteres, mas python vem antes de csharp por ordem de tamanho o sort começa da esquerda para a direita