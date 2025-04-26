pessoas = []

for i in range(4):
   nome = input('Digite seu nome: ')
   peso = float(input('Digite seu peso: '))
   pessoas.append({'nome': nome, 'peso': peso})
   
   
pesado  = []
leve = []
for pessoa in pessoas:
    print(f"Nome: {pessoa['nome']}, Peso: {pessoa['peso']}kg")
    
    if pessoa['peso'] > 78.0:
        pesado.append(pessoa)
    else:
        leve.append(pessoa)
        
    
  
  
print(f" total de pessoas: {len(pessoas)}")  

print("\nPESSOAS COM MAIS DE 78KG:")
for pesados in pesado:
    print(f"{pesados['nome']} pesa {pesados['peso']}kg")
    
print("\nPESSOAS COM 78KG OU MENOS:")
for leves in leve:
    print(f"{leves['nome']} pesa {leves['peso']} kg")
    
    

