import re

texto="Curso de Python para desenvolvimento para a bolsa do SETI"

res=re.sub("\s","-",texto)
res=re.sub(",",".", texto)

print(res)