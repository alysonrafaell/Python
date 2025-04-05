import random

print("gera 5 numeros entre um e 50: ")

for num in range(3):
     print(f'\nRODADAS: ')
     for n in range(3):
         num2 = random.randint(1,50)
         print(f'numero gerado {num2}')
num = random.random()
print(f"numero gerado: {round(num*10,3)}")

valor = random.uniform(1,100)
print(f'número: {round (valor,0)}')

l = [2,4,6,9,10,13,14,16,18,20,21,27,33]
n = random.choice(l)
print(f'numero escolhido: {n}')
n = random.sample(l,4)
print(n)

"EMBARALHAR "
print(f'lista original : {l}')
print(f'embaralhar a lista e exibir ela: ')
n = random.shuffle(l)
print(l)