aluno = {}
soma = 0

aluno['nome'] = str(input('Digite seu nome: '))

for i in range(1,5):
    
    nota= aluno['media'] = float(input(f'Digite sua primeira nota {i}: '))
    soma += nota
    if aluno['media'] >= 6:
        aluno['Situação'] = print('Aprovado')
    elif aluno['media'] >= 5.5:
        aluno['Situação'] = print('Recuperação')
    else:
        aluno['Situação'] = print('Reprovado')
        
aluno['media'] = soma/4
print("\n--- Resultado ---")

for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}") 
# print(f"Média: {aluno['media']:.2f}")
    