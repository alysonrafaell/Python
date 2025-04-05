print('tentando algo novo.')
def contar(num = 8, caractere= "+"):
    for i in range(8):
        print(caractere)
        
if __name__ == '__main__':
    contar(10, "*")
    


x = 6
y = 7
z = 2

def soma_mult(a,b, c =  0):
    num = ()
    if c == 0:
        return a*b
    else:
        return a+b+c
    

if __name__ == '__main__':
    res = soma_mult(x,y,z)
    print(res)
    


    