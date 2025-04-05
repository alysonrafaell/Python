# SET 
planeta_anao = {'plutao','ceres','eris','haumea', 'makemake'} 
print(len(planeta_anao))
print('lua' not in planeta_anao)
for i in planeta_anao:
    print(i.title())

astros = ['lua','venus','sirius', 'marte', 'lua']
print(astros)
astros_set = set(astros)
print(astros_set)


astros1 = {'lua','venus','sirius', 'marte','io'}
astros2 = {'lua','venus','sirius',  'marte', 'lua', 'cometa de Halley'}
print(astros1 | astros2) 
# OU
print(astros1.union(astros2))

#intercesçao
print(astros1 & astros2)
print(astros1.intersection(astros2))

#diferença simetrica:
print(astros1 ^ astros2)
astros1.add('urano')
astros1.add('sol')
print(sorted(astros1))
astros1.pop()
print(astros1)
