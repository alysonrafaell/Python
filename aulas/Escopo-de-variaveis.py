# ESCOPO GLOBAL E ESCOPO LOCAL

var_global = 'curso completo de python'
def escreve_texto( ):
    # var_global = 'macaco sinistro' ISSO VAI SER UMA VARIAVEL LOCAL NAO GLOBAL
    global var_global # ISSO AQUI PEGA A VARIAVEL GLOBAL E POE DENTRO DA FUNÇAO
    var_local = 'alyson rafael'
    print(f'var global  {var_global}')
    print(f'var local   {var_local}') # e sim aqui
    
if __name__ == "__main__":
    print('executar a função escrever_texto')
    escreve_texto()
    
    print('tenta acessar as variaveis diretamente')
    print(f'var global  {var_global}')
    # print(f'var local   {var_local}')#variavel local nao esta aqui 
    