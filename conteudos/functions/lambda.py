soma=lambda a,b:a+b # funcao anonima, nao precisa de nome nem de return
mul=lambda a,b,c:(a+b)*c

print(soma(2,5))
print(mul(2,5,3))

print((lambda a,b:a-b)(3,2)) # desse jeito nao precisa salvar em nenhuma variavel

r=lambda x,func:x+func(x) # utiliza uma funcao como parametro
res=r(2, lambda x:x*x) # utiliza outra lambda como parametro
print(res)