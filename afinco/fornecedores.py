import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import re

class TelaFornecedores(tk.Toplevel):
    def __init__(self, parent, is_admin=False):
        super().__init__(parent)
        self.title("Gerenciar Fornecedores")
        self.geometry("800x550")
        self.resizable(False, False)
        self.is_admin = is_admin

        self.conn = sqlite3.connect("fornecedores.db")
        self.cursor = self.conn.cursor()
        self.criar_tabela()

        self.frame_form = tk.Frame(self, padx=10, pady=10)
        self.frame_form.pack(fill=tk.X)

        self.frame_lista = tk.Frame(self)
        self.frame_lista.pack(fill=tk.BOTH, expand=True)

        self.criar_formulario()
        self.criar_lista()
        self.carregar_fornecedores()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS fornecedores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                email TEXT
            )
        """)
        self.conn.commit()

    def criar_formulario(self):
        tk.Label(self.frame_form, text="Nome:").grid(row=0, column=0)
        self.entry_nome = ttk.Entry(self.frame_form)
        self.entry_nome.grid(row=0, column=1, padx=10)

        tk.Label(self.frame_form, text="Telefone:").grid(row=1, column=0)
        self.entry_telefone = ttk.Entry(self.frame_form)
        self.entry_telefone.grid(row=1, column=1, padx=10)

        tk.Label(self.frame_form, text="Email:").grid(row=2, column=0)
        self.entry_email = ttk.Entry(self.frame_form)
        self.entry_email.grid(row=2, column=1, padx=10)

        ttk.Button(self.frame_form, text="Adicionar", command=self.adicionar_fornecedor).grid(row=0, column=2, padx=10)
        ttk.Button(self.frame_form, text="Atualizar", command=self.atualizar_fornecedor).grid(row=1, column=2, padx=10)
        ttk.Button(self.frame_form, text="Excluir", command=self.excluir_fornecedor).grid(row=2, column=2, padx=10)

    def validar_nome(self, nome):
        if len(nome) <= 11:
            return False
        if not re.match(r'^[a-zA-ZÀ-ÿ\s]{12,}$', nome):
            return False
        return True

    def validar_email(self, email):
        return re.match(r'[^@]+@[^@]+\.[^@]+', email) is not None

    def criar_lista(self):
        colunas = ("id", "nome", "telefone", "email")
        self.tree = ttk.Treeview(self.frame_lista, columns=colunas, show="headings")
        for col in colunas:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.selecionar_linha)

    def carregar_fornecedores(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.cursor.execute("SELECT * FROM fornecedores")
        for row in self.cursor.fetchall():
            self.tree.insert("", tk.END, values=row)

    def adicionar_fornecedor(self):
        nome = self.entry_nome.get().strip()
        telefone = self.entry_telefone.get().strip()
        email = self.entry_email.get().strip()

        if not self.validar_nome(nome):
            messagebox.showerror("Erro", "Nome inválido. Deve ter mais que 11 caracteres e conter apenas letras e um espaço.")
            return
            
        if not self.validar_email(email):
            messagebox.showerror("Erro", "Email inválido. Deve conter @ e domínio válido.")
            return

        self.cursor.execute("""
            INSERT INTO fornecedores (nome, telefone, email) 
            VALUES (?, ?, ?)
        """, (nome, telefone, email))
        
        self.conn.commit()
        self.carregar_fornecedores()
        self.limpar_campos()

    def atualizar_fornecedor(self):
        item = self.tree.selection()
        if not item:
            messagebox.showwarning("Seleção", "Selecione um fornecedor para atualizar.")
            return

        id_selecionado = self.tree.item(item)["values"][0]
        nome = self.entry_nome.get().strip()
        telefone = self.entry_telefone.get().strip()
        email = self.entry_email.get().strip()

        if not self.validar_nome(nome) or not self.validar_email(email):
            return

        self.cursor.execute("""
            UPDATE fornecedores 
            SET nome=?, telefone=?, email=?
            WHERE id=?
        """, (nome, telefone, email, id_selecionado))
        
        self.conn.commit()
        self.carregar_fornecedores()
        self.limpar_campos()

    def excluir_fornecedor(self):
        item = self.tree.selection()
        if not item:
            messagebox.showwarning("Seleção", "Selecione um fornecedor para excluir.")
            return

        if messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir este fornecedor?"):
            id_selecionado = self.tree.item(item)["values"][0]
            self.cursor.execute("DELETE FROM fornecedores WHERE id=?", (id_selecionado,))
            self.conn.commit()
            self.carregar_fornecedores()
            self.limpar_campos()

    def selecionar_linha(self, event):
        item = self.tree.selection()
        if item:
            valores = self.tree.item(item)["values"]
            self.entry_nome.delete(0, tk.END)
            self.entry_nome.insert(0, valores[1])
            self.entry_telefone.delete(0, tk.END)
            self.entry_telefone.insert(0, valores[2])
            self.entry_email.delete(0, tk.END)
            self.entry_email.insert(0, valores[3])

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

    def __del__(self):
        self.conn.close()