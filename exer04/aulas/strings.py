frase = 'vamos aprender python hoje'
palavras= frase.split()
print(palavras[0])
for i in palavras:
    print(i)
for letra in frase:
    print(letra)
    
email = input('dIGITE SEU ENDEREÇO DE EMAIL: ')
arroba = email.find('@')
print(arroba)
usuario = email[0:arroba]
dominio = email[arroba+1:]
print(usuario)
print(dominio)

produtos = 'carbonato de sodio e oxido de zinco'
print('sodio' in produtos)
print('magnesio' in produtos)
item = 'paralelepipedo'
pos = item.find('lele')
print(pos)
pos = item.find('pi')
print(pos)

objetos = 'Pedra Tesoura  Papel'
print(objetos.upper())
print(objetos.lower()) 
print(objetos.capitalize())
print(objetos.title())

suplemento = 'cloreto de magnesio'
novo_suplemento = suplemento.replace('magnesio','zinco')
print(novo_suplemento)
print(suplemento)

frase = '             óla, mundo'
print(frase)
print(frase.lstrip())
print(frase.rstrip())
print(frase.strip())


 