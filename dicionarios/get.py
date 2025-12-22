contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "9999-9999"}
}
contatos["chave"] #>>> KeyError: 'chave'

contatos.get("chave") #>>> None
contatos.get("chave", "{}") #>>> '{}'
contatos.get("guilherme@gmail.com", {}) #>>> {'nome': 'Guilherme', 'telefone': '9999-9999'}
