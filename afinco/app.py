import customtkinter as ck
from customtkinter import CTkImage
from tkinter import *
import sqlite3
from tkinter import messagebox
from Admin_menu import Admin_menu
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime  

         
class App(ck.CTk):
    def __init__(self):
            super().__init__()
            self.config_janela_inicial() 
            self.tela_login()
            self.cria_tabela()
            
    def config_janela_inicial(self):
            self.geometry("700x400")
            self.title('Mercado')
            self.resizable(False,False)
            self.configure(fg_color="#1F201C")
            
    def tela_login(self):
            if hasattr(self, 'container_new_cadastro'):
                    self.container_new_cadastro.destroy()
            if hasattr(self, 'frame_escolha_tipo'):
                self.frame_escolha_tipo.destroy()
            if hasattr(self, 'container_cadastro'):
                    self.container_cadastro.destroy()
                    
            self.img = PhotoImage(file='login.png')
            self.img = self.img.subsample(7,7)
            self.label_image = ck.CTkLabel(self, text=None, image=self.img)
            self.label_image.grid(row=1, column=0,padx=10, pady= 10)
            
            self.title_label = ck.CTkLabel(self, text = 'Faça login com sua conta existente \n ou Registre-se para  criar uma nova !', font=('Verdana', 17, 'bold'))
            self.title_label.grid(row=0, column=0, pady=10, padx=10)
            
            self.container_cadastro = ck.CTkFrame(self, width=350, height=350, corner_radius=13)
            self.container_cadastro.place(x=370, y=10)
            
            self.lb_title = ck.CTkLabel(self.container_cadastro, text="Faça seu login",font=('Verdana',20, 'bold'))
            self.lb_title.grid(row=0,column = 0,padx=10, pady=10)
            
            self.user_login = ck.CTkEntry(self.container_cadastro, width=300, placeholder_text='Seu nome de usuario..', font=('Verdana',16, 'bold'), corner_radius=15, border_color='grey')
            self.user_login.grid(row=1, column=0,padx=10,pady=10)
            
            self.senha_login = ck.CTkEntry(self.container_cadastro, width=300, placeholder_text='Sua senha..', font=('Verdana',16, 'bold'), corner_radius=15, border_color='grey', show="#")
            self.senha_login.grid(row=2, column=0,padx=10,pady=10)
            
            self.ver_senha = ck.CTkCheckBox(self.container_cadastro,text="Visualizar senha", font=('Verdana',12, 'bold'),corner_radius=20, command=self.toggle_senha_login)
            self.ver_senha.grid(row=3, column=0,padx=10,pady=10)
        
            self.btn_login= ck.CTkButton(self.container_cadastro, width=300, text='Cadastrar'.upper(), font=('Verdana',16, 'bold'),corner_radius=15, fg_color="#228B1C", hover_color="#1C6B17", command=self.verifica_login)
            self.btn_login.grid(row=4, column=0,padx=10,pady=10)
            
            self.aviso = ck.CTkLabel(self.container_cadastro, text= "Novo cadastro?, clique abaixo.", font= ('Verdana', 10,'bold'))
            self.aviso.grid(row=5, column=0,padx=10,pady=10)
            
            self.btn_cadastro= ck.CTkButton(self.container_cadastro, width=300, text='NOVA CONTA'.upper(), font=('Verdana',16, 'bold'),corner_radius=15, command=self.tela_cadastro)
            self.btn_cadastro.grid(row=6, column=0,padx=10,pady=10)
            
    def tela_cadastro(self):
            if hasattr(self, 'container_new_cadastro') and self.container_new_cadastro.winfo_exists():
                self.container_new_cadastro.destroy()
            if hasattr(self, 'container_cadastro') and self.container_cadastro.winfo_exists():
                self.container_cadastro.destroy()
            if hasattr(self, 'frame_escolha_tipo') and self.frame_escolha_tipo.winfo_exists():
                self.frame_escolha_tipo.destroy()
                
            self.container_new_cadastro = ck.CTkFrame(self, width=420, height=480, corner_radius=13)
            self.container_new_cadastro.place(x=370, y=10)

            self.lb_title = ck.CTkLabel(self.container_new_cadastro, text="Faça seu Cadastro", font=('Verdana', 20, 'bold'))
            self.lb_title.grid(row=0, column=0, padx=10, pady=12)

            self.new_user_login = ck.CTkEntry(self.container_new_cadastro, width=300, placeholder_text='Seu nome de usuário...', font=('Verdana', 16, 'bold'), corner_radius=15, border_color='grey')
            self.new_user_login.grid(row=1, column=0, padx=10, pady=5)

            self.new_user_email = ck.CTkEntry(self.container_new_cadastro, width=300, placeholder_text='Email do usuário...', font=('Verdana', 16, 'bold'), corner_radius=15, border_color='grey')
            self.new_user_email.grid(row=2, column=0, padx=10, pady=5)

            self.cadastro_senha_login = ck.CTkEntry(self.container_new_cadastro, width=300, placeholder_text='Senha do usuário...', font=('Verdana', 16, 'bold'), corner_radius=15, border_color='grey', show= "#")
            self.cadastro_senha_login.grid(row=3, column=0, padx=10, pady=5)

            self.confirmar_senha_cadastro = ck.CTkEntry(self.container_new_cadastro, width=300, placeholder_text='Confirmar senha...', font=('Verdana', 16, 'bold'), corner_radius=15, border_color='grey', show="#")
            self.confirmar_senha_cadastro.grid(row=4, column=0, padx=10, pady=5)
            
            self.ver_senha = ck.CTkCheckBox(self.container_new_cadastro, text="Visualizar senha", font=('Verdana', 12, 'bold'), corner_radius=20, command=self.toggle_senha_cadastro)
            self.ver_senha.grid(row=5, column=0, pady=10,)
            
            self.tipo_usuario_var = StringVar()
            self.tipo_usuario_combobox = ck.CTkComboBox(self.container_new_cadastro, values=["Cliente", "Administrador"], variable=self.tipo_usuario_var, command=self.alterar_formulario_tipo_usuario)
            self.tipo_usuario_combobox.grid(row=6, column=0, padx=10, pady=5)
            self.tipo_usuario_combobox.set("Cliente")
            
            self.btn_cadastrar_user = ck.CTkButton(self.container_new_cadastro, width=300, text='Cadastrar'.upper(), font=('Verdana', 16, 'bold'), corner_radius=15, fg_color="#228B1C", hover_color="#1C6B17", command= self.cadastrar_usuario)
            self.btn_cadastrar_user.grid(row=7, column=0, padx=10, pady=5)
            
            self.btn_voltar_login = ck.CTkButton(self.container_new_cadastro, width=300, text='VOLTAR AO LOGIN', font=('Verdana', 16, 'bold'), corner_radius=15, command=self.tela_login)
            self.btn_voltar_login.grid(row=8, column=0, padx=10, pady=10)
            
            self.alterar_formulario_tipo_usuario("Cliente")
            
    def tela_new_user(self):
            if hasattr(self, 'container_cadastro') and self.container_cadastro.winfo_exists():
                self.container_cadastro.destroy()
            if hasattr(self, 'container_new_cadastro') and self.container_new_cadastro.winfo_exists():
                self.container_new_cadastro.destroy()
            if hasattr(self, 'frame_escolha_tipo') and self.frame_escolha_tipo.winfo_exists():
                self.frame_escolha_tipo.destroy()

            self.frame_escolha_tipo = ck.CTkFrame(self, width=400, height=200, corner_radius=13)
            self.frame_escolha_tipo.place(x=150, y=100)

            lb = ck.CTkLabel(self.frame_escolha_tipo, text="Escolha o tipo de conta:", font=('Verdana', 18, 'bold'))
            lb.grid(row=0, column=0, columnspan=2, pady=10)

            btn_cliente = ck.CTkButton(self.frame_escolha_tipo, text="Cliente", command=lambda: self.tela_cadastro("Cliente"))
            btn_cliente.grid(row=1, column=0, padx=10, pady=10)

            btn_admin = ck.CTkButton(self.frame_escolha_tipo, text="Administrador", command=lambda: self.tela_cadastro("Administrador"))
            btn_admin.grid(row=1, column=1, padx=10, pady=10)

            btn_voltar_login = ck.CTkButton(self.frame_escolha_tipo, text="Voltar ao Login", command=self.tela_login)
            btn_voltar_login.grid(row=2, column=0, columnspan=2, pady=10)

    def alterar_formulario_tipo_usuario(self, escolha):
        self.new_user_login.grid_forget()
        self.new_user_email.grid_forget()
        self.cadastro_senha_login.grid_forget()
        self.confirmar_senha_cadastro.grid_forget()
        self.ver_senha.grid_forget()
        self.tipo_usuario_combobox.grid_forget()
        self.btn_cadastrar_user.grid_forget()
        self.btn_voltar_login.grid_forget()

        self.new_user_login.grid(row=1, column=0, padx=10, pady=5)

        if escolha == "Cliente":
            self.new_user_email.grid(row=2, column=0, padx=10, pady=5)
            self.cadastro_senha_login.grid(row=3, column=0, padx=10, pady=5)
            self.confirmar_senha_cadastro.grid(row=4, column=0, padx=10, pady=5)
            self.ver_senha.grid(row=5, column=0, pady=10)
            self.tipo_usuario_combobox.grid(row=6, column=0, padx=10, pady=5)
            self.btn_cadastrar_user.grid(row=7, column=0, padx=10, pady=5)
            self.btn_voltar_login.grid(row=8, column=0, padx=10, pady=10)
            self.btn_voltar_login.configure(text="VOLTAR AO LOGIN", command=self.tela_login)

        elif escolha == "Administrador":
            self.cadastro_senha_login.grid(row=2, column=0, padx=10, pady=5)
            self.confirmar_senha_cadastro.grid(row=3, column=0, padx=10, pady=5)
            self.ver_senha.grid(row=4, column=0, pady=10)
            self.btn_cadastrar_user.grid(row=5, column=0, padx=10, pady=5)
            self.btn_voltar_login.configure(text="VOLTAR", command=self.voltar_para_tela_escolha_tipo)
            self.btn_voltar_login.grid(row=6, column=0, padx=10, pady=10)
            
    def limpa_new_cadastro(self):
        self.new_user_login.delete(0, END)
        self.new_user_email.delete(0, END)
        self.cadastro_senha_login.delete(0, END)
        self.confirmar_senha_cadastro.delete(0, END)
        
    def limpa_new_login(self):
            self.user_login.delete(0, END)
            self.senha_login.delete(0, END)
            self.ver_senha.deselect()
            
    def cadastrar_usuario(self):
            user_login = self.new_user_login.get()
            tipo_usuario = self.tipo_usuario_var.get()
            user_email = self.new_user_email.get()
            senha = self.cadastro_senha_login.get()
            confirmar_senha = self.confirmar_senha_cadastro.get()

            if tipo_usuario == "Administrador":
                if user_login == "" or senha == "" or confirmar_senha == "":
                    messagebox.showerror(title="Sistema de login", message="Por favor preencha todos os campos obrigatórios para Administrador!")
                    return
                
                if len(user_login) <= 11 or not all(c.isalpha() or c.isspace() for c in user_login):
                        messagebox.showerror(title="Login", 
                         message="O nome de usuário do Administrador deve ter mais de 12 caracteres, usando apenas letras e espaços (sem números ou símbolos).")
                        return
                    
                if senha != confirmar_senha:
                    messagebox.showerror(title="Sistema de login", message="Erro!!\nSenhas diferentes!")
                    return
                
            else:
                user_email = self.new_user_email.get()
                senha = self.cadastro_senha_login.get()
                confirmar_senha = self.confirmar_senha_cadastro.get()

                if (user_login == "" or user_email == "" or senha == "" or confirmar_senha == ""):
                    messagebox.showerror(title="Sistema de login", message="Erro!!\nPor favor preencha todos campos!")
                    return

                if len(user_login) < 4 or not user_login.isalpha():
                    messagebox.showerror(title="Sistema de login", 
                        message="O nome de usuário deve ter pelo menos 4 letras e não pode ter números!")
                    return
                
                if "@" not in user_email:
                    messagebox.showerror(title="Sistema de login", 
                        message="O email precisa conter '@'.")
                    return

                if len(senha) < 4:
                    messagebox.showerror(title="Sistema de login", 
                        message="A senha deve ter pelo menos 4 caracteres!")
                    return

                if senha != confirmar_senha:
                    messagebox.showerror(title="Sistema de login", message="Erro!!\nSenhas diferentes!")
                    return
            
            try:
                self.conexão_db()
            
                if tipo_usuario != "Administrador":
                    self.cursor.execute("SELECT * FROM Usuarios WHERE User = ?", (user_login,))
                if self.cursor.fetchone():
                        messagebox.showerror(title="Erro no cadastro", message="Já existe um usuário com este nome!")
                        self.desconecta_db()
                        return
            
                if tipo_usuario != "Administrador":
                    self.cursor.execute("SELECT * FROM Usuarios WHERE Email = ?", (user_email,))
                if self.cursor.fetchone():
                    messagebox.showerror(title="Erro no cadastro", message="Já existe um usuário com este email!")
                    self.desconecta_db()
                    return

                self.cursor.execute("""
                    INSERT INTO Usuarios (User, Email, Senha, Confirmar_Senha, Tipo)
                    VALUES (?, ?, ?, ?, ?)
                """, (user_login, user_email, senha, confirmar_senha, tipo_usuario))
                self.conex.commit()

                if tipo_usuario == "Administrador":
                    messagebox.showinfo(
                            title="Cadastro realizado",
                            message=f"Prezado(a) {user_login}, seu cadastro como administrador foi concluído com sucesso. Por favor, faça login para iniciar a gestão da plataforma."
                        )
                else:
                        messagebox.showinfo(
                            title="Cadastro realizado",
                            message=f"{user_login}!\n Cadastro concluído. Faça login e aproveite tudo o que preparamos para você!"
                        )
                self.limpa_new_cadastro()
                self.tela_login()

            except Exception as e:
                messagebox.showerror(title="Erro no cadastro", message=f"Ocorreu um erro: {e}")

            finally:
                self.desconecta_db()
                    
    def toggle_senha_cadastro(self):
            if self.ver_senha.get() == 1:
                self.cadastro_senha_login.configure(show="")
                self.confirmar_senha_cadastro.configure(show="")
            else:
                self.cadastro_senha_login.configure(show="#")
                self.confirmar_senha_cadastro.configure(show="#")
                
    def toggle_senha_login(self):
            if self.ver_senha.get() == 1:
                self.senha_login.configure(show="")
            else:
                self.senha_login.configure(show="#")

    def voltar_para_tela_escolha_tipo(self):
        if hasattr(self, 'container_new_cadastro') and self.container_new_cadastro.winfo_exists():
            self.container_new_cadastro.destroy()
            self.tela_cadastro()

    def verifica_login(self):
        def registrar_login(usuario, tipo):
            conn = sqlite3.connect("sistema.db")
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS LoginsRecentes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    data_hora TEXT NOT NULL
                )
            """)
            agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO LoginsRecentes (usuario, tipo, data_hora) VALUES (?, ?, ?)", (usuario, tipo, agora))
            conn.commit()
            conn.close()

        try:
            user_login = self.user_login.get().strip()
            senha_login = self.senha_login.get().strip()

            if not user_login or not senha_login:
                messagebox.showwarning(
                    title='Sistema de Login', 
                    message="Por favor preencha todos os campos!"
                )
                return

            self.conexão_db()

            self.cursor.execute("SELECT * FROM Usuarios WHERE User = ? AND Senha = ?", 
                                (user_login, senha_login))
            resultado = self.cursor.fetchone()

            if resultado:
                tipo_usuario = resultado[5]
                self.usuario_logado = user_login

                registrar_login(user_login, tipo_usuario)

                is_admin = (tipo_usuario == "Administrador")

                if is_admin:
                    if len(user_login) <= 11 or not all(c.isalpha() or c.isspace() for c in user_login):
                        messagebox.showerror(
                            title="Login",
                            message="O nome de usuário do Administrador deve ter mais que 11 caracteres, usando apenas letras e espaços (sem números ou símbolos)."
                        )
                        return
                    messagebox.showinfo(
                        title='Login',
                        message=f"Bem-vindo, {user_login}!\nCadastro de administrador efetuado com sucesso.\nPor favor, proceda com o login para acessar o painel de gerenciamento."
                    )

                else:
                    self.limpa_new_login()
                    messagebox.showinfo(title='Login',
                                    message=f"Bem-vindo, {user_login.capitalize()}!\nLogin realizado com sucesso.")

                self.carregar_imagens_admin()

                self.withdraw()
                admin_menu = Admin_menu(
                    master=self,
                    images=self.admin_images,
                    admin_name=user_login,
                    is_admin=is_admin
                )
                admin_menu.grab_set()
                self.wait_window(admin_menu)
                self.deiconify()

            else:
                messagebox.showerror(
                    title="Sistema de Login",
                    message="Usuário ou senha inválidos!"
                )

        except sqlite3.Error as e:
            messagebox.showerror(
                title="Erro de Banco de Dados",
                message=f"Erro ao acessar o banco de dados:\n{str(e)}"
            )

        except Exception as e:
            messagebox.showerror(
                title="Erro inesperado",
                message=f"Ocorreu um erro inesperado:\n{str(e)}"
            )

        finally:
            if hasattr(self, 'conex') and self.conex:
                self.desconecta_db()
        
    def carregar_imagens_admin(self):
            try:
                self.admin_images = {
                'carrinho': ImageTk.PhotoImage(Image.open("imagens/carrinho.png").resize((30, 30), Image.LANCZOS)),
                'usertrocar': ImageTk.PhotoImage(Image.open("imagens/usertrocar.png").resize((30, 30), Image.LANCZOS)),
                'vendas': ImageTk.PhotoImage(Image.open("imagens/vendas.png").resize((30, 30), Image.LANCZOS)),
                'dashboard': ImageTk.PhotoImage(Image.open("imagens/dashboard.png").resize((30, 30), Image.LANCZOS)),
                'estoque': ImageTk.PhotoImage(Image.open("imagens/estoque.png").resize((30, 30), Image.LANCZOS))
                }
            except Exception as e:
                print(f"Erro ao carregar imagens: {e}")
                self.admin_images = {
                    k: tk.PhotoImage(width=30, height=30)
                    for k in ['carrinho', 'usertrocar', 'vendas', 'dashboard', 'estoque']
                }

    def conexão_db(self):
            self.conex = sqlite3.connect('Sistema_cadastros.db', check_same_thread=False)
            self.cursor = self.conex.cursor()
            print('Banco de dados criado 👨‍💻')
        
    def desconecta_db(self):
            self.conex.close()
            print('Banco de dados desconectado  📴')
        
    def cria_tabela(self):
            self.conexão_db()
            self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS Usuarios(
                            Id INTEGER PRIMARY KEY AUTOINCREMENT,
                            User TEXT NOT NULL,
                            Email TEXT NOT NULL,
                            Senha TEXT NOT NULL,
                            Confirmar_Senha TEXT NOT NULL,
                            Tipo TEXT NULL
                            
                            );""")
            self.conex.commit()
            print("Tabela criada.")
            self.desconecta_db()   
        
    def getdetalhes(self):
        self.amontarmain()
        
    def amontarmain(self):
        self.Admin_menu(8,8)
        self.topframe = LabelFrame(self.mainw, width=1420, height=97, bg="#4267b2")
        self.topframe.place(x=0, y=0)
        self.loja_name = "Mercadinho"
        self.lojalable = Label(self.topframe, text=self.loja_name +  "'Sistemas Vendas", bg="#4267b2", anchor="center")
        self.lojalable.config(font="Roboto 30 bold", fg="snow")
        self.lojalable.place(x=150, y=30)
        img = PhotoImage(file="imagens/perfil.png")
        img = img.subsample(4,4)
        self.menuperfil = tk.Label(self.topframe, image=img, compound= TOP)
        self.menuperfil.image = img
        self.menuperfil.place(x=1250, y=8)
            
    def entrar_admin(self):
        try:
            dummy_images = {
                'carrinho': CTkImage(Image.open("imagens/carrinho.png").resize((30, 30))),
                'usertrocar': CTkImage(Image.open("imagens/usertrocar.png").resize((30, 30))),
                'vendas': CTkImage(Image.open("imagens/vendas.png").resize((30, 30))),
                'dashboard': CTkImage(Image.open("imagens/dashboard.png").resize((30, 30))),
                'estoque': CTkImage(Image.open("imagens/estoque.png").resize((30, 30))),
            }
        except Exception as e:
            print("Erro ao carregar imagens:", e)
            dummy_images = {
                'carrinho': CTkImage(Image.new("RGBA", (30, 30), (0, 0, 0, 0))),
                'usertrocar': CTkImage(Image.new("RGBA", (30, 30), (0, 0, 0, 0))),
                'vendas': CTkImage(Image.new("RGBA", (30, 30), (0, 0, 0, 0))),
                'dashboard': CTkImage(Image.new("RGBA", (30, 30), (0, 0, 0, 0))),
                'estoque': CTkImage(Image.new("RGBA", (30, 30), (0, 0, 0, 0))),
            }

        self.withdraw()

        admin = Admin_menu(dummy_images, admin_name="João Gomes", is_admin=True)
        admin.grab_set()
        admin.focus()

if __name__ == "__main__":
    app = App()
    app.mainloop()