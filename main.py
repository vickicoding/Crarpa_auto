import os, json, time, platform
import time
import platform


name_config = "Config.json"
extension = ".cdr"


# Função para criar o arquivo config caso não esteja criado
def write_json(argument_config):
    with open(name_config, 'w', encoding="utf-8") as arq:
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
        time.sleep(0.01)
    
    if next:
        print()
    return ""


# Função para criar uma pasta
def criar_pasta(diretorio, nome_cliente):
    caminho = os.path.join(diretorio, nome_cliente)
    os.makedirs(caminho, exist_ok=True)


# Função para criar um arquivo
def criar_arquivo(diretorio, nome_cliente):
    caminho = os.path.join(diretorio, nome_cliente, nome_cliente + extension)
    if not os.path.exists(caminho):
        with open(caminho, "w") as file:
            pass
        #Criação do arquivo foi um sucesso
        return True
    
    else:
        return False

#Função para obter o diretório do usuário ou do arquivo caso exista
def get_diretory():
    if os.path.exists(name_config):
        escrever("Carregando Configurações!!!")
        diretorio = load_json(name_config)
        clear_console()
        
    else:
        escrever("Arquivo de configuração não encontrado...")
        while True:
            diretorio = input(escrever("Diretório: "))  # Exemplo: ~/Documents
            
            if not diretorio or not diretorio.strip():
                clear_console()
                escrever("Diretório não pode ser vazio!!!")
            
            else:
                break        
            
            
        dir = {
        "diretory" : f"{diretorio}"
        }
        escrever("Salvando pré-configuração")
        write_json(dir)
        escrever("Arquivo config.json salvo!!!")
        time.sleep(0.5)
        clear_console()
    
    return diretorio

#Função para receber um nome válido do usuário
def get_name():
    while True:
        name = input(escrever("Nome do Cliente: "))
        
        if not name.strip():
            clear_console()
            escrever("Nome não pode ser vaio!!!")
            time.sleep(0.5)
        
        else:
            return name    
            

# Solicita o nome do cliente
nome_cliente = get_name()
clear_console()

# Obter diretório
diretorio = get_diretory()


print(f"Nome: {nome_cliente}\nCaminho: {diretorio}\n")

# Criar pasta e arquivo
criar_pasta(diretorio, nome_cliente)
if criar_arquivo(diretorio, nome_cliente):
    escrever("Sucess!!!")

else:
    escrever("Arquivo já existente")
