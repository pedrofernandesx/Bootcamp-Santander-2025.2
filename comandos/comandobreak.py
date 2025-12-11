#se o numero for dif de 0 continua, se for par ele exibe o numero, se for impar ele exibe numero, 
# se for 10, ele para

# while True:
   # numero = int(input("Informe um número"))
    
  #  if numero == 10:
 #       break

#    print(numero)

for numero in range(100): #de 0 á 99

        if numero % 2 == 0:
            continue

        print(numero, end=" ")