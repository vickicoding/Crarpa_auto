import os, json, shutil
import datetime
from pathlib import Path


#Config
file_config = 'Report.json'



def open_cdr(cam):
    caminho_origem = cam
    name = str(caminho_origem).rsplit(f'\\', 1)[-1]
    name = Path(name).stem
    dir_parents = str(caminho_origem).rsplit(f'\\', 1)[0]
    extense = "." + str(caminho_origem).rsplit(f'.', 1)[-1]
    caminho_finally = f'"{str(dir_parents) + f"\\" + name + extense}"'
    
    # print(caminho_finally)
    # print(name)
    # print(extense)

    os.system(caminho_finally)


def create_write_json(text):
    if create_file(file_config):
        # print("Config Create Sucess")
        
        if write_file(name_arq=file_config, content=text):
            # print("Write Sucess")
            pass
        else:
            # print("Error writed")
            pass
        
    else:
        # print("Error Created")
        if write_file(name_arq=file_config, content=text):
            # print("Write Sucess")
            pass


#função para ler um arquivo
def read_file_json(arq):
    try:
        with open(arq, "r", encoding="utf-8") as arq:
            data_json = json.load(arq)
            
            if not data_json == "":
                # print("Arquivo Acessado")
                return data_json

            else:
                # print("Arquivo vazio")
                return False
            
    except FileNotFoundError:
        # print("Arquivo não encontrado")
        return False


#função para criar um arquivo
def create_file(name_arq):
    if not os.path.exists(name_arq):
        data = {}
        data.update({'Dates': []})
        
        with open(name_arq, "w") as arq:
            json.dump(data, arq, indent=4, ensure_ascii=False)
        return True
        
    else:
        return False


def create_dir(arq, caminho, return_new_path=False):
    client = arq.replace(" ", "")
    name = Path(client).stem #client.rsplit('.', 1)[0]
    diretory = caminho.replace(" ", "")
    
    new_path = str(diretory) + "\\" + name + str("." + arq.rsplit('.', 1)[-1]) #Caminho completo da nova pasta junto ao arquivo
    Path(new_path)
    # print(new_path)
    old_path = Path(diretory) / arq #Caminho onde o arquivo esta antes de ser movido
    # print(f'\nDIR ATUAL: {Path.cwd()}\nNOVA DIR: {new_path}\nFONTE DIR: {old_path}')
    
    if return_new_path:
        return old_path, new_path
    
    return old_path
    

#Função para copiar arquivos
def copy_file(arq, caminho):
    old_path, new_path = create_dir(arq, caminho, return_new_path=True)
    
    #Path(dir_pasta).mkdir(exist_ok=True) #Criar pasta onde o arquivo irá ser movido
    shutil.copy2(old_path, new_path) #Mover arquivo para a nova pasta criada
    
    return new_path
    

#função para escrever em um arquivo
def write_file(name_arq, content):
    if os.path.exists(name_arq):
        data = read_file_json(name_arq)
        
        data["Dates"].append(content)
        
        with open(name_arq, "w", encoding="utf-8") as arq:
            json.dump(data, arq, indent=4, ensure_ascii=False )
            
        return True
    
    else:
        return False


def text_formated_json(client_name, diretory):
    dict_client = {
        'Date': data_atual(),
        'Hours': hora_atual(),
        'Name': client_name,
        'Dir': diretory
    }
    
    create_write_json(dict_client)



#função formatar um numero sempre mantendo 0 na frente caso seja menor que 10
def format_zero(number):
    if not number >= 10:
        number = "0" + str(number)
    return number


#função para obter a data atual
def data_atual():
    dt = datetime.date.today() 
    dia = format_zero(dt.day)
    mes = format_zero(dt.month)
    ano = dt.year
    data_text = f"{dia}/{mes}/{ano}"  
    
    return data_text

def hora_atual():
    dt = datetime.datetime

    hora_atual = dt.now()
    hora_formatada = hora_atual.strftime('%H:%M')

    return hora_formatada

def remove_barras(word):
    word = word.replace(r"\\", "")
    word = word.replace("/", "")
    return word


def ultimo_status():
    # print("Lendo ultimos arquivos")
    dados = read_file_json(file_config)
    
    if not dados == "":
        # print("dados enviados com sucesso")
        caminho = dados["Dates"][-1]["Dir"]
        return caminho
    
    else:
        # print("error ao tentar logar os ultimos caminhos")
        return FileNotFoundError