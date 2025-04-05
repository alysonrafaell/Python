#DICIONARIOS
elemento = {
    'z':3,
    'nome':'litio',
    'grupo': 'metais alcalinos',
    'densidade': 0.534
}
print(f'elemento: ', {elemento['nome']})
print(f'elemento: ', {elemento['grupo']})
print(f'o dicionario possui: {len(elemento)}')

# atualizar uma entrada:
elemento['grupo'] = 'alcalinos'
print(elemento)

# adicionar uma entrada 
elemento['periodo'] = 1
print(elemento)

# exclusao de itens em dicionarios
del elemento['periodo']
print(elemento)

# apagar todos os itens
# elemento.clear()
# print(elemento)

# #apagar tudo da memoria
# del elemento
# print(elemento)

#RETORNA CHAVES E VARIAVEIS:
print(elemento.items())
for i in elemento.items():
    print(i)

# RETORNA AS CHAVES, QUE TEM UMA VARIAVEL DENTRO: 
print(elemento.keys())
for i in elemento.keys():
    print(i)
    
# RETORNA VALORES: 
print(elemento.values())
for i in elemento.values():
    print(i)
    
for i,j in elemento.items():
    print(f'{i}:{j}')