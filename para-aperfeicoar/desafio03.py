from datetime import datetime

dados = {}

dados['nome'] = str(input('Digite seu nome: '))
nasc = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados ['ctps'] = int(input('numero da carteira de trabalho(0 não tem): '))
    
if dados['ctps'] != 0:
        dados['contratação'] = int(input('ano de contratação: '))
        dados['salário'] = float(input('salário: R$ '))
        dados['aposentadoria'] = dados ['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
    
print('∬' * 30)
for fim, fin in dados.items():
    print(f'- {fim}: {fin}')
print('∬' * 30)





