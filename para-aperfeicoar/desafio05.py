import random

numeros = []

def sortear():
    global numeros
    numeros = random.sample(range(1,30),5)
    print(f'numeros sorteados: {numeros}')

def somaPar():
    soma = sum(num for num in numeros if num%2 == 0)
    print(f'soma os numeros pares: {soma}')

sortear()  
somaPar()  
