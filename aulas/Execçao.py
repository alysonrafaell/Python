# EXECÇÃO É UM ERRO QUE  REPRESENTA UM ERRO QUE OCORREU AO EXECUTAR O PROGRAMA
# BLOCOS: TRY ..... EXCPET
# n1 = int(input('digite um numero: '))
# n2 = int(input('digite um numero: '))

# try:
    
#     r = round(n1/n2,2)

# except ZeroDivisionError:
#     print('nao é possivel dividir por zero')
# else:    
#     print(r)





def exemplo_de_erro_de_valor(k,j):
        round(k/j,2)
        
if __name__=='__main__':
        while True:
            try:
                n1 = int(input('digite um numero: '))
                n2 = int(input('digite um numero: '))
                break
            except ValueError:
                print(f'erro de valor, tente novamente')
        try:
            r = round(n1/n2,2)
        except ZeroDivisionError:
            print(f'nao é possivel dividir por zero.')
        except:
            print('nao deu certo>')
        else:
            print(r)
        finally:
            print('acabou o programa.')