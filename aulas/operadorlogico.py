idade = 18
altura = 1.80

resultado = (idade >= 18) and (altura >= 1.80)
mensagem = "pode participar do evento? " +  str(resultado)

print( mensagem)

 #programa de disparo de alarme

porta = 'f'
janela = 'f'

alarme = (porta == "a") or (janela == 'a')
msg = "SUA CASA ESTA SENDO ENVADIDA !  " + str(alarme)

print(msg)


tem_dinheiro = True
tem_dinheiro = not tem_dinheiro
msg = ' Tem dinheiro? ' + str(tem_dinheiro)

print(msg)