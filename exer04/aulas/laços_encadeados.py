for cont_ex in range(1,6): #CONTE_EX É CONTADOR EXTERNO
    print(f'\nrodada: {cont_ex}') # ESSE \N É PARA QUEBRAR LINHA
    for cont_in in range(3,0,-1): #CONT_EX É CONTADOR INTERNO
        print(f'Valor: {cont_in}')
print('FIM DOS LAÇOS')

"MUITO IMPORTANTE ISSO"

import random

for x in range(1,6):
    print(f'\nRODADA: {x}')
    for z in range(5):
        num = random.randint(1,102)
        print(f'Valor: {num}')