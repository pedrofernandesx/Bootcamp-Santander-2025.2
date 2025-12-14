linguagens = ["python", "js", "c", "java", "csharp"] 

sorted(linguagens, key=lambda x: len(x)) # faz a ordenação pela quantidade de caracteres, lambda é uma função anônima que a cada item da lista retorna o tamanho do item
#>>> ['c', 'js', 'java', 'python', 'csharp']

sorted(linguagens, key=lambda x: len(x), reverse=True) # faz a ordenação pela quantidade de caracteres em ordem reversa
#>>> ['python', 'csharp', 'java', 'js', 'c']
