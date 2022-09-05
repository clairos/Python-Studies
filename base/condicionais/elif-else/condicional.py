import os
os.system('cls') # windows
# os.system('clear') # linux

res=0

a=int(input("Digite um valor: "))
b=int(input("Digite outro valor: "))
op=input("Digite um Operador: ")

if "+" in op:
    res=a+b

elif "-" in op: # elif = else + if
    res=a-b

elif "*" in op:
    res=a*b

elif "/" in op:
    res=a/b

else:
    print("Operador Inválido")

print(str(a) + op + str(b) + " = " + str(res))


clima="chuva"; dinheiro=299; lugar=""

if clima=="sol" or (dinheiro>300 and dinheiro <500):
    lugar="clube"
else:
    lugar="cinema"

print("Vou ao " + lugar)

# and = tudo tem que ser True para retornar True
# or = apenas um tem que ser True para retornar False