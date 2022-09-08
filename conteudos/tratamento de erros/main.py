x=10

# try e except sao necessarios, else e finally pode utilizar ou nao
try: 
    print(x)
except:
    print("Erro")
else: 
    print("Tudo certo")
finally:
    print("Fim do tratamento")


num = 7
if not type(num) is int: # vai gerar um erro e para a execução do programa
    raise Exception("Somente números perimitidos") 
else:
    print(num)