carro = 'f'
porta = 'f'
 
aviso = (carro == 'a' or porta == 'f')

print(aviso)

num = 0 
while (num < 10):
    num += 1
    print(num)
    
planeta = None

while True:
    print("Digite nomes de plenetas e se quiser sair do loop digite x.")
    planeta = input()
    if planeta == 'x' or planeta == 'X':
        break
         
    
