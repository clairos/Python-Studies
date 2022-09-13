import urllib.request 

pagina = urllib.request.urlopen('http://127.0.0.1:5500/conteudos/urllib/cursopython.html')
texto = pagina.read().decode('utf-8')

produto = input('Digite o produto: ')
produto_pos = texto.find(produto)
produto_txt = texto[produto_pos: 1000]
preco_pos = produto_txt.find('R$')
preco = texto[produto_pos + preco_pos: produto_pos + preco_pos + 7]

if produto_pos > -1:
    print(f"Produto.: {produto}")
    print(f"Preço...: {preco}")
else:
    print("Produto não encontrado")
