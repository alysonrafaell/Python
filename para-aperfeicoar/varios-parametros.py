def maior(*num): #  " * " VARIOS PARAMENTROS 
    cont = maior = 0
    print('-=' * 30)
    print('//valores passados//')
    for valor in num:
        print(f'{valor}', end=" ")
        
        if cont == 0: # SE O VALOR FOR 0 O MAIOR NUMERO VAI SER ESSE VALOR
            maior = valor
        else:
            if valor > maior: # SE O VALOR FOR MAIOR QUE 0 ELE É REALOCADO NA VARIAVEL VALOR
                maior= valor
        cont+= 1 # SOMA COM MAIS UM NUMERO
    
    print(f'numeros informados: {cont}')
    print(f'maior valor informado: {maior}')
    
if __name__ == "__main__":
    maior(1, 2, 3, 4, 5, 6)
    maior(7,8,90,20,40)
    maior(-10,-50)
    maior(6)
    maior()