lista = [0,1,2,3,4,6,7,8,9]
print(lista[2])

for numero in range(10): # SEMPRE ACABA NO ANTERIOR A ELE
    print(numero)
    
nome = input('digite seu nome:')
for x in range(11):
    print (f'{x+0} {nome}')
    # RANGE FUNCIONA POR 3 PARAMETROS: (VALOR INICIAL, VALOR FINAL E INCREMENTO )
for x in range (2,20,4):
    print(x)
    
pedras = ('rubi','esmeralda', 'safira', 'quartzo', 'diamante', 'ouro')

for pedra in pedras:
    if pedra == 'quartzo':
        continue
    print(pedra)

pessoas = ('alyson', 'rafael', 'alefe', 'gabriel')
    
for pessoas in pessoas:
    if pessoas == 'rafael':
        continue
    print(pessoas)