import os
import time


def escrever(word, next=True):
    for char in word:
        print(char, end="")
        time.sleep(0.05)
    
    if next:
        print()


def criar_pasta(diretorio, client_name):
    caminho = os.path.join(diretorio, client_name)
    os.makedirs(caminho, exist_ok=True)
    time.sleep(1)
    escrever("Criação da pasta foi um sucesso!!!")


def criar_arquivo(diretorio, client_name):
    caminho = os.path.join(diretorio, client_name, client_name + ".cdr")
    with open(caminho, "w") as arquivo:
        pass
    time.sleep(1)
    escrever("Criação da arquivo foi um sucesso!!!")



client_name = input(escrever("Name Client: "))


if os.path.exists("config.txt"):
    escrever("Arquivo de pré-configuração encontrado!!!")
    time.sleep(1)
    escrever("Analizando dados...")
    time.sleep(1)
    
    with open("config.txt", "r") as config_file:
        config_data = config_file.read()
        escrever("Configuration loaded:", config_data)
        diretorio = config_data
        escrever("Análise completa!!!")
        time.sleep(1)
 
else:
    escrever("Arquivo de pré-configuração não encontrado.")
    time.sleep(1)
    
    diretorio = input(escrever("Directory: "))  # Exemplo: /storage/emulated/0/Documents
    
    with open("config.txt", "w") as config_file:
        config_file.write(diretorio)
        escrever("Salvando pré-configuração")
        time.sleep(1)
        escrever("Arquivo config.txt salvo!!!")

    
# Criar pasta e arquivo
criar_pasta(diretorio, client_name)
criar_arquivo(diretorio, client_name)
    
    
