#Ultima modificação Dia 5/7/2023 feita por: Barros
import tkinter as tk
from PIL import ImageTk
from PIL import Image
import os

global cadastrado
global canvas
cadastrado = False

def remover_foco_login(event):
    global canvas
    global texto_login_entrada
    global texto_senha_entrada
    global texto_login_entrada_cadastro
    global texto_senha_entrada_cadastro
    global texto_senha_entrada_cadastro_confirmação

    canvas.focus_set()   

    if texto_senha_entrada == "Coloque sua Senha aqui...":
        senha_entrada.delete(0, tk.END)
    if texto_login_entrada == "Coloque seu Login aqui...":     
        login_entrada.delete(0, tk.END)    
    
def limpar_placeholder_login(event):
    global senha_entrada
    global login_entrada
    global texto_login_entrada
    global texto_senha_entrada

    texto_login_entrada= login_entrada.get()
    texto_senha_entrada= senha_entrada.get()    
    
    if texto_senha_entrada == "Coloque sua Senha aqui...":
        senha_entrada.delete(0, tk.END) 
        senha_entrada.configure(show="")  
    else:
        senha_entrada.configure(show="*")
     
    if texto_login_entrada == "Coloque seu Login aqui...":
        login_entrada.delete(0, tk.END)    

def remover_foco_cadastro(event):
    global canvas
    global texto_login_entrada
    global texto_senha_entrada
    global texto_login_entrada_cadastro
    global texto_senha_entrada_cadastro
    global texto_senha_entrada_cadastro_confirmação
    canvas.focus_set() 
      
    if texto_senha_entrada_cadastro == "Coloque sua Senha aqui...":
        senha_entrada_cadastro.delete(0, tk.END)
    if texto_login_entrada_cadastro == "Coloque seu Login aqui...":     
        login_entrada_cadastro.delete(0, tk.END)    
    if texto_senha_entrada_cadastro_confirmação == "Confirme sua Senha aqui...":     
        senha_entrada_cadastro_confirmação.delete(0, tk.END)                          
   
def limpar_placeholder_cadastro(event):
    global senha_entrada_cadastro
    global login_entrada_cadastro
    global senha_entrada_cadastro_confirmação
    global texto_login_entrada_cadastro
    global texto_senha_entrada_cadastro
    global texto_senha_entrada_cadastro_confirmação

    texto_login_entrada_cadastro = login_entrada_cadastro.get()
    texto_senha_entrada_cadastro = senha_entrada_cadastro.get()
    texto_senha_entrada_cadastro_confirmação = senha_entrada_cadastro_confirmação.get()

    
    if texto_senha_entrada_cadastro == "Coloque sua Senha aqui...":
        senha_entrada_cadastro.delete(0, tk.END) 
        senha_entrada_cadastro.configure(show="")  
    else:
        senha_entrada_cadastro.configure(show="*")
     
    if texto_senha_entrada_cadastro_confirmação == "Confirme sua Senha aqui...":
        senha_entrada_cadastro_confirmação.delete(0, tk.END) 
        senha_entrada_cadastro_confirmação.configure(show="") 
    else:
        senha_entrada_cadastro_confirmação.configure(show="*")           
     
    if texto_login_entrada_cadastro == "Coloque seu Login aqui...":
        login_entrada_cadastro.delete(0, tk.END)    


def cadastro():

    global cadastrar_usuario
    global botao_fazer_cadastro

    def cadastrar_usuario():

        global login_entrada_cadastro
        global senha_entrada_cadastro
        global senha_entrada_cadastro_confirmação
        global alerta_confirmar_senha
        global alerta_senha
        global alerta_login
        global tamanho_senha
        global alerta_cadastro
        global cadastrado
        global nome
        global senha

        caracteres_especiais = ["!", "@", "#", "$", "%", "&", "*", "-", "_", "+", "=", "/", "\\", "|", ":", ";", ",", ".", "?", "(", ")", "[", "]", "{", "}", "<", ">", "'", "`", "~", "^", "¡", "¿", "ç"]
        nome = login_entrada_cadastro.get()
        senha = senha_entrada_cadastro.get()
        confirmar_senha = senha_entrada_cadastro_confirmação.get()
        tamanho_senha = len(senha)
        #canvas.itemconfig(item_id, text="Novo texto")
        canvas.itemconfig(alerta_login, text="")
        canvas.itemconfig(alerta_senha, text="")
        canvas.itemconfig(alerta_confirmar_senha, text="")
        canvas.itemconfig(alerta_cadastro, text="")
        if (nome == "") or (senha == "") or (confirmar_senha == ""):
            canvas.itemconfig(alerta_login, text="• Todos os campos são obrigatórios!", font=("Cascadia Mono SemiBold", 11, "bold"), fill="#00CED1")
            canvas.itemconfig(alerta_senha, text="• Todos os campos são obrigatórios!", font=("Cascadia Mono SemiBold", 11, "bold"), fill="#00CED1")
            canvas.itemconfig(alerta_confirmar_senha, text="• Todos os campos são obrigatórios!", font=("Cascadia Mono SemiBold", 11, "bold"), fill="#00CED1")
            if nome != "":
                canvas.itemconfig(alerta_login, text="")
            if senha != "":
                canvas.itemconfig(alerta_senha, text="")
            if confirmar_senha != "":
                canvas.itemconfig(alerta_confirmar_senha, text="")

        elif not any(char in caracteres_especiais for char in senha):
            canvas.itemconfig(alerta_login, text="")
            canvas.itemconfig(alerta_senha, text="• Coloque pelo menos 1 caractere especial!", font=("Cascadia Mono SemiBold", 10, "bold"), fill="#00CED1")
            canvas.itemconfig(alerta_confirmar_senha, text="")
        elif tamanho_senha < 3 or tamanho_senha > 10:
            canvas.itemconfig(alerta_login, text="")
            canvas.itemconfig(alerta_senha, text="• Minímo de 3 caracteres e máximo de 10!", font=("Cascadia Mono SemiBold", 11, "bold"), fill="#00CED1")
            canvas.itemconfig(alerta_confirmar_senha, text="")
        elif senha != confirmar_senha:
            canvas.itemconfig(alerta_login, text="")
            canvas.itemconfig(alerta_senha, text="• As senhas não batem!", font=("Cascadia Mono SemiBold", 12, "bold"), fill="#00CED1")
            canvas.itemconfig(alerta_confirmar_senha, text="• As senhas não batem!", font=("Cascadia Mono SemiBold", 12, "bold"), fill="#00CED1")
        elif nome == senha:
            canvas.itemconfig(alerta_login, text="• Nome e senha não podem ser iguais!", font=("Cascadia Mono SemiBold", 11, "bold"), fill="#00CED1")
            canvas.itemconfig(alerta_senha, text="• Nome e senha não podem ser iguais!", font=("Cascadia Mono SemiBold", 11, "bold"), fill="#00CED1")
            canvas.itemconfig(alerta_confirmar_senha, text="")
        else:
            canvas.itemconfig(alerta_cadastro, text="Cadastro Efetuado!!", font=("Cascadia Mono SemiBold", 15, "bold"), fill="green")
            cadastrado = True
    

    def func_mostrar_senha():
        global senha_entrada_cadastro        
        if senha_entrada_cadastro.cget("show") == "*":
            senha_entrada_cadastro.config(show="")
        else:
            senha_entrada_cadastro.config(show="*")
            
    def func_mostrar_senha_confirmacao():
        global senha_entrada_cadastro_confirmação
        if senha_entrada_cadastro_confirmação.cget("show") == "*":
            senha_entrada_cadastro_confirmação.config(show="")
        else:
            senha_entrada_cadastro_confirmação.config(show="*")

    def func_janela_cadastro():
        global imagem_janela_cadastro_tk
        global imagem_janela_logo_cadastro_tk
        global imagem_janela_cadastro_iconeUser_tk
        global imagem_janela_cadastro_iconecadeadofechado_tk
        global imagem_janela_cadastro_nuvem_tk
        global canvas 
        global login_entrada_cadastro
        global senha_entrada_cadastro
        global senha_entrada_cadastro_confirmação
        global alerta_confirmar_senha
        global alerta_senha
        global alerta_login        
        global alerta_cadastro
        global janela_cadastro
        global botao_fazer_cadastro

        janela_cadastro = tk.Toplevel()
        janela_cadastro.title("Cadastro")
        janela_cadastro.geometry("360x640")
        janela_cadastro.resizable(False, False)
        canvas = tk.Canvas(janela_cadastro, width=360, height=640)
        canvas.pack()        
        imagem_janela_cadastro_caminho = os.path.join(diretorio_atual, 'imagem_de_fundo.jpg')
        imagem_janela_cadastro = Image.open(imagem_janela_cadastro_caminho)
        imagem_janela_cadastro_resized = imagem_janela_cadastro.resize((360, 640))  
        imagem_janela_cadastro_tk = ImageTk.PhotoImage(imagem_janela_cadastro_resized)
        canvas.create_image(0, 0, image=imagem_janela_cadastro_tk, anchor="nw")

        imagem_janela_logo_caminho = os.path.join(diretorio_atual, 'logo_ehchuva.png')
        imagem_janela_logo_cadastro = Image.open(imagem_janela_logo_caminho) 
        imagem_janela_logo_cadastro_resized = imagem_janela_logo_cadastro.resize((450, 350)) 
        imagem_janela_logo_cadastro_tk = ImageTk.PhotoImage(imagem_janela_logo_cadastro_resized)
        canvas.create_image(-40, -50, image=imagem_janela_logo_cadastro_tk, anchor="nw")

        imagem_janela_cadastro_nuvem_caminho = os.path.join(diretorio_atual, 'nuvem.png') 
        imagem_janela_cadastro_nuvem = Image.open(imagem_janela_cadastro_nuvem_caminho)
        imagem_janela_cadastro_nuvem_resized = imagem_janela_cadastro_nuvem.resize((420,170))
        imagem_janela_cadastro_nuvem_tk = ImageTk.PhotoImage(imagem_janela_cadastro_nuvem_resized)
        canvas.create_image(-15, 225, image=imagem_janela_cadastro_nuvem_tk, anchor="nw") 
        canvas.create_image(-15, 315, image=imagem_janela_cadastro_nuvem_tk, anchor="nw")
        canvas.create_image(-15, 405, image=imagem_janela_cadastro_nuvem_tk, anchor="nw")  
        canvas.create_image(-15, 540, image=imagem_janela_cadastro_nuvem_tk, anchor="nw")         

        imagem_janela_cadastro_iconeUser_caminho = os.path.join(diretorio_atual, 'icone_user.png') 
        imagem_janela_cadastro_iconeUser = Image.open(imagem_janela_cadastro_iconeUser_caminho)
        imagem_janela_cadastro_iconeUser_resized = imagem_janela_cadastro_iconeUser.resize((30,30))
        imagem_janela_cadastro_iconeUser_tk = ImageTk.PhotoImage(imagem_janela_cadastro_iconeUser_resized)
        canvas.create_image(75, 275, image=imagem_janela_cadastro_iconeUser_tk, anchor="nw")

        imagem_janela_cadastro_iconecadeadofechado_caminho = os.path.join(diretorio_atual, 'icone_cadeado_fechado.png') 
        imagem_janela_cadastro_iconecadeadofechado = Image.open(imagem_janela_cadastro_iconecadeadofechado_caminho)
        imagem_janela_cadastro_iconecadeadofechado_resized = imagem_janela_cadastro_iconecadeadofechado.resize((25,25))
        imagem_janela_cadastro_iconecadeadofechado_tk = ImageTk.PhotoImage(imagem_janela_cadastro_iconecadeadofechado_resized)
        canvas.create_image(75, 365, image=imagem_janela_cadastro_iconecadeadofechado_tk, anchor="nw")     
        canvas.create_image(75, 455, image=imagem_janela_cadastro_iconecadeadofechado_tk, anchor="nw")     
                 
        informacao_janela_cadastro = canvas.create_text(180, 245, text="Cadastre-se", font=("Cooper Black", 18))

        """x1, y1, x2, y2 = 95, 311.5, 120, 328
        hor, ver = 157, 85
        for i in range(2):
            canvas.create_oval(x1,y1,x2,y2, fill = '#C0C0C0', outline= '#000000')
            canvas.create_oval(x1,y1+ver,x2,y2+ver, fill = '#C0C0C0', outline= '#000000')
            canvas.create_oval(x1,y1+2*ver,x2,y2+2*ver, fill = '#C0C0C0', outline= '#000000')
            x1, x2 = x1+hor, x2+hor"""

        login_entrada_cadastro = tk.Entry(janela_cadastro, width=25, border = 0, bg="#F8F8FF")
        login_entrada_cadastro.insert(0, "Coloque seu Login aqui...")        
        login_barra_cadastro = canvas.create_text(190, 310, text="――――――――――――――――――", font=("Arial", 9, "bold"))
        login_entrada_cadastro_window = canvas.create_window(110, 290, anchor="w", window=login_entrada_cadastro)

        senha_entrada_cadastro = tk.Entry(janela_cadastro, width=25, border = 0, bg='#F8F8FF')
        senha_entrada_cadastro.insert(0, "Coloque sua Senha aqui...")        
        senha_barra_cadastro = canvas.create_text(190, 400, text="――――――――――――――――――", font=("Arial", 9, "bold"))
        senha_entrada_cadastro_window = canvas.create_window(110, 380, anchor="w", window=senha_entrada_cadastro)

        senha_entrada_cadastro_confirmação = tk.Entry(janela_cadastro, width=25, border = 0, bg='#F8F8FF')
        senha_entrada_cadastro_confirmação.insert(0, "Confirme sua Senha aqui...")       
        login_barra = canvas.create_text(190, 490, text="――――――――――――――――――", font=("Arial", 9, "bold"))
        senha_entrada_cadastro_confirmação_window = canvas.create_window(110, 470, anchor="w", window=senha_entrada_cadastro_confirmação)
        
        botao_fazer_cadastro = tk.Button(janela_cadastro, text="Cadastrar-se", command=cadastrar_usuario, cursor='hand2', bg="#F8F8FF", fg="#000000")
        botao_fazer_cadastro_window = canvas.create_window(180, 555, anchor="center", window=botao_fazer_cadastro)
                                
        botao_direcionamento_login = tk.Button(janela_cadastro, text="Faça o login", command=troca_janela_cadastro_pro_login, cursor='hand2', bg="#F8F8FF", fg="#0000FF")
        direcionamento_login_texto = canvas.create_text(180, 600, text="Se você já está cadastrado", font=("Cooper Black", 12))        
        botao_direcionamento_login_window = canvas.create_window(180, 625, anchor="center", window=botao_direcionamento_login)   

        alerta_login = canvas.create_text(180, 335, text="")
        alerta_senha = canvas.create_text(180, 430, text="")
        alerta_confirmar_senha = canvas.create_text(180, 515, text="")  
        alerta_cadastro = canvas.create_text(180, 520, text="") 

        mostrar_senha = tk.Button(janela_cadastro, text="😎", command=func_mostrar_senha, cursor='hand2')
        mostrar_senha_janela = canvas.create_window(325, 380, anchor="center", window=mostrar_senha)
        mostrar_senha_confirmacao = tk.Button(janela_cadastro, text="😎", command=func_mostrar_senha_confirmacao, cursor='hand2')
        mostrar_senha_confirmacao_janela = canvas.create_window(325, 470, anchor="center", window=mostrar_senha_confirmacao)

        canvas.bind('<Button-1>', remover_foco_cadastro)
        login_entrada_cadastro.bind('<FocusIn>', limpar_placeholder_cadastro)
        senha_entrada_cadastro.bind('<FocusIn>', limpar_placeholder_cadastro)        
        senha_entrada_cadastro_confirmação.bind('<FocusIn>', limpar_placeholder_cadastro)

    func_janela_cadastro()

def troca_janela_login_pro_cadastro():

    def vai_pro_cadastro():
        global janela_login
        janela_login.destroy()
        cadastro()
    vai_pro_cadastro()

def troca_janela_cadastro_pro_login():

    def vai_pro_login():
        global janela_cadastro
        janela_cadastro.destroy()
        login()
    vai_pro_login()


def login():

    def conta_existente():
        global cadastrado
        global alerta_login
        global alerta_login_realizado
        global canvas
        global nome
        global senha

        teste_login_realizado = login_entrada.get()
        teste_senha_realizado = senha_entrada.get()
        
        if teste_login_realizado == nome and teste_senha_realizado == senha and cadastrado == True:
            canvas.itemconfig(alerta_login, text="")
            canvas.itemconfig(alerta_senha, text="")               
            canvas.itemconfig(alerta_login_realizado, text="Login Realizado!!", font=("Cascadia Mono SemiBold", 14, "bold"), fill="green")         
        else:
            canvas.itemconfig(alerta_login_realizado, text="")
            canvas.itemconfig(alerta_login, text="• Login não consta no sistema!", font=("Cascadia Mono SemiBold", 11, "bold"), fill="#00CED1")
            canvas.itemconfig(alerta_senha, text="• Senha não consta no sistema!", font=("Cascadia Mono SemiBold", 11, "bold"), fill="#00CED1")


    def func_mostrar_senha():
        global senha_entrada       
        if senha_entrada.cget("show") == "*":
            senha_entrada.config(show="")
        else:
            senha_entrada.config(show="*")


    def func_janela_login():

        global imagem_janela_login_tk
        global imagem_janela_logo_login_tk
        global imagem_janela_iconecadeado_tk
        global imagem_janela_iconeUser_tk
        global imagem_janela_nuvem_tk
        global alerta_login_realizado
        global canvas 
        global login_entrada
        global senha_entrada
        global alerta_senha
        global alerta_login        
        global alerta_cadastro
        global janela_login
        global cadastro

        janela_login = tk.Toplevel()
        janela_login.title("Login")
        janela_login.geometry("360x640")
        janela_login.resizable(False,False)
        canvas = tk.Canvas(janela_login, width=360, height=640)
        canvas.pack()        

        imagem_janela_login_caminho = os.path.join(diretorio_atual, 'imagem_de_fundo.jpg')
        imagem_janela_login = Image.open(imagem_janela_login_caminho)
        imagem_janela_login_resized = imagem_janela_login.resize((360, 640))  
        imagem_janela_login_tk = ImageTk.PhotoImage(imagem_janela_login_resized)
        canvas.create_image(0, 0, image=imagem_janela_login_tk, anchor="nw")

        imagem_janela_logo_caminho = os.path.join(diretorio_atual, 'logo_ehchuva.png')
        imagem_janela_logo_login = Image.open(imagem_janela_logo_caminho)
        imagem_janela_logo_login_resized = imagem_janela_logo_login.resize((450, 350)) 
        imagem_janela_logo_login_tk = ImageTk.PhotoImage(imagem_janela_logo_login_resized)
        canvas.create_image(-40, -50, image=imagem_janela_logo_login_tk, anchor="nw")

        imagem_janela_nuvem_caminho = os.path.join(diretorio_atual, 'nuvem.png') 
        imagem_janela_nuvem = Image.open(imagem_janela_nuvem_caminho)
        imagem_janela_nuvem_resized = imagem_janela_nuvem.resize((420,170))
        imagem_janela_nuvem_tk = ImageTk.PhotoImage(imagem_janela_nuvem_resized)
        canvas.create_image(-15, 240, image=imagem_janela_nuvem_tk, anchor="nw") 
        canvas.create_image(-15, 330, image=imagem_janela_nuvem_tk, anchor="nw")
        canvas.create_image(-15, 475, image=imagem_janela_nuvem_tk, anchor="nw")
                 
        imagem_janela_iconeUser_caminho = os.path.join(diretorio_atual, 'icone_user.png') 
        imagem_janela_iconeUser = Image.open(imagem_janela_iconeUser_caminho)
        imagem_janela_iconeUser_resized = imagem_janela_iconeUser.resize((30,30))
        imagem_janela_iconeUser_tk = ImageTk.PhotoImage(imagem_janela_iconeUser_resized)
        canvas.create_image(75, 290, image=imagem_janela_iconeUser_tk, anchor="nw")

        imagem_janela_iconecadeado_caminho = os.path.join(diretorio_atual, 'icone_cadeado.png') 
        imagem_janela_iconecadeado = Image.open(imagem_janela_iconecadeado_caminho)
        imagem_janela_iconecadeado_resized = imagem_janela_iconecadeado.resize((25,25))
        imagem_janela_iconecadeado_tk = ImageTk.PhotoImage(imagem_janela_iconecadeado_resized)
        canvas.create_image(75, 380, image=imagem_janela_iconecadeado_tk, anchor="nw")     

        informacao_janela_login= canvas.create_text(180, 245, text="Acesse o Aplicativo", font=("Cooper Black", 20))


        """x1, y1, x2, y2 = 95, 311.5, 120, 328
        hor, ver = 157, 85
        for i in range(2):
            canvas.create_oval(x1,y1,x2,y2, fill = '#C0C0C0', outline= '#000000')
            canvas.create_oval(x1,y1+ver,x2,y2+ver, fill = '#C0C0C0', outline= '#000000')
            x1, x2 = x1+hor, x2+hor"""


        login_entrada = tk.Entry(janela_login, width=25, border= 0, bg="#F8F8FF")
        login_entrada.insert(0, "Coloque seu Login aqui...")
        login_barra = canvas.create_text(190, 325, text="――――――――――――――――――", font=("Arial", 9, "bold"))        
        login_entrada_window = canvas.create_window(110, 305, anchor="w", window=login_entrada )

        senha_entrada = tk.Entry(janela_login, width=25, border = 0, bg="#F8F8FF")
        senha_entrada.insert(0, "Coloque sua Senha aqui...")
        senha_barra = canvas.create_text(190, 415, text="――――――――――――――――――", font=("Arial", 9, "bold"))        
        senha_entrada_window = canvas.create_window(110, 395, anchor="w", window=senha_entrada)

        botao_direcionamento_cadastro = tk.Button(janela_login, text="Cadastre-se", command=troca_janela_login_pro_cadastro, cursor='hand2', bg="#F8F8FF", fg="#0000FF", width=15)       
        botao_direcionamento_cadastro_window = canvas.create_window(180, 545, anchor="center", window=botao_direcionamento_cadastro)  

        botao_fazer_login = tk.Button(janela_login, text="Fazer Login", command=conta_existente, cursor='hand2')
        botao_fazer_login_window = canvas.create_window(180, 485, anchor="center", window=botao_fazer_login)    

        alerta_login = canvas.create_text(180, 350, text="")
        alerta_senha = canvas.create_text(180, 440, text="")
        alerta_login_realizado = canvas.create_text(180, 450, text="")

        mostrar_senha = tk.Button(janela_login, text="😎", command=func_mostrar_senha, cursor='hand2')
        mostrar_senha_janela = canvas.create_window(325, 395, anchor="center", window=mostrar_senha)

        canvas.bind('<Button-1>', remover_foco_login)
        senha_entrada.bind('<FocusIn>', limpar_placeholder_login)
        login_entrada.bind('<FocusIn>', limpar_placeholder_login)

    func_janela_login()


caminho_atual = os.path.abspath(__file__)
diretorio_atual = os.path.dirname(caminho_atual)




menu = tk.Tk()
menu.title("Teste Cadastro")
menu.geometry("300x300")
botao_cadastro = tk.Button(menu, text="Cadastro", command=cadastro)
botao_login = tk.Button(menu, text="Login", command=login)
botao_cadastro.pack()
botao_login.pack()

menu.mainloop()

