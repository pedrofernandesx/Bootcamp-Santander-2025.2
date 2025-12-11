MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade.")
else: 
    print("Vcê é menor de idade.")

if idade >= MAIOR_IDADE:
    print("Você é maior de idade e pode começar o processo da sua CHN.")

elif idade == IDADE_ESPECIAL: 
    print("Você pode ter aulas mas não pode dirigir.")
    
else:
        print("Você pode ter aulas de direção teóricas, mas não pode dirigir.")