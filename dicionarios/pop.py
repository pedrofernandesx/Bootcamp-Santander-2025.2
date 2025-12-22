contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2222"}
}
resultado = contatos.pop("guilherme@gmail.com") #>>> {'nome': 'Guilherme', 'telefone': '3333-2222'}
print(resultado) #>>> {'nome': 'Guilherme', 'telefone': '3333-2222'}
# print(contatos) #>>> {}

resultado = contatos.pop("guilherme@gmail.com", "não encontrado") #>>> 'não encontrado'
print(resultado) #>>> {}