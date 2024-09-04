from CTkMessagebox import CTkMessagebox
from customtkinter import CTk, set_appearance_mode, set_default_color_theme, filedialog, CTkLabel, RIGHT, LEFT, CTkEntry, StringVar, CTkButton, CTkCheckBox, CTkFrame
import crarpa_main, os, utils

# Mudar tema
set_appearance_mode("dark")
set_default_color_theme("dark-blue")


# Criar janela
app = CTk()
WINX, WINY = 500, 300
app.geometry(str(WINX)+"x"+str(WINY))
app.title("Crarpa Auto")
# app.iconbitmap("image\logo_icon.ico")
app.resizable(False, False)


#Funções da aplicação

def verificar_dados(name: str, diretory: str, ext: str) -> bool:
    name_str = name.strip()
    extension = ext.strip()
    response = True
    
    # verificacão que exibirá uma cor vermelha onde está errado
    if not name_str: 
        input_client.configure(fg_color='red')
        response = False
    
    if not input_folder.get() and checkbox_folder.get() == "yes": 
        input_folder.configure(fg_color='red')
        response = False
    
    if not extension:
        input_file_extense.configure(fg_color='red')
        response = False
    
    elif not os.path.exists(diretory): 
        input_dir.configure(fg_color='red')
        response = False
    
    elif verificar_existencia(name_str, diretory):
        input_client.configure(fg_color='red')
        response = False
        
    
    if name_str and not verificar_existencia(name_str, diretory): input_client.configure(fg_color=['#F9F9FA', '#343638']) 
    if input_folder.get() and not verificar_existencia(input_folder.get(), diretory): input_folder.configure(fg_color=['#F9F9FA', '#343638']) 
    if extension: input_file_extense.configure(fg_color=['#F9F9FA', '#343638']) 
    if os.path.exists(diretory): input_dir.configure(fg_color=['#F9F9FA', '#343638'])
    

    # if name_str and os.path.exists(diretory): return True
    return response


def verificar_existencia(name_file, dir_file): 
    if os.path.exists(dir_file):
        if dir_file and name_file in os.listdir(dir_file):
            return True
    
    return False


def button_gerar():
    
    name = input_client.get().strip()
    folder = input_folder.get() if var_checkbox_folder.get() == "yes" else name
    caminho = input_dir.get()
    file_extense = input_file_extense.get()
    only_file: bool
    
    if checkbox_only_file.get() == "y":
        only_file = True
        
    else:
        only_file = False
        
    
    if verificar_dados(name, caminho, file_extense): # Verificar se o campo de nomes não está vazio e se o caminho existe 
        
        if crarpa_main.run(name=name, folder=folder, dir_file=caminho, ext=file_extense, only_file=only_file):
            CTkMessagebox(title="File created successfully", message=f"NAME: \n{name}\n\nDIR:\n{caminho}\nExt:\n{file_extense}", icon="check", header=False)
            
            utils.text_formated_json(name, caminho)
            
            if var_checkbox.get() == "open" and not only_file:
                cam = f"{caminho}\\{folder}\\{name}{file_extense}"
                utils.open_cdr(cam)
            
            elif var_checkbox.get() == "open" and only_file:
                cam = f"{caminho}\\{name}{file_extense}"
                utils.open_cdr(cam)
        
        else:
            if verificar_existencia(name, caminho):
                CTkMessagebox(title="Erro", message=f"The operation could not be performed\n\nERROR: 001", icon="cancel", header=False)#caminho já existe
            
            else:
                CTkMessagebox(title="Erro", message=f"The operation could not be performed\n\nERROR: 002", icon="cancel", header=False)#Error no arquivo crarpa_main
                
    else:
        CTkMessagebox(title="Erro", message=f"Fill in all the information\n\nERROR: 003", icon="cancel", header=False)#Erro de coerência/falta de informações
              
                             
def press_key(event):
    key = event.keysym
    name = input_client.get()
    caminho = input_dir.get()
    file_extense = input_file_extense.get()
    verificar_dados(name, caminho, file_extense)
    
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
    caminho = filedialog.askdirectory()
    var_dir.set(str(caminho))
    if os.path.exists(input_dir.get()): input_dir.configure(fg_color=['#F9F9FA', '#343638'])
   
   
def action_position_folder():
    if var_checkbox_folder.get() == "no":
        dir_label.place(x=25, y=150-40)
        input_dir.place(x=70, y=150-40)
        btn_dir.place(x=350, y=150-40)
        checkbox_open.place(x=25, y=190-40)
        checkbox_only_file.place(x=240, y=190-40)
        checkbox_folder.place(x=110, y=190-40)
        
        #"Esconder" label e Entry da Folder
        name_folder.place(x=25, y=150000)
        input_folder.place(x=70, y=150000)
        
        dir_label.focus()
        # checkbox_only_file.configure(state="normal")
            
    else:
        checkbox_only_file.deselect()
        # checkbox_only_file.configure(state="disabled")
        
        name_folder.place(x=25, y=150-40)
        input_folder.place(x=70, y=150-40)
        
        dir_label.place(x=25, y=150)
        input_dir.place(x=70, y=150)
        btn_dir.place(x=350, y=150)
        checkbox_open.place(x=25, y=190)
        checkbox_only_file.place(x=240, y=190)
        checkbox_folder.place(x=110, y=190)
       

def action_update_only_file():
    checkbox_folder.deselect()
    action_position_folder()

       
def Loding_date():
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
titulo_label_right = CTkLabel(master=frame_right.frame, text="Management System", font=("Impact", 15))
#name and extension file
name_client_label = CTkLabel(master=frame_right.frame, text="Name: ", font=("Arial", 10))
input_client = CTkEntry(master=frame_right.frame, placeholder_text="Client: ", width=270)
file_extense = StringVar(value=".cdr")
input_file_extense = CTkEntry(master=frame_right.frame, textvariable=file_extense, placeholder_text=file_extense, width=50)
#name folder and entry folder
name_folder = CTkLabel(master=frame_right.frame, text="Folder: ", font=("Arial", 10))
input_folder = CTkEntry(master=frame_right.frame, placeholder_text="Folder Name: ", width=270)
#diretory, entry for diretory and buttom "Search"
dir_label = CTkLabel(master=frame_right.frame, text="Dir: ", font=("Arial Bold", 10))
var_dir = StringVar()
input_dir = CTkEntry(master=frame_right.frame, textvariable=var_dir, width=270)
btn_dir = CTkButton(master=frame_right.frame, text="Search", width=50 ,command=search_dir)
#checkbox "Open"
var_checkbox = StringVar()
checkbox_open = CTkCheckBox(master=frame_right.frame, text='Open', variable=var_checkbox, onvalue="open", offvalue="anything")
#checkbox "Only file"
var_checkbox_only_file = StringVar()
checkbox_only_file = CTkCheckBox(master=frame_right.frame, text='Only File', variable=var_checkbox_only_file, onvalue="y", offvalue="n", command=action_update_only_file)
#checkbox "Person. Folder"
var_checkbox_folder = StringVar()
checkbox_folder = CTkCheckBox(master=frame_right.frame, text='Person. Folder', variable=var_checkbox_folder, onvalue="yes", offvalue="no", command=action_position_folder)
#Button make
btn_make_right = CTkButton(master=frame_right.frame, text="Make", command=button_gerar, width=70)


# widget frame left
version_label_left = CTkLabel(master=frame_left.frame, text="v1.1", font=("Impact", 10))
# btn_left_top = CTkButton(master=frame_left.frame, text="-",width=10, height=30, command=scale_bar_left)


# Lançar frames
frame_right.adicionar(side=RIGHT)
frame_left.adicionar(side=LEFT)

# Lançar widget right
inserir(titulo_label_right, (frame_right.width/2) -90, 10)
inserir(name_client_label, 25, 70)
inserir(input_client, 70, 70)
inserir(input_file_extense, 350, 70)
inserir(dir_label, 25, 110)
inserir(input_dir, 70, 110)
inserir(btn_dir, 350, 110)
inserir(checkbox_open, 25, 150)
inserir(checkbox_folder, 110, 150)
inserir(checkbox_only_file, 240, 150)

inserir(btn_make_right, 380, 250)

# Lançar widget left
# inserir(btn_left_top, frame_left.width/4, 10)
inserir(version_label_left, frame_left.width/4, frame_right.height -30)

Loding_date()

# loop
app.mainloop()