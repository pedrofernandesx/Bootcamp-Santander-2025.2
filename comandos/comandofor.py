texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# EXEMPLO USANDO ITERÁVEL
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
# o FOR    separa o texto em > letras e verifica se cada letra é uma >vogal    

#exemplo USANDO bult-in range

for numero in range(1, 11):
    print(numero, end=" ")

