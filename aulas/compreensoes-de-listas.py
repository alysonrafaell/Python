numeros = [1,4,78,23,12,3,4,5]

quadrados = [num ** 2 for num in numeros]
print(quadrados)

# criar uma lista de numeros pares entre 0 a 10
pares = [num for num in range(21) if num%2 == 0 ] 
print(f'numeros pares são eles:  {pares}')


soma = 0
n = int(input('digite um numero: '))
lista = [i for i  in range(1, n+1)]
soma = sum(lista)
print(soma)
                  
                  
# quantidade de vogais no texto
frase = 'Se você viaja para o passado, esse passado se torna seu futuro, e seu presente anterior se torna o passado, que agora não pode ser mudado pelo seu novo futuro'
vogais = ['a', 'e', 'i', 'o', 'u', 'ã', 'ê',]

lista_vogais = [v for v in frase if v in vogais]
print(f'a frase possui {len(lista_vogais)} vogais:')
print(lista_vogais)
                        
                        
# distributiva entre valores de duas linhas
distributiva = [k*m for k in [2,3,5] for m in [10,20,30]] 
print(distributiva)                              

n = int(input('digite: '))
dobro = [k for k in range(11)]

print(dobro)