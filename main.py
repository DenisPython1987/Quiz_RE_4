from Utilidades.apresentação import cabeçalho
import perguntas
import resultado

soma = 0

cabeçalho("QUIZ RESIDENT EVIL 4")

alternativa_1 = perguntas.pergunta_1()
soma += alternativa_1
alternativa_2 = perguntas.pergunta_2()
soma += alternativa_2
alternativa_3 = perguntas.pergunta_3()
soma += alternativa_3
alternativa_4 = perguntas.pergunta_4()
soma += alternativa_4
alternativa_5 = perguntas.pergunta_5()
soma += alternativa_5

cabeçalho("RESULTADOS")

print(f"\033[36m{resultado.verifica(soma)}\033[m")

cabeçalho("VOLTE SEMPRE!!!")