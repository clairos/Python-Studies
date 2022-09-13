import os
import shutil

caminho_original = 'C:\\Users\\clara.brusa\\Pictures\\pasta_teste'
caminho_novo = 'C:\\Users\\clara.brusa\\Pictures\\pasta_nova'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

# for root, dirs, files in os.walk(caminho_original):
for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        # print(old_file_path)
        # print(new_file_path)

        # shutil.move(old_file_path, new_file_path)   # move também serve para renomear os arquivos
        # print(f'Arquivo {file} movido com sucesso!')

        # if '.txt' in file:
        #     shutil.copy(old_file_path, new_file_path)
        #     print(f'Arquivo {file} copiado com sucesso!') 

        if '.txt' in file:
            os.remove(new_file_path)
            print(f'Arquivo {file} foi apagado.')
