lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy() # Faz uma cópia rasa da lista
print(lista)  # Saída: [1, 'Python', [40, 30, 20]]  
print(id(l2), id(lista))  # IDs diferentes 

l2[0] = 2
print(lista)