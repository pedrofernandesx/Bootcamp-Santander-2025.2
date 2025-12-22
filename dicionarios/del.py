contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2222"},
	"giovanna@gmail.com": {"nome": "giovanna", "telefone": "3333-1111"},
	"chappie@gmail.com": {"nome": "chappie", "telefone": "3333-3333"},
	"melaine@gmail.com": {"nome": "melaine", "telefone": "3333-4444"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]["telefone"]

print(contatos) #>>> {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'giovanna', 'telefone': '3333-1111'}, 'chappie@gmail.com': {'nome': 'chappie'}, 'melaine@gmail.com': {'nome': 'melaine', 'telefone': '3333-4444'}}
