contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2222"},
	"giovanna@gmail.com": {"nome": "giovanna", "telefone": "3333-1111"},
	"chappie@gmail.com": {"nome": "chappie", "telefone": "3333-3333"},
	"melaine@gmail.com": {"nome": "melaine", "telefone": "3333-4444"},
}


resultado = "guilherme@gmail.com" in contatos  #>>> True
print(resultado)

"megui@gmail.com" in contatos  #>>> False
print(resultado)

"idade" in contatos["guilherme@gmail.com"]  #>>> False
print(resultado)

"telefone" in contatos["giovanna@gmail.com"]  #>>> True
print(resultado)