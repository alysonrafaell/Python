def enviar_convite():
    # Informações do evento
    data = "15 de Fevereiro de 2024"
    local = "Hotel Grand Royale, Avenida das Acácias, 1234, Centro"
    inicio = "19h00"
    termino = "00h00"
    dress_code = "Traje de gala"
    lista_presentes = "Lista de presentes disponível na recepção ou online."

    # Mensagem de convite
    mensagem = f"""
    ----------------------------------------------
    **Convite Especial**
    
    É com imensa honra e grande prazer que o convidamos para uma noite de sofisticação e elegância, destinada a criar memórias inesquecíveis. Este evento, cuidadosamente planejado, reunirá o que há de melhor em requinte e celebração. Sua presença será de extrema importância para tornar esta ocasião ainda mais especial.
    
    **Detalhes do Evento:**
    
    - **Data:** {data}
    - **Local:** {local}
    - **Horário de Início:** {inicio}
    - **Horário de Término:** {termino}
    
    A noite será marcada por momentos de convivência em um ambiente encantador, onde o luxo e a boa companhia estarão em perfeita harmonia. O evento contará com um jantar refinado, acompanhado de música ao vivo e um espaço especialmente preparado para momentos de descontração e troca de ideias.
    
    **Dress Code:** {dress_code}. Pedimos a gentileza de que os convidados se apresentem com vestimenta formal, em concordância com a elegância da ocasião.
    
    Além disso, em vez de presentes tradicionais, optamos por uma {lista_presentes}. Sua contribuição será muito bem-vinda, mas, acima de tudo, sua presença será o maior presente para todos nós.
    
    Agradecemos desde já a sua atenção e estamos ansiosos para celebrar esta noite única ao seu lado.
    
    Com os melhores cumprimentos,
    [BLUE ANGEL]
    ----------------------------------------------
    """

    print(mensagem)

# Chama a função para exibir o convite
enviar_convite()


print("Para prosseguirmos, precisamos saber algumas informações.","\n")
while True:
    entrada = input("Digite sua idade: ")
    if entrada.isdigit():
        idade =int(entrada)
        if idade <18:
            print(f"Idade não autorizada ❌,", idade,"anos.")
            break
        else:
            print(f"Idade autorizada ✅,", idade,"anos.")
            break
    else:
        print("Por favor, digite sua idade sem letras ou caracteres especiais.")
    
    
acompamhantes = input("Quantos acompanhantes? ")
if not acompamhantes.isdigit() or int(acompamhantes) <0:
    print("Por favor, só números e acompanhantes maior ou igual a zero !")
else:
    total_de_pessoas = int(acompamhantes)
    print(f'Seus acompanhantes {total_de_pessoas}',".")
    
    print("\n","Queremos expressar nossa sincera gratidão por ter aceitado nosso convite com tanto carinho. Sua presença fez toda a diferença em nossa celebração, tornando o momento ainda mais especial. Agradecemos de coração e esperamos que tenha se divertido tanto quanto nós!") 