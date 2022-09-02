a=int(input("Insira um número: "))
b=int(input("Insira outro número: "))

def somar():
    r=a+b
    print("Resultado: {}".format(r))

def subtrair():
    r=a-b
    print("Resultado: {}".format(r))

def multiplicar():
    r=a*b
    print("Resultado: {}".format(r))

def dividir():
    r=a/b
    print("Resultado: {}".format(r))

op=input("Digite a operação desejada (Ex: +, -, *, /): ")

if "+" in op:
    somar()
elif "-" in op:
    subtrair()
elif "*" in op:
    multiplicar()
elif "/" in op:
    dividir()
