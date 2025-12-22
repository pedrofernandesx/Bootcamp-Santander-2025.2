#A forma mais comum para percorrer os dados de um dicionário é utilizando comando for.

contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2222"},
	"giovanna@gmail.com": {"nome": "giovanna", "telefone": "3333-1111"},
	"chappie@gmail.com": {"nome": "chappie", "telefone": "3333-3333"},
	"melaine@gmail.com": {"nome": "melaine", "telefone": "3333-4444"},
}

print(contatos["giovanna@gmail.com"]["telefone"]) # >>> "3333-1111"

extra = contatos["melaine@gmail.com"]


#for chave in contatos:
#	print(chave, contatos[chave])

for chave, valor in contatos.items():
	print(chave, valor)