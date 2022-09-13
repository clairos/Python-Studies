import urllib.request # para coletar informacao de paginas online

pagina = urllib.request.urlopen('http://127.0.0.1:5500/conteudos/urllib/cursopython.html')
texto = pagina.read().decode('utf-8')

# dado=texto[0:15]

produto_pos_ini = texto.find('Mouse')
produto_pos_fim = produto_pos_ini + 5

# preco=texto[produto_pos_ini+26:produto_pos_ini+26+7]

qtde_pos_ini = produto_pos_ini + 14
qtde_pos_fim = qtde_pos_ini + 3

preco_pos_ini = qtde_pos_ini + 12
preco_pos_fim = preco_pos_ini + 7


produto = texto[produto_pos_ini : produto_pos_fim]
qtde = texto[qtde_pos_ini : qtde_pos_fim]
preco = texto[preco_pos_ini : preco_pos_fim]

# print(dado)

print(f"Produto....: {produto}")
print(f"Quantidade.: {qtde}")
print(f"Preço......: {preco}")