import  os
from pathlib import Path


# Função para criar uma pasta
def criar_pasta(nome_cliente, diretorio):
    caminho = Path(diretorio) / nome_cliente
        
    if not os.path.exists(caminho):
        caminho.mkdir(exist_ok=True)
        # print("Pasta criada com sucesso")
        return True
    
    else:
        # print("Pasta já existe")
        return False


# Função para criar um arquivo
def criar_arquivo(nome_cliente, diretorio, ext):
    # print(nome_cliente)
    client = nome_cliente
    diretory = diretorio
    caminho = Path(diretory) / client / (client + str(ext))
    if not os.path.exists(caminho):
        path = Path(caminho)
        path.touch()
        
        # Retornar uma confirmação sobre a criação do arquivo
        # print("Arquivo criado com sucesso")
        return True
    
    else:
        # print("Arquivo já existe")
        return False


def run(name, dir_file, ext, only_dir=False):
    name = name.strip()
    response = False
    
    try:
        if only_dir:
            if criar_pasta(name, dir_file): response = True
            
        else:
            if criar_pasta(name, dir_file) and criar_arquivo(name, dir_file, ext): response = True
        
        return response
    
    except: return response
    # finally: print(response)
