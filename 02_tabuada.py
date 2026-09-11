numero = int(input("Digite um número para ser multiplicado: "))
qtd_de_vezes = int(input("Digite a quantidade de vezes que esse número deverá ser multiplicado: "))

contador = 1

while (contador <= qtd_de_vezes):
    resultado = (numero * contador)
    print (f"{numero} X {qtd_de_vezes} = {resultado}")
    contador += 1