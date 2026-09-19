# Escreva um programa em Python que simule uma tabuada.


numero = int(input("Digite um número para ser multiplicado: "))

qtd_de_vezes = int(input("Digite a quantidade de vezes que esse número deverá ser multiplicado: "))


contador = 1 


while (contador <= qtd_de_vezes):
    resultado = numero * contador
    print(f"{numero} × {contador} = {resultado}")
    contador += 1


# algoritmo "Tabuada"
# var
#   numero, qtd_de_vezes, contador, resultado: inteiro
# inicio
#   escreva("Digite um número para ser multiplicado: ")
#   leia(numero)
#   escreva("Digite a quantidade de vezes que esse número deverá ser multiplicado: ")
#   leia(qtd_de_vezes)
#
#   contador <- 1
#
#   enquanto (contador <= qtd_de_vezes) faca
#     resultado <- numero * contador
#     escreval(numero, " × ", contador, " = ", resultado)
#     contador <- contador + 1
#   fimenquanto
# fimalgoritmo