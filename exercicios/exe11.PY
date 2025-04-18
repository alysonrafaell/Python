planeta = None

while True:
    print("Digite nomes de planetas e se quiser sair do loop digite x.")
    
    planeta = input()
    print(f"Você digitou: '{planeta}'")  # Aqui imprimimos a entrada para ver o que o programa recebe

    if planeta == 'x' or planeta == 'X':
        break
