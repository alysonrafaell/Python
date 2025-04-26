def contador(inicio,fim,passo):

 if inicio < fim:
     for i in range(inicio,fim + 1, passo):
         print(i)
 else:
        for i in range(inicio,fim - 1,-passo):
            print(i)
            
contador(1,10,1)
contador(10,0,2)
contador(-10,0,1)#contagem personalizada
    