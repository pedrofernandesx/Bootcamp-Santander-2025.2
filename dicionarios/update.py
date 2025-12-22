contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2222"}
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos) #>>> {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "9999-8888"}})
print(contatos) #>>> {