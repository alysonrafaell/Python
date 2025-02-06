class Vendedor():
    def __init__(self,nome):#CRIA UM VENDENDOR, DENTRO DO () COLOCAR OQ PRECISA PARA CRIAR VENDENDOR, POR EXEMPLO SO PRECISA DE NOME.
        
        #AQUI QUE PRECISA DA CARACTERISTICA, TIPO: VENDENDOR ELE TEM NOME E VENDAS(META).
        self.nome = nome
        self.venda = 0
        self.quantidade_minima = 50
        
        #ATRIBUTOS:
    def vendeu(self,venda): 
        self.venda = venda
    def caixas(self,quantidade_minima):
        self.quantidade_minima = quantidade_minima
        if self.quantidade_minima > 50:
            print(self.nome,f"Parabéns você vendeu {self.quantidade_minima}, tuuuudooo.")
        elif self.quantidade_minima == 25:
            print(self.nome, f"Você vendeu {self.quantidade_minima} ,a metade pelo menos 😒")
        else: 
            print(self.nome,f"VOCÊ TEM QUE VENDER METADE PELO MENOS !!!!!, SÓ {self.quantidade_minima} NÃO É O SUFICIENTE.")
        
        
            
    def bateu_meta(self, meta):
        if self.venda > meta:
             print(self.nome, "Parabéns, você bateu a meta.")
        else:
            print(self.nome, ", Não bateu a meta prevista.")