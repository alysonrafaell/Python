import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
from adicionar_produto import TelaAdicionarProduto
from dashboard import TelaDashboard
from estoque import TelaEstoque
from fornecedores import TelaFornecedores
from vendas import TelaVendas

class Admin_menu(tk.Toplevel):
    def __init__(self, master=None, images=None, admin_name="", is_admin=False):
        super().__init__(master)
        self.images = images
        self.admin_name = admin_name
        self.is_admin = is_admin
        
        self.title("Sistema de Mercado - Admin" if is_admin else "Sistema de Mercado - Cliente")
        self.geometry("900x600")
        self.resizable(False, False)
        self.configure(bg="#f8f9fa")
        
        self.protocol("WM_DELETE_WINDOW", self.quit_app)

        self.create_header()
        self.create_button_area()
        self.create_bottom_block()
        
    def create_header(self):
        header_frame = tk.Frame(self, bg="#2c3e50", height=100)
        header_frame.pack(fill=tk.X)
        
        title_frame = tk.Frame(header_frame, bg="#2c3e50")
        title_frame.pack(side=tk.LEFT, padx=20)
        
        title_label = tk.Label(title_frame,
                             text="PAINEL ADMINISTRATIVO" if self.is_admin else "PAINEL DO CLIENTE",
                             font=("Roboto", 16, "bold"),
                             bg="#2c3e50",
                             fg="white")
        title_label.pack(pady=10)
        
        user_frame = tk.Frame(header_frame, bg="#2c3e50")
        user_frame.pack(side=tk.RIGHT, padx=20)
        
        profile_container = tk.Frame(user_frame, bg="#34495e", bd=0, highlightthickness=0)
        profile_container.pack(pady=10, padx=10)
        
        try:
            profile_img = Image.open("imagens/perfil1.png").resize((50, 50), Image.LANCZOS)
            self.profile_photo = ImageTk.PhotoImage(profile_img)
            profile_label = tk.Label(profile_container, image=self.profile_photo, bg="#34495e")
            profile_label.grid(row=0, column=0, rowspan=2, padx=(0, 10))
        except:
            profile_label = tk.Label(profile_container, text="👤", font=("Arial", 20), 
                                   bg="#34495e", fg="white")
            profile_label.grid(row=0, column=0, rowspan=2, padx=(0, 10))
        
        welcome_label = tk.Label(profile_container,
                               text="Bem-vindo,",
                               font=("Roboto", 10),
                               bg="#34495e",
                               fg="#ecf0f1")
        welcome_label.grid(row=0, column=1, sticky="w")
        
        name_label = tk.Label(profile_container,
                            text=self.admin_name if self.admin_name else ("Admin" if self.is_admin else "Cliente"),
                            font=("Roboto", 12, "bold"),
                            bg="#34495e",
                            fg="white")
        name_label.grid(row=1, column=1, sticky="w")

    def create_button_area(self):
        button_main_frame = tk.Frame(self, bg="#f8f9fa")
        button_main_frame.pack(pady=20, fill=tk.X, padx=20)
        
        button_container = tk.Frame(button_main_frame, bg="white", bd=0, 
                                  highlightbackground="#e0e0e0", highlightthickness=1,
                                  relief=tk.RAISED)
        button_container.pack(fill=tk.X, padx=10, pady=10)
        
        all_buttons = [
            {"text": "Adicionar produtos", "image": "carrinho", "command": self.adicionar_produto},
            {"text": "Fornecedores", "image": "usertrocar", "command": self.fornecedores},
            {"text": "Vendas", "image": "vendas", "command": self.vendas},
            {"text": "Dashboard", "image": "dashboard", "command": self.dashboard},
            {"text": "Estoque", "image": "estoque", "command": self.estoque}
        ]

        botoes_cliente = ["Vendas", "Estoque"]

        buttons_frame = tk.Frame(button_container, bg="white")
        buttons_frame.pack(pady=10, padx=10)
        
        for btn in all_buttons:
            if not self.is_admin and btn["text"] not in botoes_cliente:
                continue

            btn_frame = tk.Frame(buttons_frame, bg="white")
            btn_frame.pack(side=tk.LEFT, padx=15, pady=5)
            
            photo = self.images[btn["image"]]
            button = tk.Button(
                btn_frame,
                text=btn["text"],
                font=("Roboto", 10, "bold"),
                image=photo,
                compound=tk.TOP,
                bg="white",
                fg="#2c3e50",
                activebackground="#f0f0f0",
                activeforeground="#2c3e50",
                relief=tk.FLAT,
                bd=0,
                padx=10,
                pady=5,
                command=btn["command"]
            )
            button.image = photo
            button.pack()
            
            button.bind("<Enter>", lambda e, b=button: b.config(bg="#f0f0f0"))
            button.bind("<Leave>", lambda e, b=button: b.config(bg="white"))
    
    def create_bottom_block(self):
            bottom_frame = tk.Frame(self, bg="#f8f9fa")
            bottom_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

            container = tk.Frame(bottom_frame, bg="white", bd=0,
                                highlightbackground="#e0e0e0", highlightthickness=1,
                                relief=tk.RAISED)
            container.pack(fill=tk.BOTH, expand=True)

            header = tk.Frame(container, bg="#2c3e50", height=40)
            header.pack(fill=tk.X)

            titulo = "ÚLTIMOS ACESSOS" if self.is_admin else "PRODUTOS À VENDA"
            tk.Label(header, text=titulo, font=("Roboto", 11, "bold"),
                    bg="#2c3e50", fg="white", anchor=tk.W, padx=15).pack(side=tk.LEFT)

            table_frame = tk.Frame(container, bg="white")
            table_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

            if self.is_admin:
                headers = ["USUÁRIO", "TIPO DE ACESSO", "DATA/HORA"]
                query = """
                    SELECT usuario, tipo, data_hora 
                    FROM LoginsRecentes 
                    ORDER BY data_hora DESC 
                    LIMIT 10
                """
            else:
                headers = ["NOME", "DESCRIÇÃO", "PREÇO"]
                query = """
                    SELECT nome, descricao, preco 
                    FROM Produtos 
                    ORDER BY id DESC 
                    LIMIT 10
                """

            for col, header_text in enumerate(headers):
                lbl = tk.Label(table_frame, text=header_text, font=("Roboto", 9, "bold"),
                            bg="#3498db", fg="white", padx=10, pady=5)
                lbl.grid(row=0, column=col, sticky="ew")
                table_frame.grid_columnconfigure(col, weight=1)

            try:
                conn = sqlite3.connect("sistema.db")
                cursor = conn.cursor()
                cursor.execute(query)
                dados = cursor.fetchall()
                conn.close()
            except Exception as e:
                dados = []
                print(f"Erro ao carregar dados: {e}")

            for row, linha in enumerate(dados, start=1):
                bg = "#f8f9fa" if row % 2 == 0 else "white"
                for col, valor in enumerate(linha):
                    if not self.is_admin and col == 2:
                        valor = f"R$ {valor:.2f}"
                    lbl = tk.Label(table_frame, text=valor, font=("Roboto", 9),
                                bg=bg, padx=10, pady=5, anchor=tk.W)
                    lbl.grid(row=row, column=col, sticky="ew")

    def adicionar_produto(self):
        TelaAdicionarProduto(self)

    def vendas(self):
        TelaVendas(self)

    def dashboard(self):
        TelaDashboard(self)

    def estoque(self):
        TelaEstoque(self)

    def fornecedores(self):
        TelaFornecedores(self)

    def quit_app(self):
        self.destroy()
        self.quit()