# num1= int(input ("Digite um numero: "))
# num2 =int(input("Digite um numero: "))


# print(num1+num2)
# x=y=z =bool
# n1=n2=0
# print("Digite um numero: ")
# n1 = int(input())
# n2 = int(input("Digite um numero: "))

# x = n1 == n2
# print("São iguais?","\n", x )
# z = n1 > n2
# print(n1,"é maior que", n2, "?", z, "\n")

import random

numero_aleatorio = random.randint(-10,10)
numero2 = random.randint(-5,5)
x=y=z=bool
n1=n2=int
print("Digite um numero: ")
print(numero_aleatorio)
print("Digite um numero: ")
print(numero2)

x=numero_aleatorio==numero2
print("São iguais?","\n",x)

z= numero_aleatorio>numero2
print(numero_aleatorio, "é maior que ", numero2,"?", "\n", z)

y = numero_aleatorio!=numero2
print(numero_aleatorio, "é diferente de ", numero2,"?","\n",y,"\n","sendo a diferença de ", numero_aleatorio-numero2)


