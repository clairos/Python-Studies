a=int(input("Insira um número: "))
b=int(input("Insira outro número: "))

def somar(a, b):
    r=a+b
    print("Resultado: {} + {} = {}".format(a,b,r))

def subtrair(a, b):
    r=a-b
    print("Resultado: {} - {} = {}".format(a,b,r))

def multiplicar(a, b):
    r=a*b
    print("Resultado: {} * {} = {}".format(a,b,r))

def dividir(a, b):
    r=a/b
    print("Resultado: {} / {} = {}".format(a,b,r))

op=input("Digite a operação desejada (Ex: +, -, *, /): ")

if op=="+":
    somar(a,b)
elif op=="-":
    subtrair(a,b)
elif op=="*":
    multiplicar(a,b)
elif op=="/":
    dividir(a,b)
else:
    print("Operação inválida")
