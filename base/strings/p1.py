curso = "Curso de Python" # string pode ser considerado um array


print(curso) # vai imprimir tudo
print(curso[9]) # vai imprimir a letra P
print(curso[9:15]) # delimita um range para imprimir, vai imprimir 'python'

print(curso.strip()) # strip = faz remoção de espaços
print(curso.lower().strip()) # lower = converte tudo para minusculo
print(curso.upper()) # upper = converte tudo para maiusculo
print(curso.replace("Python", "JavaScript")) # replace eh autoexplicativo
a=curso.split(" ") # quebra a string no indicado que vc colocar

print("Tamanho: " + str(len(curso))) # len = length, tamanho de uma lista
print(a[0])