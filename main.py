from CTkMessagebox import CTkMessagebox
from customtkinter import *
from pathlib import Path
import crarpa_main, os, utils

# Mudar tema
set_appearance_mode("dark")
set_default_color_theme("dark-blue")


# config
file_extense = ".cdr"


# Criar janela
app = CTk()
WINX, WINY = 500, 300
app.geometry(str(WINX)+"x"+str(WINY))
app.title("Crarpa Auto")
# app.iconbitmap("image\logo_icon.ico")
app.resizable(False, False)


#Funções da aplicação

def verificar_dados(name_str, diretory):
    response = True
    
    if not name_str: # verificar se o texto não está vazio e exibir uma cor vermelha no input
        input_client.configure(fg_color='red')
        # input_client.focus()
        response = False
    
    elif not os.path.exists(diretory): # verificar se esse caminho existe e exibir uma cor vermelha no input
        input_dir.configure(fg_color='red')
        # input_dir.focus()
        response = False
    
    elif verificar_existencia(name_str, diretory):
        input_client.configure(fg_color='red')
        response = False
        
    
    if name_str and not verificar_existencia(name_str, diretory): input_client.configure(fg_color=['#F9F9FA', '#343638']) 
    if os.path.exists(diretory): input_dir.configure(fg_color=['#F9F9FA', '#343638'])

    if name_str and os.path.exists(diretory): return True
    if not response:
        return False


def verificar_existencia(name_file, dir_file): 
    if os.path.exists(dir_file):
        if dir_file and name_file in os.listdir(dir_file):
            return True
    
    return False


def button_gerar():
    # print(input_dir.cget('fg_color'))
    
    name = input_client.get()
    caminho = input_dir.get()
    
    if verificar_dados(name, caminho): # Verificar se o campo de nomes não está vazio e se o caminho existe 
        print(f'Name: {name}\nDir: {caminho}')
        
        if crarpa_main.run(name, caminho, file_extense):
            CTkMessagebox(title="Arquivo criado com sucesso", message=f"NOME: \n{name}\n\nDIR:\n{caminho}", icon="check", header=False)
            print("Successfully created .cdr file and folder")
            
            utils.text_formated_json(name, caminho)
            
            if var_checkbox.get() == "open":
                cam = f"{caminho}\\{name}\\{name}{file_extense}"
                utils.open_cdr(cam)
        
        else:
            if verificar_existencia(name, caminho):
                CTkMessagebox(title="Erro", message=f"Não foi possível realizar a operação\n\nERROR: 001", icon="cancel", header=False)
            
            else:
                CTkMessagebox(title="Erro", message=f"Não foi possível realizar a operação\n\nERROR: 002", icon="cancel", header=False)
                
            print("Error in create file and archive")
                             
                             
        


def press_key(event):
    key = event.keysym
    name = input_client.get()
    caminho = input_dir.get()
    verificar_dados(name, caminho)
    
    if key == "Return":
        button_gerar()


def inserir(obj, posx=None, posy=None, side=None):
    if posx or posy:
        obj.place(x=posx, y=posy)
        
    elif side != None:
        obj.pack(side=side)
        
    else:
        return Exception
    

def search_dir():
    caminho = Path(filedialog.askdirectory())
    print(caminho)
    var_dir.set(str(caminho))
    if os.path.exists(input_dir.get()): input_dir.configure(fg_color=['#F9F9FA', '#343638'])
   

def checkbox_value():
    print(f"CheckBox: {var_checkbox.get()}")


def checar_estado():
    try:
        caminho = utils.ultimo_status()
        var_dir.set(caminho)
    
    except:
        var_dir.set(r"C:/Users")

app.bind('<Key>', func=press_key)

 
# Classe para criar Frames
class Frame:
    def __init__(self, root, width, height):
        self.root = root
        self.width = width
        self.height = height
    
        self.frame = CTkFrame(self.root, self.width, self.height)
    
    def adicionar(self, side):
        inserir(self.frame, side=side)
        

# create frames 
frame_right = Frame(root=app, width=(WINX-35), height=WINY)
frame_left = Frame(root=app, width=30, height=WINY)
frame_left.frame.configure(fg_color="transparent")


# widget frame right
titulo_label_right = CTkLabel(master=frame_right.frame, text="Sistema de Gerenciamento", font=("Impact", 15))

name_client_label = CTkLabel(master=frame_right.frame, text="Name: ", font=("Arial", 10))
input_client = CTkEntry(master=frame_right.frame, placeholder_text="Client: ", width=270)
dir_label = CTkLabel(master=frame_right.frame, text="Dir: ", font=("Arial Bold", 10))
var_dir = StringVar()
input_dir = CTkEntry(master=frame_right.frame, textvariable=var_dir, width=270)
btn_dir = CTkButton(master=frame_right.frame, text="Search", width=50 ,command=search_dir)

var_checkbox = StringVar()
checkbox_open = CTkCheckBox(master=frame_right.frame, text='open', variable=var_checkbox, onvalue="open", offvalue="anything", command=checkbox_value)

btn_right = CTkButton(master=frame_right.frame, text="Gerar", command=button_gerar, width=70)


# widget frame left
version_label_left = CTkLabel(master=frame_left.frame, text="v1.0", font=("Impact", 10))
# btn_left_top = CTkButton(master=frame_left.frame, text="-",width=10, height=30, command=scale_bar_left)


# Lançar frames
frame_right.adicionar(side=RIGHT)
frame_left.adicionar(side=LEFT)

# Lançar widget right
inserir(titulo_label_right, (frame_right.width/2) -90, 10)
inserir(name_client_label, 25, 70)
inserir(input_client, 70, 70)
inserir(dir_label, 25, 110)
inserir(input_dir, 70, 110)
inserir(btn_dir, 350, 110)
inserir(checkbox_open, 70, 150)
inserir(btn_right, 380, 250)


# Lançar widget left
# inserir(btn_left_top, frame_left.width/4, 10)
inserir(version_label_left, frame_left.width/4, frame_right.height -30)


checar_estado()

# loop
app.mainloop()