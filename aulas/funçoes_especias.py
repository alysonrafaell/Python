# Funçoes lambda(ou anonimas)
#Sintaxe:
#Lambda argumentos: expressão


#NUMERO ELEVADO 2
quadrado = lambda x: x**2
for i in range(1,11):
    print(quadrado(i))
    
    
#DESCOBRIR O NUMERO PAR
par = lambda x: x%2 == 0
print(par(23))


#DECOBRIR CELSIUS
f_c = lambda f : (f-32) * 5/9 # transformaçao para celsius
print(f_c(32))


# Função map()
#sintaxe 
#map(funçao, interavel)
num = [1,2,3,4,5,6,7,8]
dobro = map(lambda x: x * 2, num)
print(list(dobro))
#COM STRINGS
palavras = ['python', 'é', 'massa']
maiusculo = list(map(str.upper,palavras ))
frase = ' '.join(maiusculo)
print(frase)

#Função filter()
# Sintaxe
# filter(função, sequência)

def numeros_pares(n):
    return n% 2 ==0

numeros = [1,2,3,4,5,6,7,8,9,10,12,13,14]

num_par = list(filter(numeros_pares, numeros))
print(num_par)


numeros = [1,2,3,4,5,6,7,8,9,10,12,13,14]
num_impar = list(filter(lambda x: x % 2 != 0, numeros))
print(num_impar)

#Função reduce()
#Sintaxe
#reduce(Função, Sequencia, Valor_inicial)
from functools import reduce

def mult(x,y):
    return x*y


num = reduce(mult, numeros)
print(num)

#SOMA CUMULATIVA DOS QUADRADOS  DE VALORES(dos elevados ao quadrado), USANDO EXPRESSÃO LAMBDA
numeros = [1,2,3,4]
#((1²+ 2²)²+3²)²+4²
total = reduce(lambda x, y: x**2 + y**2, numeros)
print(total)