nome = "guilherme"

print(nome.upper())  # Converte para maiúsculas
print(nome.lower())  # Converte para minúsculas
print(nome.title())  # Converte para formato título

texto = "   Olá, Mundo!   "
print(texto.strip() + ".")  # Remove espaços em branco no início e no fim da string e printa a string com um ponto no final
print(texto.lstrip() + ".") # Remove espaços em branco no início da string ""
print(texto.rstrip() + ".") # Remove espaços em branco no fim da string ""

menu = "Python"

print("####" + "Python" + "####")  # Exibe a string com # antes e depois
print(menu.center(14)) # Centraliza a string em um campo de 14 caracteres
print(menu.center(14, "#")) # Centraliza a string em um campo de 14 caracteres, preenchendo com #

for letra in menu:          
    print(letra, end="-")  # Printa cada letra da string (menu) seguida de um hífen
print()  # Apenas para pular uma linha no final do loop acima

# Mas para ser mais prático, podemos usar o join:

print("-".join(menu))  # Adiciona um hífen entre cada caractere da string 