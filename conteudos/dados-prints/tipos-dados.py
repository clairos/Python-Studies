x = 1 #int
x = "Python" #string
x = 15.6 #float
x = False #boolean

n1 = 5
n2 = 2
x = complex(n1, n2)
x = ["Carro", "Aviao", "Navio"] # list / array -> valores podem ser alterados
x[0] = "Onibus" # alterado o valor na posicao 0 da lista

x = ("Carro", "Aviao", "Navio", 1, 58.3, True) # tuple -> valores nao podem ser alterados

x = range(0,100,1) # cria automaticamente uma lista

x = { #dict 
    "languague": "Python",
    "level": "easy",
    "name": "Clara"
}

x = {1,3,4,5,7,1,4,5} #set -> nao imprime valores repetidos
x = frozenset({1,3,4,5,7,1,4,5}) # set, porem nao permite alteração

print("Valor: " + str(x)) # str() converte para string
print("Valor: " + str(x[0]))
print("Valor: " + x["languague"])
print("Tipo: " + str(type(x)))

print(x.real)
print(x.imag)