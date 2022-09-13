import json

carros_dictionary = {
    "marca":"renault",
    "modelo":"clio",
    "cor":"prata"
}
# dictionary -> objeto json

carros_list = ["honda", "volkswagen", "ford", "fiat", "chevrolet"]
# list -> array json

carros_tupla = ("honda", "volkswagen", "ford", "fiat", "chevrolet")
# tupla -> array json

carros_json_d = json.dumps(carros_dictionary, indent = 4, separators = (": ", " = "), sort_keys = True)
print(carros_json_d)

carros_json_l = json.dumps(carros_list, indent = 4)
print(carros_json_l)

carros_json_t = json.dumps(carros_tupla)
print(carros_json_t)