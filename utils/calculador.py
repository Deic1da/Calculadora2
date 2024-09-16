# utils/calculador.py

def Calculador(equacao):
    operadores = "+-*/"
    resultado = None
    numero_direita = None
    numero_esquerda = None
    sinal = None

    divisao = equacao.count("/")
    multiplicacao = equacao.count("*")
    somar = equacao.count("+")
    subtrair = equacao.count("-")

    for i in operadores:
        equacao = equacao.replace(i, f" {i} ")
    
    equacao = equacao.split()

    while multiplicacao != 0:
        for i in range(len(equacao)):
            if i > 0 and i < len(equacao) - 1:
                if equacao[i] == "*":
                    sinal = equacao[i]
                    numero_direita = float(equacao[i + 1])
                    numero_esquerda = float(equacao[i - 1])
                    resultado = numero_esquerda * numero_direita
                    equacao[i - 1:i + 2] = [resultado]
                    multiplicacao = multiplicacao-1
                    break
    while divisao != 0:
        for i in range(len(equacao)):
            if i > 0 and i < len(equacao) - 1:
                if equacao[i] == "/":
                    sinal = equacao[i]
                    numero_direita = float(equacao[i + 1])
                    numero_esquerda = float(equacao[i - 1])
                    resultado = numero_esquerda / numero_direita
                    equacao[i - 1:i + 2] = [resultado]
                    divisao = divisao-1
                    break

    while somar+subtrair != 0:
        for i in range(len(equacao)):
            if i > 0 and i < len(equacao):
                if equacao[i] == "+":
                    sinal = equacao[i]
                    numero_direita = float(equacao[i + 1])
                    numero_esquerda = float(equacao[i - 1])
                    resultado = numero_esquerda + numero_direita
                    equacao[i - 1:i + 2] = [resultado]
                    somar = somar-1
                    break
                elif equacao[i] == "-":
                    sinal = equacao[i]
                    numero_direita = float(equacao[i + 1])
                    numero_esquerda = float(equacao[i - 1])
                    resultado = numero_esquerda - numero_direita
                    equacao[i - 1:i + 2] = [resultado]
                    subtrair = subtrair-1
                    break

    return equacao[0]
