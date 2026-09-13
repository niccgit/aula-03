# Escreva um programa em Python que peça as seguintes duas informações do usuário:
#
# Quantidade de vezes (int)
# Tipo de número (par ou ímpar)
#
# O programa deve imprimir na tela os números de acordo com a quantidade de vezes pedida e de acordo com seu tipo.


opcoes_tipo_de_numero = ["pares","ímpares"]


tipo_de_numero = input("Digite que tipo de número você gostaria (Pares ou Ímpares): ").lower()

while tipo_de_numero not in opcoes_tipo_de_numero:
    tipo_de_numero = input("Resposta inválida! Responda somente com 'Pares' ou 'Ímpares'").lower()


qtd_de_vezes = int(input("Digite a quantidade de vezes que esse número deverá ser impresso: "))


numero = 1
contador = 0

while contador < qtd_de_vezes:
    if (tipo_de_numero == "pares" and numero % 2 == 0) or (tipo_de_numero == "ímpares" and numero % 2 != 0):
        print(numero)
        contador += 1
    numero += 1


# Pseudocódigo (Visualg)
#
# algoritmo "impressão de números"
# var
#   tipo_de_numero: caractere
#   qtd_de_vezes, numero, contador: inteiro
#
# inicio
#   escreva("Digite que tipo de número você gostaria (Pares ou Ímpares): ")
#   leia(tipo_de_numero)
#   escreva("Digite a quantidade de vezes que esse número deverá ser impresso: ")
#   leia(qtd_de_vezes)
#
#   numero <- 1
#   contador <- 0
#
#   enquanto (contador <= qtd_de_vezes) faca
#      se ((tipo_de_numero = "pares") e (numero % 2 = 0)) ou ((tipo_de_numero = "ímpares") e (numero % 2 <> 0)) entao
#         escreval(numero)
#         contador <- contador + 1
#      fimse
#      numero <- numero + 1
#   fimenquanto
# fimalgoritmo
