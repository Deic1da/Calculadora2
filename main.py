from utils.calculador import *

print("As equações são:\nSoma (+)\nSubtração (-)\nDivisão (/)\nMultiplicação (*)")
equacao = input("Digite aqui: ")

equacao = Calculador(equacao)

print(f"Resultado = {equacao}")