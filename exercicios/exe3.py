'OQUE EU FIZ E NAO DEU CERTO'
palavras = ['python','asimov', 'codigo', 'web','programação']

print(min(palavras))
print(max(palavras))

'CHATGPT'
palavras = ['python', 'asimov', 'codigo', 'web', 'programação']

# Encontrando a palavra com o comprimento mínimo (menor palavra)
min_palavra = min(palavras, key=len)

# Encontrando a palavra com o comprimento máximo (maior palavra)
max_palavra = max(palavras, key=len)

print("Valor mínimo (menor palavra):", min_palavra)  # 'web'
print("Valor máximo (maior palavra):", max_palavra)  # 'programação'
