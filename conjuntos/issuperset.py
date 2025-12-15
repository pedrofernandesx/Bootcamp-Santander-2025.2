#{}.issuperset                       —> verifica se um conjunto contém todos os 							   
#                                        elementos do outro  conjunto.
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}



print(conjunto_a.issuperset(conjunto_b)) #>>> false –  o elemento de B não está em A 
print(conjunto_b.issuperset(conjunto_a)) #>>> true – existem elementos de A em B