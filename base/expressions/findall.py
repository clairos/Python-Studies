import re # RegEx 

texto="Curso de Python para desenvolvimento da bolsa no SETI"

# res=re.findall("o", texto)
pesq=input("Pesquisar: ")
res=re.findall(pesq, texto)

qtde=len(res)

print(f"Qtde: {qtde}")
for q in res:
    print(q)

# print(len(res))
