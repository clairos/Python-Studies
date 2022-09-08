# antes estava dando erro "AttributeError: partially initialized module 'json' has no attribute 'loads' (most likely due to a circular import)"
# isso pq nomeei o arquivo json.py entao conflitava na hora de fazer o import
# lembrar de nao nomear os arquivos com nome de alguma biblioteca que for importar
import json

carro_json='{"marca":"renault","modelo":"clio","cor":"prata"}'  # formato de dictionary
carro_dic={
    "marca":"renault",
    "modelo":"clio",
    "cor":"prata"
}

carros=json.loads(carro_json) # converte json para dictionary
carro_json=json.dumps(carro_dic) # converte dictionary para json

print(carros)
print(carros["modelo"])

for k,v in carros.items(): # k for key, v for value
    print(f"{k}: {v}")

print(carro_json)