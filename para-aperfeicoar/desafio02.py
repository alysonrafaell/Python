matriz = [0,0,0], [0,0,0], [0,0,0]
# GUANABARA SALVOU
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite seu numero [{l},{c}]: '))
print('*' * 22)

for l in range (0,3):
    for c in range(0,3):
        print(f'[{matriz [c] [l]:^5}]', end = "")
        
    print()
print('*' * 22)
