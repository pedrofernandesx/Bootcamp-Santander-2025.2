contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2222"}
}

contatos.popitem() #>>> ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2222'})
resultado = contatos.popitem() #erro se o dicionário estiver vazio