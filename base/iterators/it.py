carros = ["HRV","Golf","Argo","Focus"]

itCarros = iter(carros)

print(next(itCarros)) # somente percorre a lista para frente
print(next(itCarros))
print(next(itCarros))
print(next(itCarros))
# print(next(itCarros)) # quando chega no final da erro StopIteration

while itCarros:
    try:
        print(next(itCarros)) # facilita pois nao precisa se preocupar com o tamanho da lista
    except StopIteration:
        print("Fim da lista")
        break;