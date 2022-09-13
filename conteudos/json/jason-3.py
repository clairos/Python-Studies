import json

# {
#     "nome":"Bruno",
#     "time":"aviadores",
#     "vivo":"True",
#     "energia": 100,
#     "mochila":["pederneira","corda","linha","arame"],
#     "aeronaves":[
#         {"tipo":"transporte","habilidade":80},
#         {"tipo":"ataque","habilidade":100},
#         {"tipo":"reconhecimento","habilidade":50}
#     ]
# }

jogador_j = '{"nome":"Bruno","time":"aviadores","vivo":"True","energia": 100,"mochila":["pederneira","corda","linha","arame"],"aeronaves":[{"tipo":"transporte","habilidade":80},{"tipo":"ataque","habilidade":100},{"tipo":"reconhecimento","habilidade":50}]}'

jogador = json.loads(jogador_j)

def linha():
    print("-----------------------")


# itens
for i in jogador.items():
    print(i)
linha()

#chaves
for k in jogador:
    print(k)
linha()

# valores
for v in jogador.values():
    print(v)
linha()

# nome do jogador
print(jogador["nome"]) # qualquer chave vai funcionar nesse caso
linha()

# itens da mochila
for im in jogador["mochila"]:
    print(im)
linha()

# aeronaves
for a in jogador["aeronaves"]:
    print(a)
linha()

# tipos de aeronaves
for a in jogador["aeronaves"]:
    print(a["tipo"]) # funcionaria com "habilidade" também
linha()

# misturar tipo e habilidade
for a in jogador["aeronaves"]:
    print("{} - {}".format(a["tipo"], a["habilidade"]))
linha()