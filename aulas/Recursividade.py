# RECURSIVIDADE 

# FORMULA GERAL PARA O FATORIAL: 
# FATORIAL(NUM) = 1, SE NUM = 0 OU SE NUM = 1 ' CASO-BASE', É OQ FINALIZA O PROGRAMA
# FATORIAL(NUM) = NUM * FATORIAL( NUM - 1), PARA NUM > 1 CASO RECURSIVO
# FATORIAL DE  4
# 4! -> 4 * FATORIAL (3) = 4 * 3 * FATORIAL (2) =  4 * 3 * 2 * FATORIAL(1= igual a 1) ->
#4! = 4 * 3 * 2 * 1 = 24

def fatorial(numero):
    
        if numero == 0 or numero == 1:
            return 1
        else:
            return numero*fatorial(numero -1)
    
def mostrar_calculo(numero):
    elementos = [str(i) for i in range(numero, 0, -1)]
    expressao = " * ".join(elementos)
    resultado = fatorial(numero)
    print(f"{expressao} = {resultado}")
    return resultado 
    
if __name__ == '__main__':
    
  
    a = int(input('Digite um número: '))
    
    try:    
        resultado = mostrar_calculo(a)  # Chama só uma vez
    
    except RecursionError:
        print('o numero é muito grande ou negativo.')
    else:
        print(f'O fatorial do número {a} é igual a {resultado}')
