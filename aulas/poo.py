# orientação a objetos: paradigma da programação/ linguagem multiparadigma
# classes de objetos
class  Veiculo:
    def roda(self):
        #AQUI DENTRO É O METODO
        print(f'tenho rodas.')
    # INIT: CONSTRUTOR
    def __init__(self, nome, cor):
        self.__nome = nome
        self.__cor = cor
       
        self.__registro = None
    #GETTER: SERVE PARA ACESSAR OS ATRIBUTOS PRIVADOS OU ACESSAR OUTROS ELEMENTOS NA CLASS
    def get_cor(self):
        print(f"a cor do carro é: {self.__cor}\nnome: {self.__nome}")
    
    def get_registro(self):
        return self.__registro
    
    #SETTER: GRAVA UM DADO DENTRO DE UMA CLASS/OBJETO
    def set_registro(self, registro): # PORQUE FORNECE UM DADO PARA O PARAMETRO
        self.__registro= registro
class  Carro(Veiculo):
    # metodo init vai ser herdado
    def movimentar(self):
        print('sou carro loko.')
        
class Motocicleta(Veiculo):
        def movimentar(self):
            print(f'TALVEZ EU SEJA UMA MOTO OU UM BIKE MOTORIZADA')
            
class Aviao(Veiculo):
    def __init__(self, nome, cor, categoria):
         super().__init__(nome, cor)    
         self.__categoria = categoria
         
    def get_categoria(self):
        return self.__categoria
    
    def movimentar(self):
        print('TO VOANDO ALTO')
    
if __name__ =="__main__":
        my_vehicle= Veiculo("fusca",'azul'    )
        my_vehicle.roda()
        my_vehicle.get_cor()
        my_vehicle.set_registro("382828-3")
        print(f'registro: {my_vehicle.get_registro()}\n')
        
        my_car = Carro('audi', "branco\n")
        my_car.movimentar()
        my_car.get_cor()
        
        seu_carro = Carro("audi", "preto\n")
        seu_carro.movimentar()
        seu_carro.get_cor()
        
        moto = Motocicleta('dinka-double-g', 'cromada\n')
        moto.movimentar()
        moto.get_cor()
        
    
        meu_aviao = Aviao('jatinho','branco','luxuoso\n')
        meu_aviao.movimentar()
        meu_aviao.get_cor()
        print(f'categoria: {meu_aviao.get_categoria()}')