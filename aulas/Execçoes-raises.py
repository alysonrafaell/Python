from math import sqrt

if __name__=='__main__':
    while True:
        try: 
            num = int(input('digite um numero positivo: '))
            if num < 0:
                raise   ArithmeticError
            else:
                print(f'a raiz quadrada de {num} = {sqrt(num)}')
            break
        except ArithmeticError:
            print('digitou o numero errado.')
        finally: 
            print('fim do programa.')
            

