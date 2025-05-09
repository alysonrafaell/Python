class Casa:
    def house(self,qts_pessoas,veiculos):
      print(f'sua casa tem quantas pessoas?: {qts_pessoas}')
      print(f'quantos veiculos tem sua casa?: {veiculos}')
    
    def abrir_porta(self):
        print("A porta foi aberta.")

    def fechar_janela(self):
        print("A janela foi fechada.")
        
minha_casa = Casa()
minha_casa.house(4, 2)         # Chama o método house
minha_casa.abrir_porta()       # Chama o método abrir_porta
minha_casa.fechar_janela()     # Chama o método fechar_janela
