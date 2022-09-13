curso = "Curso de Python"

res = "Python" in curso
print(res)
res = "Python" not in curso
print(res)

cidade = "Chapecó"
dia = 2
mes = "Setembro"
ano = 2022
data = "{}, {} de {} de {}\n\"{}\"" 
# \n quebra de linha 
# \" aspas duplas
# \' aspas simples
# \t tab
# \r retorno
# \b backspace

print(data.format(cidade, dia, mes, ano, curso))