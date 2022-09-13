import re

texto = "Curso de Python para desenvolvimento para a bolsa do SETI"

res = re.split(" ", texto)

for i in res:
    print(i)
