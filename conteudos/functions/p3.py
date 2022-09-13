valores = [1,5,3,2]

def somar(num):
    r = 0

    for n in num:
        r += n

    return r

resposta = somar(valores)
print(f"Resultado da soma: {resposta}") # outro formato de print como o .format