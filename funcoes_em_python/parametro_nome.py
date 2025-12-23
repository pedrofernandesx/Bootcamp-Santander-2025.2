def criar_carro(modelo, ano, placa, marca,*, motor, combustivel):
    print(
        f"Modelo: {modelo} | Ano: {ano} | Placa: {placa} | "
        f"Marca: {marca} | Motor: {motor} | Combustível: {combustivel}"
    )

criar_carro(
    "Palio",
    1999,
    "ABC-1234",
    marca="Fiat",
    motor="1.0",
    combustivel="Gasolina"
)

print("Carro adicionado com sucesso!")