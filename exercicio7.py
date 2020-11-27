# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u.

from collections import Counter
ocorrencias = []

textoLivro = """Essa é uma ideia nova? Há muitos ditados que mostram a importância do risco e o poder da persistência,
como “Quem não arrisca não petisca”, “Se não der certo da primeira vez, tente uma segunda e uma
terceira” ou “Roma não foi feita em um só dia”. (Aliás, fiquei encantada ao saber que os italianos usam a
mesma expressão.) O que verdadeiramente surpreende é que as pessoas de mindset fixo não
concordariam com isso. Para elas, os ditados seriam: “Se eu não arriscar, nada perderei”, “Se não der
certo da primeira vez, é porque provavelmente não tenho competência”, “Se Roma não foi feita em um só
dia, provavelmente foi porque não poderia ser feita em menos tempo”. Em outras palavras, risco e
esforço são duas coisas capazes de revelar suas deficiências e mostrar que você não está à altura da
tarefa. Com efeito, é espantoso verificar até que ponto as pessoas de mindset fixo não acreditam no
esforço.
O que também constitui novidade é que as ideias das pessoas a respeito de risco e esforço derivam de
seus mindsets mais básicos. Não se trata somente do fato de que algumas pessoas são capazes de
reconhecer o valor de desafiar a si mesmas e a importância do esforço. Nossa pesquisa demonstrou que
isso deriva diretamente do mindset de crescimento. Quando ensinamos a alguém esse mindset, cujo ponto
focal é o desenvolvimento, as ideias sobre desafio e esforço vêm em seguida. Da mesma forma, não se
trata somente de que para algumas pessoas o desafio e o esforço podem não ser agradáveis. Quando
(temporariamente) colocamos alguém num mindset fixo, que se concentra nas características permanentes,
essa pessoa rapidamente passa a temer o desafio e a desvalorizar o esforço."""

for letra in textoLivro:
    # if 'a' in letra or 'b' in letra or 'c' in letra or 'd' in letra or 'e' in letra or ' ' in letra:
    lista_vogais_space = ["a", "e", "i", "o", "u", " "]
    if letra in lista_vogais_space:
        ocorrencias.append(letra)

resultado = Counter(ocorrencias)
for variavel, numero in resultado.items():
    print(f'O elemento "{variavel.upper()}" aparece no texto {numero} vezes')