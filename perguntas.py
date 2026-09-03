from Utilidades.números import leia_int

def linha():
    """Função para imprimir uma linha na tela para organizar 
    as informações"""
    print("\033[97m-=-\033[m" * 20)
    
def escolha_usuário(número):
    """Função para validar a escolha do usuário.
    Recebe um inteiro que é digitado pelo usuário.
    Retorna um valor booleano."""

    #Verificando se a opção encontra-se no intervalo de 1 a 4.
    #Tratamento de dados simples que retorna um booleano 
    if número < 1 or número > 4:
        print("\033[31mOpção inválida! Digite uma opção entre 1 e 4!\033[m")
        return False
    else:
        return True
    

def pergunta_1():
    """Função para a primeira pergunta. Retorna um inteiro 
    que representa a pontuação do Jogador."""

    #Lista de opções 
    opções = ("Chris Redfield", "Claire Redfield", "Leon S. Kennedy", "Tiririca")

    #Criando uma variável para armazenar a escolha certa 
    certa = 0

    #Loop da pergunta, só termina quando conseguir uma resposta válida 
    while True:

        #Mostrando a pergunta na tela
        print("\033[36mQual é o nome do personagem principal do Resident Evil 4 original?\033[m")

        #Mostrando uma linha para organizar as informações 
        linha()

        #Loop for para mostrar as opções e guardar a opção correta 
        for indice, valor in enumerate(opções):

            #Determinando a resposta correta como 'Leon S. Kennedy'
            if valor == 'Leon S. Kennedy':

                #Guardando a resposta correta e somando um ao índice para coincidir
                # com a resposta do usuário 
                certa = indice + 1

            #Mostrando as opções na tela
            print(f"\033[34m{indice + 1} - {valor}\033[m")

        #Imprimindo uma linha para organizar as informações 
        linha()

        #Chamando a função leia_int() para validar a escolha do usuário 
        escolha = leia_int("\033[33mQual é a resposta correta? Sua resposta: \033[m")

        #Imprimindo uma linha para organizar as informações 
        linha()

        #Validando uma segunda vez 
        validação = escolha_usuário(escolha)

        #Verificando se a validação retornou True e se a resposta do usuário é correta
        if validação and escolha == certa:
            return 3
        if validação and escolha != certa:
            return 1
            
def pergunta_2():
    """Função para trabalhar a segunda pergunta.
    Retorna um valor inteiro."""

    #opções
    opções = ("Broken Butterfly", "Standard Handgun", "Red 9", "Punisher")

    #Criando a variável que vai armazenar a resposta correta 
    certa = 0

    #Mostrando a pergunta 
    print("\033[36mQual é a arma mais forte do jogo?\033[m")

    #Mostrando uma linha na tela para organizar as informações 
    linha()

    #Loop for para mostrar as opções na tela e guardar a resposta correta 
    for indice, valor in enumerate(opções):

        #Determinando a resposta correta como 'Broken Betterfly'
        if valor == "Broken Butterfly":

            #Guardando o índice da resposta correta e somando um
            certa = indice + 1

        #Mostrando as opções na tela
        print(f"\033[34m{indice + 1} - {valor}\033[m")

    #Mostrando uma linha na tela para organizar as informações 
    linha()

    #Chamando a função leia_int() para validar a resposta do usuário 
    escolha = leia_int("\033[33mQual é a resposta correta? Sua resposta: \033[m")

    #Mostrando uma linha na tela para organizar as informações 
    linha()

    #Validando uma segunda vez
    validação = escolha_usuário(escolha)

    #Testando se a função escolha_usuário() retornou True e
    # testando a resposta do usuário 
    if validação and escolha == certa:
        return 3
    if validação and escolha != certa:
        return 1
            
def pergunta_3():
    """Função para trabalhar a terceira pergunta.
    Retorna um valor inteiro."""

    #Opções
    opções = ("Claire Redfield", "Ashley Graham", "Xuxa Meneghel", "Ada Wong")

    #Criando a variável que vai guardar a resposta correta 
    certa = 0

    #Mostrando a pergunta na tela 
    print("\033[36mQuem você tem que resgatar no jogo?\033[m")

    #Mostrando uma linha na tela para organizar as informações 
    linha()

    #Loop for para mostrar as opções na tela e guardar a resposta correta 
    for indice, valor in enumerate(opções):

        #Determinando a resposta correta como 'Ashley Grahan'
        if valor == "Ashley Graham":

            #Guardando o índice da resposta correta e somando um ao índice 
            certa = indice + 1

        #Mostrando as opções na tela 
        print(f"\033[34m{indice + 1} - {valor}\033[m")

    #Mostrando uma linha na tela para organizar as informações 
    linha()

    #Chamando a função leia_int() para validar a escolha do usuário 
    escolha = leia_int("\033[33mQual é a resposta correta? Sua resposta: \033[m")

    #Mostrando uma linha na tela para organizar as informações 
    linha()

    #Validando uma segunda vez 
    validação = escolha_usuário(escolha)

    #Testando se a validação retornou True e se a escolha do usuário é correta 
    if validação and escolha == certa:
        return 3
    if validação and escolha != certa:
        return 1
            
def pergunta_4():
        opções = ("Verdugo", "Dr. Salvador", "El gigante", "Salazar")
        certa = 0
        print("\033[36mQual chefão precisa de nitrogênio para ser derrotado?\033[m")
        linha()
        for indice, valor in enumerate(opções):
            if valor == "Verdugo":
                certa = indice + 1
            print(f"\033[34m{indice + 1} - {valor}\033[m")
        linha()
        escolha = leia_int("\033[33mQual é a resposta correta? Sua resposta: \033[m")
        linha()
        validação = escolha_usuário(escolha)
        if validação and escolha == certa:
            return 3
        if validação and escolha != certa:
            return 1

def pergunta_5():
    opções = ("México", "Brasil", "Japão", "Espanha")
    certa = 0
    print("\033[36mEm qual país se passa o jogo?\033[m")
    linha()
    for indice, valor in enumerate(opções):
        if valor == "Espanha":
            certa = indice + 1
        print(f"\033[34m{indice + 1} - {valor}\033[m")
    linha()
    escolha = leia_int("\033[33mQual é a resposta correta? Sua resposta: \033[m")
    linha()
    validação = escolha_usuário(escolha)
    if validação and escolha == certa:
        return 3
    if validação and escolha != certa:
        return 1