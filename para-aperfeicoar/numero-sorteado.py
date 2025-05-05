from random import randint # NUMERO ALEATORIO
from time import sleep
from operator import  itemgetter
jogo = {'jogador01':randint(1,6),  # UM DADO TEM SEIS LADOS
         'jogador02': randint(1,6),
         'jogador03': randint(1,6),
         'jogador04':randint(1,6)}

print('Valores sorteados: ')
for numero, jogado in jogo.items():
    print(f'{numero} tirou {jogado} no dado. ')
    sleep(1) # PAUSA POR 1 SEGUNDO
    
ranking= {}
ranking = sorted(jogo.items(),key= itemgetter(1), reverse=True)
print('\n---resultado---')
for i,v in enumerate (ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    