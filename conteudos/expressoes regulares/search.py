import re

texto = "Curso de Python para desenvolvimento para a bolsa do SETI"

res = re.search("Curso", texto)

if (res != None):
    pi = res.start()
    pf = res.end()

    tam = pf - pi

    print(pi)
    print(pf)
    print(tam)
else:
    print("Não encontrado")
