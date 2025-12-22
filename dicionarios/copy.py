contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2222"},
}
copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

contatos["guilherme@gmail.com"] #>>>{"nome": "Gui"}

print(contatos["guilherme@gmail.com"]) #>>> {"nome": "Guilherme", "telefone": "3333-2222"}

print(copia["guilherme@gmail.com"]) #>>> {"nome": "Gui"}
