# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.


def forma_triangulo(a, b, c):
    if (a - b) < c and (a + b) > c:
        if (a - c) < b and (a + c) > b:
            if (b - c) < a and (b + c) > a:
                print(f'Os lados {a}, {b} e {c} podem formar um triangulo!')
        tipo_triangulo(a, b, c)
    else:
        print(f'Os lados {a}, {b} e {c} não formam um triangulo!')


def tipo_triangulo(a, b, c):
    if (a == b) and (a == c) and (b == c):
        print(f'Os valores digitados foram {a}, {b} e {c}.', end=' ')
        print(f'Formam um TRIÂNGULO EQUILATÉRO.')
    elif (a != b) and (a != c) and (b != c):
        print(f'Os valores digitados foram {a}, {b} e {c}.', end=' ')
        print(f'Formam um TRIÂNGULO ESCALENO.')
    else:
        print(f'Os valores digitados foram {a}, {b} e {c}.', end=' ')
        print(f'Formam um TRIÂNGULO ISÓCELES.')


ladoA = int(input("Informe o lado A do triangulo: "))
ladoB = int(input("Informe o lado B do triangulo: "))
ladoC = int(input("Informe o lado C do triangulo: "))

forma_triangulo(ladoA, ladoB, ladoB)


#Mesma mudança do exercício 1, eu tiraria os prints de dentro da função. Lembrando também que o "end=' '"
#não é necessário nessa ocasião, dava pra fazer: 
# print(f'Os valores digitados foram {a}, {b} e {c}. Formam um TRIÂNGULO tal')
