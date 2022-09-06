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

jogador_j='{"nome":"Bruno","time":"aviadores","vivo":"True","energia": 100,"mochila":["pederneira","corda","linha","arame"],"aeronaves":[{"tipo":"transporte","habilidade":80},{"tipo":"ataque","habilidade":100},{"tipo":"reconhecimento","habilidade":50}]}'

jogador=json.loads(jogador_j)

# itens
for i in jogador.items():
    print(i)

#chaves
for k in jogador:
    print(k)

# valores
for v in jogador.values():
    print(v)

# nome do jogador
print(jogador["nome"]) # qualquer chave vai funcionar nesse caso

# itens da mochila
for im in jogador["mochila"]:
    print(im)

# aeronaves
for a in jogador["aeronaves"]:
    print(a)

# tipos de aeronaves
for a in jogador["aeronaves"]:
    print(a["tipo"]) # funcionaria com "habilidade" também

# misturar tipo e habilidade
for a in jogador["aeronaves"]:
    print("{} - {}".format(a["tipo"], a["habilidade"]))