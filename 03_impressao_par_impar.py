quantidade_de_vezes = int(input("Digite a quantidade de vezes que você gostaria de números pares ou ímpares: "))
tipo_de_numero = input("Você gostaria de números Pares ou Ímpares? ").lower()

opcoes = ["pares","impares", "ímpares"]

while tipo_de_numero not in opcoes:
    tipo_de_numero = input("Resposta inválida! Digite somente 'Pares' ou 'Ímpares': ").lower()

numero = 1
contador = 0

while contador < quantidade_de_vezes:
    if (tipo_de_numero == "pares" and numero % 2 == 0) or (tipo_de_numero == "ímpares" and numero % 2 != 0):
        print(numero)
        contador += 1
    numero += 1