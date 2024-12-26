print("Digite dois numeros para uma das operações a baixo: ")
print ("Digite {1}, para ADIÇÃO")

print ("Digite {2}, para SUBTRAÇÃO ")

print ("Digite {3}, para MULTIPLICAÇÃO ")

print ("Digite {4}, para DIVISÃO")


b = float(input ("Primeiro numero: "))
a = float(input("Segundo numero: "))

opcao = int(input("Escolha sua operação: "))
if opcao == 1:
    result = a + b
    print(f"A adição de {b} + {a} é  = {result}.")
elif opcao == 2:
 result = b - a
 print(f"A subtração de {b} - {a} é = {result}.")
elif opcao == 3:
    result = b*a
    print(f"A multiplicação de {b} x {a} é = {result}")
elif opcao == 4:
  if b < 0:
     print("Erro: não é possivel dividir.")
  elif a <= b:
        result = b/a
        print(f"A divisão de {b} e {a} é = {result}.")
  else:    
      print("denominador maior que o numerodor.")
else:
    print("Opção  inválida, escolha 1 a 4.")

  


