import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class TelaAdicionarProduto(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Adicionar Produtos e Estoque")
        self.geometry("1100x600")
        self.resizable(False, False)
        
        self.conn = sqlite3.connect("produtos.db")
        self.c = self.conn.cursor()
        self.criar_tabela()
        
        self.frame_form = tk.Frame(self, bd=2, relief=tk.GROOVE, padx=15, pady=15)
        self.frame_form.place(x=10, y=10, width=400, height=580)
        
        self.frame_estoque = tk.Frame(self, bd=2, relief=tk.GROOVE, padx=15, pady=15)
        self.frame_estoque.place(x=420, y=10, width=670, height=580)
        
        self.criar_formulario()
        self.criar_lista_estoque()
        self.carregar_produtos_do_banco()

    def criar_tabela(self):
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                codigo TEXT PRIMARY KEY,
                descricao TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                preco REAL NOT NULL,
                fornecedor TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def criar_formulario(self):
        tk.Label(self.frame_form, text="Adicionar Produto", font=("Arial", 16, "bold")).pack(pady=10)
        
        tk.Label(self.frame_form, text="Código :").pack(anchor=tk.W)
        vcmd_codigo = (self.register(self.validar_codigo), '%P')
        self.entry_codigo = ttk.Entry(self.frame_form, validate='key', validatecommand=vcmd_codigo)
        self.entry_codigo.pack(fill=tk.X, pady=5)
        
        tk.Label(self.frame_form, text="Descrição:").pack(anchor=tk.W)
        self.entry_descricao = ttk.Entry(self.frame_form)
        self.entry_descricao.pack(fill=tk.X, pady=5)
        
        tk.Label(self.frame_form, text="Quantidade:").pack(anchor=tk.W)
        self.spin_quantidade = tk.Spinbox(self.frame_form, from_=1, to=10000, width=10)
        self.spin_quantidade.pack(fill=tk.X, pady=5)
        
        tk.Label(self.frame_form, text="Valor Unitário (R$):").pack(anchor=tk.W)
        vcmd_preco = (self.register(self.validar_preco), '%P')
        self.entry_preco = ttk.Entry(self.frame_form, validate='key', validatecommand=vcmd_preco)
        self.entry_preco.pack(fill=tk.X, pady=5)
        
        tk.Label(self.frame_form, text="Fornecedor:").pack(anchor=tk.W)
        self.combo_fornecedor = ttk.Combobox(self.frame_form, state="readonly")
        self.combo_fornecedor['values'] = ("Fornecedor A", "Fornecedor B", "Fornecedor C")
        self.combo_fornecedor.current(0)
        self.combo_fornecedor.pack(fill=tk.X, pady=5)
        
        btn_adicionar = ttk.Button(self.frame_form, text="Adicionar Produto", command=self.adicionar_produto)
        btn_adicionar.pack(pady=20, fill=tk.X)

    def validar_codigo(self, texto):
        if texto == "":
            return True
        if texto.isdigit() and len(texto) <= 5:
            return True
        return False

    def validar_preco(self, texto):
        if texto == "":
            return True
        allowed_chars = "0123456789,"
        if all(c in allowed_chars for c in texto):
            if texto.count(',') <= 1:
                return True
        return False

    def criar_lista_estoque(self):
        tk.Label(self.frame_estoque, text="Estoque de Produtos", font=("Arial", 16, "bold")).pack(pady=10)
        
        colunas = ("codigo", "descricao", "quantidade", "preco", "fornecedor")
        self.treeview_produtos = ttk.Treeview(self.frame_estoque, columns=colunas, show="headings")
        
        self.treeview_produtos.heading("codigo", text="Código")
        self.treeview_produtos.heading("descricao", text="Descrição")
        self.treeview_produtos.heading("quantidade", text="Quantidade")
        self.treeview_produtos.heading("preco", text="Valor Unitário (R$)")
        self.treeview_produtos.heading("fornecedor", text="Fornecedor")
        
        self.treeview_produtos.column("codigo", width=80, anchor=tk.CENTER)
        self.treeview_produtos.column("descricao", width=200)
        self.treeview_produtos.column("quantidade", width=80, anchor=tk.CENTER)
        self.treeview_produtos.column("preco", width=120, anchor=tk.E)
        self.treeview_produtos.column("fornecedor", width=150)
        
        self.treeview_produtos.pack(fill=tk.BOTH, expand=True)

    def adicionar_produto(self):
        codigo = self.entry_codigo.get().strip()
        descricao = self.entry_descricao.get().strip()
        quantidade = self.spin_quantidade.get().strip()
        preco = self.entry_preco.get().strip()
        fornecedor = self.combo_fornecedor.get().strip()
        
        if not codigo:
            messagebox.showerror("Erro", "O campo Código deve ser preenchido e conter apenas números.")
            return
        if not descricao:
            messagebox.showerror("Erro", "O campo Descrição não pode ficar vazio.")
            return
        if not quantidade:
            messagebox.showerror("Erro", "O campo Quantidade não pode ficar vazio.")
            return
        if not preco:
            messagebox.showerror("Erro", "O campo Valor Unitário não pode ficar vazio.")
            return
        if not fornecedor:
            messagebox.showerror("Erro", "Selecione um Fornecedor.")
            return
        
        try:
            quantidade_int = int(quantidade)
            if quantidade_int < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número inteiro positivo.")
            return
        
        try:
            preco_float = float(preco.replace(",", "."))
            if preco_float < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Valor Unitário deve ser um número válido maior ou igual a zero.")
            return
        
        try:
            self.c.execute("""
                INSERT INTO produtos (codigo, descricao, quantidade, preco, fornecedor)
                VALUES (?, ?, ?, ?, ?)
            """, (codigo, descricao, quantidade_int, preco_float, fornecedor))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
        except sqlite3.IntegrityError:
            self.c.execute("SELECT quantidade FROM produtos WHERE codigo = ?", (codigo,))
            quant_atual = self.c.fetchone()
            quant_atual = quant_atual[0] if quant_atual else 0
            nova_quantidade = quant_atual + quantidade_int
            self.c.execute("""
                UPDATE produtos SET descricao=?, quantidade=?, preco=?, fornecedor=?
                WHERE codigo=?
            """, (descricao, nova_quantidade, preco_float, fornecedor, codigo))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
        
        self.limpar_formulario()
        self.carregar_produtos_do_banco()

    def limpar_formulario(self):
        self.entry_codigo.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)
        self.spin_quantidade.delete(0, tk.END)
        self.spin_quantidade.insert(0, "1")
        self.entry_preco.delete(0, tk.END)
        self.combo_fornecedor.current(0)

    def carregar_produtos_do_banco(self):
        self.c.execute("SELECT codigo, descricao, quantidade, preco, fornecedor FROM produtos")
        produtos = self.c.fetchall()
        
        for item in self.treeview_produtos.get_children():
            self.treeview_produtos.delete(item)
        
        for prod in produtos:
            codigo, descricao, quantidade, preco, fornecedor = prod
            self.treeview_produtos.insert("", tk.END, values=(
                codigo,
                descricao,
                quantidade,
                f"R$ {str(preco).replace('.', '.')}",
                fornecedor
            ))