#SÃO IMUTAVEIS
halogenios = ('f', 'cl', 'br', 'i', 'at')
gases_nobres = ('he', 'ne', 'ar', 'xe', 'kr', 'rn')
elementos = halogenios + gases_nobres
t1 =(3,4,4,5,6,7,8,9,0)
print(sum(t1))

#OPERAÇOES NÃO DISPONIVEIS EM TUPLAS: .SORT(), .append(), .reverse(), .pop() .....

for elemento in elementos:
    print(f'elemento  quimicos: {elemento}')

grupo17 = list(halogenios)
print(grupo17)
grupo17[0] = 'H'

grupo1 = ['li','na','k','rb','cs','fr']
alcalinos = tuple(grupo1)
print(alcalinos)
print(sorted(alcalinos))
