nome = "teste.txt"
# f = open('C:/Users/clara.brusa/Desktop/Python/base/arquivos/' + nome, "wt")
f = open('C:/Users/clara.brusa/Desktop/Python/base/arquivos/' + nome, "r")
# r - read
# a - append
# w - write
# x - create
# t - texto
# b - binario

# f.read()
# print(f.read())
# print(f.readline())
for l in f:
    print(l)

# txt = input("Digite um texto: ")
# f.write(txt + "\n")

f.close()