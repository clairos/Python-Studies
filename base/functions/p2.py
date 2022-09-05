def somar(*num): # argumento arbitrario
    r=0

    for n in num:
        r += n
    
    print("Resultado: {}".format(r))

somar(10, 5, 3, 7) # pode acrescentar quantas entradas quiser para a funcao retornar

def nome(n="Nome padrão"): # possivel passar um valor default para o parametro
    print("Nome: {}".format(n))

nome() # se nao incluir parametro, vai printar o valor padrao
nome("Clara") # se incluir parametro, vai printar o valor passado ao chamar a funcao