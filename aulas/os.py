import os

os.chdir('C:\\teste')
print(f'DIRETORIO ATUAL: {os.getcwd()}')

padrao_nome = input('qual o padrão de nomes de arquivos a usar (sem extensão)?')

for contador, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = padrao_nome + ' ' + str(contador*2)
        nome_novo = f"{nome_arq} {exten_arq}"
        os.rename(arq, nome_novo)
        print(f'\n ARQUIVOS RENOMEADOS.')