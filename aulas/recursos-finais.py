# troca valores de duas variaveis
var1=1
var2=2
#ordenaçao de algoritimos numericos
var2, var1= var1,var2
print(f'{var1}, {var2}')

#operador condicional ternario

menor=var1 if var1<var2 else var2
print(f"menor valor {menor}")
print(f"Menor valor {(var2,var1)[var1 < var2]}")

#generators
valores = [1,3,5,7,9,11,13,15]
quadrados = (item**2 for item in valores)
print(quadrados)
for valor in quadrados:
    print(valor)
    
#funçao enumerate()
bebidas = ["cafe", "cha", "suco", "refrigerante"]
for i, item in enumerate(bebidas):
    print(f"indice: {i}, item: {item}")
    
temperaturas = [-1,10,5,-3,8,4,-2,-5,7]
total = 0
for i,t in enumerate(temperaturas):
    if  t< 0:
        print(f"temperatura negativa {i}, itens: {t}")   
        

    