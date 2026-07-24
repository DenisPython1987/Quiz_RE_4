from Utilidades.números import leia_int

def linha():
    print("\033[97m-=-\033[m" * 20)
    
def escolha_usuário(número):
    if número < 1 or número > 4:
        print("\033[31mOpção inválida! Digite uma opção entre 1 e 4!\033[m")
        return False
    else:
        return True
    

def pergunta_1():
    opções = ("Chris Redfield", "Claire Redfield", "Leon S. Kennedy", "Tiririca")
    certa = 0
    while True:
        print("\033[36mQual é o nome do personagem principal do Resident Evil 4 original?\033[m")
        linha()
        for indice, valor in enumerate(opções):
            if valor == 'Leon S. Kennedy':
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
            
def pergunta_2():
        opções = ("Broken Butterfly", "Standard Handgun", "Red 9", "Punisher")
        certa = 0
        print("\033[36mQual é a arma mais forte do jogo?\033[m")
        linha()
        for indice, valor in enumerate(opções):
            if valor == "Broken Butterfly":
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
            
def pergunta_3():
        opções = ("Claire Redfield", "Ashley Graham", "Xuxa Meneghel", "Ada Wong")
        certa = 0
        print("\033[36mQuem você tem que resgatar no jogo?\033[m")
        linha()
        for indice, valor in enumerate(opções):
            if valor == "Ashley Graham":
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