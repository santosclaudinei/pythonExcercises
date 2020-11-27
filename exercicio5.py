# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor.
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar
# numeros aleatórios, simulando os lançamentos dos dados.

from random import randint
from collections import Counter

lancamentos = []

for i in range(1, 100):
    dado = randint(1, 6)
    lancamentos.append(dado)

resultado = Counter(lancamentos)

for jogada, ocorrencia in resultado.items():
    print(f'o lado do dado {jogada} ocorreu {ocorrencia} vezes')