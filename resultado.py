def verifica(número):
    if 5 <= número <= 7:
        return f"Seus conhecimentos são rasos em RE4. Sua nota foi {número}."
    elif 8 <= número <= 11:
        return f"É... parece qe você sabe alguma coisa sobre RE4. Sua nota foi {número}."
    elif 12 <= número <= 15:
        return f"Parabéns! Você conhece RE4! Sua nota foi {número}."