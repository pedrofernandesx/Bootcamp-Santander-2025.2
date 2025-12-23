def exibir_mensagem():
    print(f"Olá! Esta é uma mensagem exibida por uma função.")   

def exibir_mensagem_2(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

def exibir_mensagem_4 (nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")
exibir_mensagem_4("Júlia")