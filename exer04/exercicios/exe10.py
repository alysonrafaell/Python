print(f'DIGITE O SUAS NOTAS NO 1º,2º,3º E 4º.')

soma = 0

for i in range(4):
    numero = float(input(f'digite a nota da unidade {i + 1}: '))
    
    soma += numero

print(f'a média da soma das unidades é: {soma} e {soma/4}')





