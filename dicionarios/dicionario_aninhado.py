
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2222"},
	"giovanna@gmail.com": {"nome": "giovanna", "telefone": "3333-1111"},
	"chappie@gmail.com": {"nome": "chappie", "telefone": "3333-3333"},
	"melaine@gmail.com": {"nome": "melaine", "telefone": "3333-4444"}
}

print(contatos["giovanna@gmail.com"]["telefone"]) # >>> "3333-1111"

extra = contatos["melaine@gmail.com"]

print(extra)