import json

with open('C:/Users/clara.brusa/Desktop/Python/base/json/jogador.json') as j: # para abrir um arquivo externo com extensao .json
    jogador=json.load(j)

# itens
for i in jogador.items():
    print(i)
#etc

# os prints do arquivo jason-3.py vao funcionar igualmente