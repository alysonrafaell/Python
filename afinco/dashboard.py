import tkinter as tk
from tkinter import ttk
import sqlite3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from collections import defaultdict

class TelaDashboard(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Dashboard de Vendas")
        self.geometry("900x600")
        self.configure(bg="white")

        self.criar_banco_de_dados()
        self.criar_widgets()
        self.mostrar_grafico_vendas()

    def criar_banco_de_dados(self):
        self.conn = sqlite3.connect('produtos.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT,
                total REAL,
                recebido REAL,
                troco REAL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS itens_venda (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                venda_id INTEGER,
                produto_descricao TEXT,
                quantidade INTEGER,
                preco_unitario REAL,
                total REAL
            )
        """)
        self.conn.commit()

    def criar_widgets(self):
        tk.Label(self, text="Área de Análise de Vendas", font=("Arial", 16, "bold"), bg="white").pack(pady=20)

        self.frame_grafico = tk.Frame(self, bg="white")
        self.frame_grafico.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def mostrar_grafico_vendas(self):
        self.cursor.execute("SELECT data, SUM(total) FROM vendas GROUP BY data ORDER BY data")
        dados = self.cursor.fetchall()

        datas = [linha[0][:10] for linha in dados]
        totais = [linha[1] for linha in dados]

        fig, ax = plt.subplots(figsize=(7, 4))
        ax.bar(datas, totais, color='skyblue')
        ax.set_title("Total de Vendas por Dia")
        ax.set_xlabel("Data")
        ax.set_ylabel("Total em R$")

        canvas = FigureCanvasTkAgg(fig, master=self.frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()