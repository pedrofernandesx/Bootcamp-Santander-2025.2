contato = {'nome': 'Guilherme', 'telefone': '3333-2222'}

contato.setdefault('nome', 'Giovanna')  
print(contato) #>>> {'nome': 'Guilherme', 'telefone': '3333-2222'}

contato.setdefault('idade', 28)  #>>> 28
print(contato) #>>> {'nome': 'Guilherme', 'telefone': '3333-2222', 'idade': 28} 