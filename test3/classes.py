class Vendedor():
    def __init__(self,nome):#CRIA UM VENDENDOR, DENTRO DO () COLOCAR OQ PRECISA PARA CRIAR VENDENDOR, POR EXEMPLO SO PRECISA DE NOME.
        
        #AQUI QUE PRECISA DA CARACTERISTICA, TIPO: VENDENDOR ELE TEM NOME E VENDAS(META).
        self.nome = nome
        self.venda = 0
        
    def vendeu(self,venda):
        self.venda = venda
            
    def bateu_meta(self, meta):
        if self.venda > meta:
             print(self.nome, "Parabéns, você bateu a meta.")
        else:
            print(self.nome, ", Não bateu a meta prevista.")