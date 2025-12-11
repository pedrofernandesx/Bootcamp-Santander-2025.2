nome = "Guilherme Arthur de Carvalho"
print(nome [0]) #indice 0 é o primeiro caractere
print(nome[-2])  #indice 1 é o segundo caractere
print(nome [:9])  #indice esta ordenando que pare no 8o caractere
print(nome[10:])  #o anterior é o espaço em branco, então ele começa do seguinte até o final
print(nome [10:16])  #substring, quero o inicio e o fim (do 9 ao 15, no caso)
print(nome[10:16:2]) #do 10 ao 16, de 2 em 2
print(nome[:])  #retorna a string inteira
print(nome[::-1])  #cria uma cópia da string de forma invertida
print(nome[::2])  #de 2 em 2, do começo ao fim