import os, json, time, platform
import time
import platform


# Função para criar o arquivo config caso não esteja criado
def write_json(argument_config):
    with open('config.json', 'w', encoding="utf-8") as arq:
        json.dump(argument_config, arq, indent=4, ensure_ascii=False)
        
        
# Função para ler o arquivo config.json
def load_json(arq):
    with open(arq, 'r', encoding="utf-8") as arq:
        data = json.load(arq)
        return data["diretory"]


# Função para limpar a tela do console
def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# Função para escrever uma string lentamente no console
def escrever(word, next=True):
    for char in word:
        print(char, end="", flush=True)
        time.sleep(0.005)
    
    if next:
        print()
    return ""


# Função para criar uma pasta
def criar_pasta(diretorio, nome_cliente):
    caminho = os.path.join(diretorio, nome_cliente)
    os.makedirs(caminho, exist_ok=True)
    escrever("Criação da pasta foi um sucesso!!!")


# Função para criar um arquivo
def criar_arquivo(diretorio, nome_cliente):
    caminho = os.path.join(diretorio, nome_cliente, nome_cliente + ".cdr")
    with open(caminho, "w") as arquivo:
        pass
    escrever("Criação do arquivo foi um sucesso!!!")



# Solicita o nome do cliente
nome_cliente = input(escrever("Nome do Cliente: "))
clear_console()



# Verifica se o arquivo de configuração existe
if os.path.exists("config.json"):
    escrever("Arquivo de pré-configuração encontrado!!!")
    escrever("Analisando dados...")
    diretorio = load_json("config.json")
    clear_console()
    
else:
    escrever("Arquivo de pré-configuração não encontrado.")
    diretorio = input(escrever("Diretório: "))  # Exemplo: /storage/emulated/0/Documents
    dir = {
    "diretory" : f"{diretorio}"
    }
    escrever("Salvando pré-configuração")
    write_json(dir)
    escrever("Arquivo config.json salvo!!!")
    time.sleep(0.5)
    clear_console()

print(f"Nome: {nome_cliente}\nCaminho: {diretorio}\n")

# Criar pasta e arquivo
criar_pasta(diretorio, nome_cliente)
criar_arquivo(diretorio, nome_cliente)

