# user = input(f'digite 5 bebidas favoritas: ')
# bebidas = list(user)
# for bebida in bebidas:
#    sorted(bebidas)
#    print(f'\nsuas bebidas são: ',bebida)

bebidas = []
print(f'\nAs suas 5 melhores bebidas.')
for i in range(5): # IN RANGE (UM NÚMERO) REFERECE A QUANTIDADE DE VEZES QUE ELE RODA

    print(f'\nSua bebida: ')
    bebida = input()
    bebidas.append(bebida)
   
bebidas.sort()   
print(f'\nSuas bebidas são:{bebidas}')

    
print(f'\nfinish')