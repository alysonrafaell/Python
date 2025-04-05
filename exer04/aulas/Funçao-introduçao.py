# FUNÇÕES
# MODULARIZAÇÃO, REÚSO DE CODIGO, LEGIBILIDADE

# def  <nome_função> ([argumentos])
#     <instruçoes>
# funçao sem parametros
def mensagem ():
    print(f'óla, meu amigo')
    print(f'óla,')
mensagem()

# função com parametros

def soma (num1, num2):
    print(f'a somma dos dois numeros {num1} e {num2} é {num1*num2}')

soma(40,1.5)

def mutl(x,y):
    return x*y
    
e = print('digite dois numeros.')
a = int(input('primeiro numero: '))
b = int(input('segundo numero: '))
c = mutl(a,b)
print(f'soma dos produtos {a} e {b} = {c}')

def divi (s,l):
    if l != 0:
        return s/l
    else: 
        return 'nao divisivel'

a = int(input('digite um numero: '))
b = int(input('digite um numero: '))
     
r=divi(a,b)
print(f'{a} dividido por {b} é igual a {r}')

def quadrado (val):
    quadrados = []
    for x in val:
        quadrados.append(x**2)
    return quadrados

def contar(num=11, caractere = "+"):
    for i in range(1,num):
        print(caractere)


if __name__ == '__main__':
    # valores = [2,4,6,7,8,9]
    # resultados = quadrado(valores)
    # for i in resultados:
    #     print(i)
    contar(9,"*")