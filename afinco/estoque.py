import tkinter as tk
from tkinter import ttk
import sqlite3

class TelaEstoque(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Estoque por Fornecedor")
        self.geometry("600x400")
        self.configure(bg="white")
        self.resizable(False, False)

        self.conn = sqlite3.connect("produtos.db")
        self.cursor = self.conn.cursor()

        self.criar_interface()
        self.carregar_dados()

    def criar_interface(self):
        label_titulo = tk.Label(self, text="Estoque por Fornecedor", font=("Arial", 16, "bold"), bg="white")
        label_titulo.pack(pady=10)

        colunas = ("fornecedor", "num_produtos", "estoque_total")
        self.tree = ttk.Treeview(self, columns=colunas, show="headings")
        self.tree.heading("fornecedor", text="Fornecedor")
        self.tree.heading("num_produtos", text="Qtd. Produtos")
        self.tree.heading("estoque_total", text="Qtd. em Estoque")

        self.tree.column("fornecedor", width=200)
        self.tree.column("num_produtos", width=100, anchor=tk.CENTER)
        self.tree.column("estoque_total", width=120, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def carregar_dados(self):
        self.cursor.execute("""
            SELECT fornecedor, COUNT(*), SUM(quantidade)
            FROM produtos
            GROUP BY fornecedor
        """)
        resultados = self.cursor.fetchall()

        for row in resultados:
            self.tree.insert("", tk.END, values=row)

    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()   