#{}.issubset                       —> verifica se um conjunto existe dentro de outro
#	                    				   se sim >>>true // se não >>>false     
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b)) #>>> true – tudo que há no conjunto A, existe no B
print(conjunto_b.issubset(conjunto_a)) #>>> false – nem tudo que há no conjunto B, existe no A