#}.disjoint                       —> verifica se dois conjuntos NÃO tem			 			  
#                                       	nenhum elemento em comum
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}


print(conjunto_a.isdisjoint(conjunto_b)) #>>> true –  não existe nenhum elemento em comum
print(conjunto_a.isdisjoint(conjunto_c)) #>>> false – existe pelo menos um elemento em comum (1)
