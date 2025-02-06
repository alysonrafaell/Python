# SIMPLES COMPOSTO ENCADEADO


n1= float(input(" digite a sua primeira nota: "))

n2= float(input(" digite sua segunda nota: "))

n3= float(input(" digite a sua primeira nota: "))

n4= float(input(" digite sua segunda nota: "))

resultado = (n1+n2+n3+n4)/4

if(resultado >= 7.0 ):
    print(f"parabens voce passou {resultado}")
elif(resultado >= 5.0):
    print(f"você está na recuperação. {resultado}")
else:
    print(f"reprovado {resultado}")
     
 



