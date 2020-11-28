# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
# e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga
#     e sempre arredonde os valores para cima, isto é, considere latas cheias.

#######################################################################################################

from math import ceil


def calculaRendimento(qtd_lata, qtd_galao):
    rend_lata = 6 * qtd_lata
    rend_galao = 6 * qtd_galao
    return rend_lata, rend_galao


def calculaMelhor(area_a_pintar, rendimento_A, rendimento_B): #rendimento_lata, rendimento_galao
    melhor_A = area_a_pintar // rendimento_A
    melhor_B = round(area_a_pintar - (melhor_A * rendimento_A))
    sobra = ceil(melhor_B / rendimento_B) * 1.1
    return melhor_A, melhor_B, sobra


def calculaQuantidade(area, qtd_lata, qtd_galao):
    qtd_lata = ceil(area / rend_lata)
    qtd_galao = ceil(area / rend_galao)
    return qtd_lata, qtd_galao


area_a_pintar = float(input("Informe o tamanho da area que deseja pintar [EM METROS QUADRADOS (M²)]: "))
lata = 18
galao = 3.6
preco_lata = 80.0
preco_galao = 25.0

rend_lata, rend_galao = calculaRendimento(lata, galao)
melhor_A, melhor_B, sobra = calculaMelhor(area_a_pintar, rend_lata, rend_galao)
qtd_lata, qtd_galao = calculaQuantidade(area_a_pintar, rend_lata, rend_galao)

input("""
Abaixo estão as opções para melhor atende-lo:
[1] -       LATAS           (18   LITROS)           R$ 80,00
[2] -       GALÃO           (3.6  LITROS)           R$ 25,00

Para visualizar as opções de orçamento pressione ENTER para continuar ... 
""")

print(f"""
Abaixo você pode optar por comprar latas ou galões:
[1] -       LATAS           {qtd_lata} Und.           R$ {(qtd_lata) * preco_lata}
[2] -       GALÃO           {(qtd_galao)} Und.          R$ {(qtd_galao) * preco_galao} 
""")

print(f"""
Abaixo estão os orcamentos com os produtos, quantidades e seus respectivos preços:
[1] -       LATAS           {ceil(melhor_A)} Und.           R$ {(melhor_A * preco_lata) :.2f}
[2] -       GALÃO           {ceil(sobra)} Und.            R$ {(sobra * preco_galao):.2f} 
[3] -       TOTAL           {ceil(melhor_A + sobra)} Und.           R$ {melhor_A * preco_lata + (sobra
    * preco_galao):.2f}
""")

#Eu só trocaria o nome das variáveis 'melhor_A' e 'melhor_B' para melhor leitura.
