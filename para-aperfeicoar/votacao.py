def voto(ano_nascimento):
    ano_atual = 2025
    idade = ano_atual - ano_nascimento # PARA DESCOBRIR A IDADE

    if idade < 16: # MENOR DE IDADE
        return 'proibido.'
    elif 18 <= idade <= 70: # MAIOR OU IGUAL A 18 E MENOR OU IGUAL A 70
        return 'obrigatorio.'
    else: # MAIOR QUE 70
        return 'facultativo.'

ano = int(input("ano de nascimento: "))
res = voto(ano)
print(f'SEU VOTO É: {res}')


  


    
        
        
        
    