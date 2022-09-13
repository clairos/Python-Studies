num1 = num2 = res = 0
lang = "Python" #variavel de escopo global

def lg():
    lang2 = "JS"

    global lang3
    lang3 = "Java"

    print(lang)

lg() # vai imprimir "Python"
#print(lang2) # vai dar erro pois a variavel foi declarada dentro da funcao, nao eh global
print(lang3) # nao vai dar erro pois a variavel foi declarada como global