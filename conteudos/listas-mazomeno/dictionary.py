# chave/key - valor/value
carro = {
    "Fabricante": "Renault",
    "Modelo": "Clio",
    "Ano": "2012",
    "Cor": "Prata"
}

carro["Cambio"]="Manual" # adiciona novo
carro.pop("Cambio") # remove

fab=carro["Fabricante"] # fab=carro.get("Fabricante")

carro["Cor"]="Preto"

print("Tamanho do Dictionary: " + str(len(carro)))

if "Modelo" in carro:
    print("SIM, modelo é uma chave \n")

for c,v in carro.items():
    # print(x) # imprime a chave
    # print(carro[x]) # imprime valor
    print(c + ": " + v)

