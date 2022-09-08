carros=["HRV","Golf","Argo","Focus"]
carros.append("Fit") # append = adiciona item no final da lista
carros.append("Clio") 
carros.append("Fusion") 
carros.remove("HRV") # autoexplicativo

carros.pop() # remove o ultimo elemento

del carros[2] # vai remover o elemento numa posicao especifica

carros.clear() # limpa a lista

carros2=list(carros) # copia a lista

carros2=["Fusca","Brasilia","Celta"]
carros3=carros+carros2 # junta as listas

print(str(len(carros)) + " carros na lista")

print(carros3)