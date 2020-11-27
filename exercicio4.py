# Faça um programa que gera uma lista dos números primos existentes
# entre 1 e um número inteiro informado pelo usuário.

def mostraNumerosPrimos(numero):
    for x in range(1, numero + 1):
        cont = 0
        for i in range(1, numero + 1):
            if (x % i == 0):
                cont = cont + 1

        if x == 1 or cont > 2:
            numerosNaoPrimos.append(x)
        else:
            numerosPrimos.append(x)
    return numerosPrimos


numero = int(input("Informe o limite para que possamos gerar as informações sobre numeros primos: "))
numerosPrimos = []
numerosNaoPrimos = []
print(f'Os numeros primos entre 1 e {numero} são:\n{mostraNumerosPrimos(numero)}')

#Muito bom, não mudaria nada. Ainda salvou os não primos que podem ser retornados com uma pequena alteração, maneiro.