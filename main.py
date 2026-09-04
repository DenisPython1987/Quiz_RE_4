from Utilidades.apresentacao import cabecalho
import perguntas
import resultado

#Declarando a variável que irá armazenar a soma de todos os retornos 
soma = 0

#Mosteando um cabeçalho 
cabeçalho("QUIZ RESIDENT EVIL 4")

#Chamando a pergunta 1
alternativa_1 = perguntas.pergunta_1()

#Armazenando o retorno 
soma += alternativa_1

#Chamando a pergunta 2
alternativa_2 = perguntas.pergunta_2()

#Armazenando o retorno 
soma += alternativa_2

#Chamando a pergunta 3
alternativa_3 = perguntas.pergunta_3()

#Guardando o retorno 
soma += alternativa_3

#Chamando a pergunta 4
alternativa_4 = perguntas.pergunta_4()

#Guardando o retorno 
soma += alternativa_4

#Chamando a pergunta 5
alternativa_5 = perguntas.pergunta_5()

#Guardando o retorno 
soma += alternativa_5

#Apresentando um cabeçalho para o resultado 
cabeçalho("RESULTADOS")

#Mostrando o resultado na tela
print(f"\033[36m{resultado.verifica(soma)}\033[m")

#Apresentando a despedida 
cabeçalho("VOLTE SEMPRE!!!")