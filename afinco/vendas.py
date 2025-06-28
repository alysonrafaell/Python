import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
import os

class TelaVendas(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Sistema de Vendas")
        self.geometry("1000x700")
        self.resizable(False, False)
        
        self.conn = sqlite3.connect('produtos.db')
        self.cursor = self.conn.cursor()
        
        self.produtos_venda = []
        self.subtotal = tk.DoubleVar(value=0.0)
        self.total_recebido = tk.DoubleVar(value=0.0)
        self.troco = tk.DoubleVar(value=0.0)
        self.codigo_produto_atual = None
        
        self.criar_widgets()
        self.carregar_imagem_padrao()
        self.carregar_produtos_disponiveis()
        
    def criar_widgets(self):
        main_frame = tk.Frame(self, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        frame_esquerdo = tk.Frame(main_frame, width=500)
        frame_esquerdo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        frame_pesquisa = tk.LabelFrame(frame_esquerdo, text="Pesquisa de Produtos", padx=10, pady=10)
        frame_pesquisa.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(frame_pesquisa, text="Código ou Descrição:").pack(side=tk.LEFT)
        self.entry_pesquisa = ttk.Entry(frame_pesquisa, width=30)
        self.entry_pesquisa.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        self.entry_pesquisa.bind('<KeyRelease>', self.pesquisar_produto)
        
        frame_disponiveis = tk.LabelFrame(frame_esquerdo, text="Produtos Disponíveis", padx=10, pady=10)
        frame_disponiveis.pack(fill=tk.BOTH, expand=True)
        
        colunas = ("codigo", "descricao", "quantidade", "preco")
        self.treeview_disponiveis = ttk.Treeview(frame_disponiveis, columns=colunas, show="headings")
        
        self.treeview_disponiveis.heading("codigo", text="Código")
        self.treeview_disponiveis.heading("descricao", text="Descrição")
        self.treeview_disponiveis.heading("quantidade", text="Estoque")
        self.treeview_disponiveis.heading("preco", text="Preço Unitário")
        
        self.treeview_disponiveis.column("codigo", width=80, anchor=tk.CENTER)
        self.treeview_disponiveis.column("descricao", width=250)
        self.treeview_disponiveis.column("quantidade", width=80, anchor=tk.CENTER)
        self.treeview_disponiveis.column("preco", width=100, anchor=tk.E)
        
        scrollbar = ttk.Scrollbar(frame_disponiveis, orient="vertical", command=self.treeview_disponiveis.yview)
        self.treeview_disponiveis.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.treeview_disponiveis.pack(fill=tk.BOTH, expand=True)
        
        self.treeview_disponiveis.bind("<Double-1>", self.selecionar_produto_disponivel)
        
        frame_direito = tk.Frame(main_frame, width=500)
        frame_direito.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        frame_info_produto = tk.LabelFrame(frame_direito, text="Informações do Produto e Pagamento", padx=10, pady=10)
        frame_info_produto.pack(fill=tk.BOTH, expand=True)
        
        frame_imagem_info = tk.Frame(frame_info_produto)
        frame_imagem_info.pack(fill=tk.X, pady=(0, 20))
        
        frame_imagem = tk.Frame(frame_imagem_info, width=200, height=200)
        frame_imagem.pack(side=tk.LEFT, padx=(0, 10))
        
        self.label_imagem = tk.Label(frame_imagem, bg='gray')
        self.label_imagem.pack(fill=tk.BOTH, expand=True)
        
        frame_detalhes = tk.Frame(frame_imagem_info)
        frame_detalhes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tk.Label(frame_detalhes, text="Descrição:", anchor='w').grid(row=0, column=0, sticky='w', pady=2)
        self.label_descricao = tk.Label(frame_detalhes, text="", anchor='w', font=('Arial', 10))
        self.label_descricao.grid(row=0, column=1, sticky='w', pady=2)
        
        tk.Label(frame_detalhes, text="Preço Unitário:", anchor='w').grid(row=1, column=0, sticky='w', pady=2)
        self.label_preco = tk.Label(frame_detalhes, text="R$ 0.00", anchor='w', font=('Arial', 10))
        self.label_preco.grid(row=1, column=1, sticky='w', pady=2)
        
        tk.Label(frame_detalhes, text="Estoque Disponível:", anchor='w').grid(row=2, column=0, sticky='w', pady=2)
        self.label_estoque = tk.Label(frame_detalhes, text="0", anchor='w', font=('Arial', 10))
        self.label_estoque.grid(row=2, column=1, sticky='w', pady=2)
        
        tk.Label(frame_detalhes, text="Quantidade:", anchor='w').grid(row=3, column=0, sticky='w', pady=2)
        self.spin_quantidade = tk.Spinbox(frame_detalhes, from_=1, to=100, width=5)
        self.spin_quantidade.grid(row=3, column=1, sticky='w', pady=2)
        
        btn_adicionar = ttk.Button(frame_detalhes, text="Adicionar à Venda", command=self.adicionar_a_venda)
        btn_adicionar.grid(row=4, column=0, columnspan=2, pady=10, sticky='ew')
        
        ttk.Separator(frame_info_produto, orient='horizontal').pack(fill=tk.X, pady=10)
        
        frame_pagamento = tk.Frame(frame_info_produto)
        frame_pagamento.pack(fill=tk.X)
        
        frame_pagamento.columnconfigure(1, weight=1)
        
        tk.Label(frame_pagamento, text="Subtotal:", font=('Arial', 10)).grid(row=0, column=0, sticky='e', pady=5)
        self.label_subtotal = tk.Label(frame_pagamento, text="R$ 0.00", font=('Arial', 10, 'bold'))
        self.label_subtotal.grid(row=0, column=1, sticky='w', pady=5, padx=10)
        
        tk.Label(frame_pagamento, text="Total Recebido:", font=('Arial', 10)).grid(row=1, column=0, sticky='e', pady=5)
        self.entry_recebido = ttk.Entry(frame_pagamento, textvariable=self.total_recebido, font=('Arial', 10))
        self.entry_recebido.grid(row=1, column=1, sticky='ew', pady=5, padx=10)
        self.entry_recebido.bind('<KeyRelease>', self.calcular_troco)
        
        tk.Label(frame_pagamento, text="Troco:", font=('Arial', 10)).grid(row=2, column=0, sticky='e', pady=5)
        self.label_troco = tk.Label(frame_pagamento, text="R$ 0.00", font=('Arial', 10, 'bold'))
        self.label_troco.grid(row=2, column=1, sticky='w', pady=5, padx=10)
        
        frame_botoes = tk.Frame(frame_info_produto)
        frame_botoes.pack(fill=tk.X, pady=(10, 0))
        
        btn_finalizar = ttk.Button(frame_botoes, text="Finalizar Venda", command=self.finalizar_venda)
        btn_finalizar.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        btn_cancelar = ttk.Button(frame_botoes, text="Cancelar Venda", command=self.cancelar_venda)
        btn_cancelar.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
    
    def carregar_imagem_padrao(self):
        try:
            img = Image.new('RGB', (200, 200), color='gray')
            photo = ImageTk.PhotoImage(img)
            self.label_imagem.configure(image=photo)
            self.label_imagem.image = photo
        except Exception as e:
            print(f"Erro ao carregar imagem padrão: {e}")
    
    def carregar_imagem_produto(self, caminho_imagem):
        try:
            if os.path.exists(caminho_imagem):
                img = Image.open(caminho_imagem)
                img = img.resize((200, 200), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                self.label_imagem.configure(image=photo)
                self.label_imagem.image = photo
            else:
                self.carregar_imagem_padrao()
        except Exception as e:
            print(f"Erro ao carregar imagem do produto: {e}")
            self.carregar_imagem_padrao()
    
    def carregar_produtos_disponiveis(self):
        try:
            self.cursor.execute("SELECT codigo, descricao, quantidade, preco FROM produtos WHERE quantidade > 0 ORDER BY descricao")
            produtos = self.cursor.fetchall()
            
            for item in self.treeview_disponiveis.get_children():
                self.treeview_disponiveis.delete(item)
            
            for produto in produtos:
                codigo, descricao, quantidade, preco = produto
                self.treeview_disponiveis.insert("", tk.END, values=(
                    codigo,
                    descricao,
                    quantidade,
                    f"R$ {preco:.2f}"
                ))
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao carregar produtos:\n{str(e)}")
    
    def pesquisar_produto(self, event=None):
        termo = self.entry_pesquisa.get().strip()
        
        try:
            self.cursor.execute("""
                SELECT codigo, descricao, quantidade, preco 
                FROM produtos 
                WHERE quantidade > 0 AND (codigo LIKE ? OR descricao LIKE ?)
                ORDER BY descricao
            """, (f"%{termo}%", f"%{termo}%"))
            
            produtos = self.cursor.fetchall()
            
            for item in self.treeview_disponiveis.get_children():
                self.treeview_disponiveis.delete(item)
            
            for produto in produtos:
                codigo, descricao, quantidade, preco = produto
                self.treeview_disponiveis.insert("", tk.END, values=(
                    codigo,
                    descricao,
                    quantidade,
                    f"R$ {preco:.2f}"
                ))
                
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao pesquisar produtos:\n{str(e)}")
    
    def selecionar_produto_disponivel(self, event):
        item = self.treeview_disponiveis.selection()
        if item:
            valores = self.treeview_disponiveis.item(item)["values"]
            self.exibir_produto(valores)
    
    def exibir_produto(self, produto):
        codigo, descricao, quantidade, preco = produto
        preco = float(preco.replace("R$ ", ""))
        
        self.codigo_produto_atual = codigo
        
        self.label_descricao.config(text=descricao)
        self.label_preco.config(text=f"R$ {preco:.2f}")
        self.label_estoque.config(text=str(quantidade))
        self.spin_quantidade.config(to=quantidade)
        self.spin_quantidade.delete(0, tk.END)
        self.spin_quantidade.insert(0, "1")
        
        caminho_imagem = f"imagens/produtos/{codigo}.jpg"
        self.carregar_imagem_produto(caminho_imagem)
    
    def limpar_exibicao_produto(self):
        self.codigo_produto_atual = None
        self.label_descricao.config(text="")
        self.label_preco.config(text="R$ 0.00")
        self.label_estoque.config(text="0")
        self.spin_quantidade.config(to=1)
        self.spin_quantidade.delete(0, tk.END)
        self.spin_quantidade.insert(0, "1")
        self.carregar_imagem_padrao()
    
    def adicionar_a_venda(self):
        if not self.codigo_produto_atual:
            messagebox.showwarning("Aviso", "Selecione um produto primeiro")
            return

        try:
            quantidade = int(self.spin_quantidade.get())
            if quantidade <= 0:
                raise ValueError

            descricao = self.label_descricao.cget("text")
            preco_texto = self.label_preco.cget("text").replace("R$ ", "")
            preco = float(preco_texto)
            codigo = self.codigo_produto_atual

            for item in self.produtos_venda:
                if item['codigo'] == codigo:
                    item['quantidade'] += quantidade
                    item['total'] = item['quantidade'] * item['preco']
                    self.atualizar_subtotal()
                    return

            novo_item = {
                'codigo': codigo,
                'descricao': descricao,
                'quantidade': quantidade,
                'preco': preco,
                'total': quantidade * preco
            }
            self.produtos_venda.append(novo_item)
            self.atualizar_subtotal()

        except ValueError:
            messagebox.showerror("Erro", "Quantidade inválida")
    
    def atualizar_subtotal(self):
        subtotal = sum(item['total'] for item in self.produtos_venda)
        self.subtotal.set(subtotal)
        self.label_subtotal.config(text=f"R$ {subtotal:.2f}")
        self.calcular_troco()
    
    def calcular_troco(self, event=None):
        try:
            recebido = float(self.total_recebido.get())
            troco = recebido - self.subtotal.get()
            self.troco.set(max(0, troco))
            self.label_troco.config(text=f"R$ {self.troco.get():.2f}")
        except:
            self.troco.set(0)
            self.label_troco.config(text="R$ 0.00")
    
    def finalizar_venda(self):
        if not self.produtos_venda:
            messagebox.showwarning("Aviso", "Nenhum produto adicionado à venda")
            return
        
        if self.total_recebido.get() < self.subtotal.get():
            messagebox.showwarning("Aviso", "Valor recebido é menor que o total da venda")
            return
        
        try:
            self.conn.execute("BEGIN TRANSACTION")
            
            self.cursor.execute("""
                INSERT INTO vendas (data, total, recebido, troco)
                VALUES (datetime('now'), ?, ?, ?)
            """, (self.subtotal.get(), self.total_recebido.get(), self.troco.get()))
            
            venda_id = self.cursor.lastrowid
            
            for item in self.produtos_venda:
                self.cursor.execute("""
                    INSERT INTO itens_venda (venda_id, produto_codigo, produto_descricao, quantidade, preco_unitario, total)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (venda_id, item['codigo'], item['descricao'], item['quantidade'], item['preco'], item['total']))
                
                self.cursor.execute("""
                    UPDATE produtos SET quantidade = quantidade - ?
                    WHERE codigo = ?
                """, (item['quantidade'], item['codigo']))
            
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")
            self.cancelar_venda()
            self.carregar_produtos_disponiveis()
            
        except sqlite3.Error as e:
            self.conn.rollback()
            messagebox.showerror("Erro", f"Falha ao registrar venda:\n{str(e)}")
    
    def cancelar_venda(self):
        self.produtos_venda = []
        self.subtotal.set(0)
        self.total_recebido.set(0)
        self.troco.set(0)
        self.limpar_exibicao_produto()
        self.entry_pesquisa.delete(0, tk.END)
        self.entry_pesquisa.focus()
    
    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()