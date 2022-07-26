#QUESTÃO 1 
"""
Escreva um programa que leia um caratere do teclado e apresente-o de diversas formas diferentes, de acordo com o solicitado.

Entrada 
A entrada consiste de um único caractere c que é garantidamente alfanumérico (uma letra alfabeto latino, maiúscula ou minúscula, ou um dígito).

Saída
A saída deve ser composta de 5 linhas, cada uma como apresentada a seguir.
Somente o caractere lido;
Duas vezes o caractere lido;
Duas vezes o caractere lido, separados por um espaço;
A mensagem '2X' (onde X deve ser substituído pelo caractere lido);
O caractere lido, envolto em colchetes.
"""
x = input('')
print(x)
print(x*2)
print(f'{x} {x}')
print(f'2{x}')
print(f'[{x}]')

#QUESTÃO 2
"""
Escreva um programa que leia três carateres do teclado e apresente ele de diversas formas diferentes.

Entrada
A entrada consiste de três caracteres alfanuméricos x,y e z, um por linha, sendo esses letra do alfabeto latino, maiúscula, minúscula ou dígito. 

Saída
A saída deve ser composta de 6 linhas (conforme os exemplos), cada uma como apresentada a seguir:
Os caracteres lidos, juntos;
Somente o primeiro caractere lido;
Duas vezes o segundo caractere lido;
Três vezes o terceiro caractere, separados por um espaço;
A mensagem "X == x, Y == y, Z == z" (onde x, y e z devem ser substituídos pelos caracteres lidos);
A mensagem "X != y, Y != x, Z == z" (onde y, x e z devem ser substituídos pelos caracteres lidos).
"""
x = input()
y = input()
z = input()
print(f'{x}{y}{z}')
print(x)
print(y*2)
print(f'{z} {z} {z}')
print(f'X == {x}, Y == {y}, Z == {z}')
print(f'X != {y}, Y != {x}, Z == {z}')

#QUESTÃO 3
"""
Escreva uma função chamada imprimeAPC que deverá imprimir uma palavra usando caracteres ASCII. 

Entrada
Não há.

Saída
A impressão da palavra APC, utilizando ASCII Art, de acordo com o exemplo
"""


def imprimeAPC():
    print('    _    ____   ____ ')
    print('   / \  |  _ \ / ___|')
    print('  / _ \ | |_) | |    ')
    print(' / ___ \|  __/| |___  ')
    print('/_/   \_\_|    \____|')

#QUESTÃO 4
"""
Implemente um programa que calcule XY. Seu programa deve ler os valores de X e Y, ambos inteiros, e imprimir o valor resultante de Xy  em ponto flutuante.

Entrada 
Dois valores inteiros X e Y.

Saída
O resultado da potenciação Xy  em ponto flutuante.

Observação
Utilize a função pow da biblioteca math 
"""
import math 
x,y = [int(i) for i in input().split(' ')]
print(math.pow(x,y))

#QUESTÃO 5
"""
Implemente uma função chamada powAPC que calcule XY. Sua função deve receber os valores de X e Y, ambos inteiros, e imprimir o valor de Xy em ponto flutuante.

Entrada 
Dois valores inteiros X e Y.

Saída
O resultado da potenciação Xy  em ponto flutuante.

Observação
Utilize a função pow da biblioteca math 
"""
import math
def powAPC (x,y):
    print(math.pow(x,y))

#QUESTÃO 6
"""
Quando Sam e Jean estão viajando, eles sempre veem esses terminais que mostram a temperatura do local onde eles se encontram. Um problema muito comum que causa diversas confusões é que dependendo do lugar, a temperatura é exibida em graus Celsius e em outros lugares a temperatura é exibida em Fahrenheit. Atualmente eles estão viajando pela América do Norte onde é comum medir a temperatura em Fahrenheit. Escreva uma função chamda converte que receba uma temperatura em ponto flutuante e imprima o resultado após a conversão para graus Celsius.

Entrada
Essa função recebe como entrada o valor da temperatura em ponto flutuante.

Saída
Imprimir o valor convertido de Fahrenheit para Celsius. O valor convertido deve ser apresentando com somente uma casa decimal.
"""


def converte(x):
    z = (x - 32) * (5/9)
    print(round(z, 1))

#QUESTÃO 7 
"""
Quando Sam e Jean estão viajando, eles sempre veem esse terminais que mostram a temperatura do local onde eles se encontram. Um problema muito comum que causa diversas confusões é que dependendo do lugar, a temperatura é exibida em graus Celsius e em outros lugares a temperatura é exibida em Fahrenheit. Atualmente eles estão viajando pela América do Sul onde é comum medir a temperatura em Celsius. Escreva uma função chamda converte que recebe uma temperatura em ponto flutuante e imprima o resultado após a conversão para Fahrenheit.

Entrada
Essa função recebe como entrada o valor da temperatura em ponto flutuante.

Saída
Imprimir o valor convertido de Celsius para Fahrenheit. O valor convertido deve ser apresentando com somente uma casa decimal.
"""


def converte(x):
    z = (x * 9/5) + 32
    print(round(z, 1))

#QUESTÃO 8
"""
Du, Dudu e Edu aproveitaram que não tinham aula na sexta-feira e resolveram ir para o Barbosinha conversar e comer uns petiscos (situação hipotética, devido a pandemia). Após um tempo de conversa, bebidas e comidas, eles resolveram pedir a conta e o garçom entregou uma conta indivual para cada um e avisou que os 10% ainda não estavam inclusos. Com isso, eles viram você passando e, sabendo que você é um exímio programador, pediram para ajudar a calcular quanto cada um iria pagar e qual o valor total da conta com os 10% inclusos.



Entrada
Três valores reais a, b e c, separados por espaço, indicando os valores das contas de Du, Dudu e Edu.

Saída
Imprima duas linhas da seguinte forma:

- A primeira linha deve conter três floats com precisão de duas casas decimais, representando o valor a ser pago por Du, Dudu e Edu.

- A segunda linha deve conter o valor total, incluindo os 10%, com precisão também de duas casas decimais.
"""

x, y, z = [float(n) for n in input().split()]
x = x*1.1
y = y*1.1
z = z*1.1
total = x + y + z
print(f'%.2f' % x, f'%.2f' % y, f'%.2f' % z)
print(f'%.2f' % total)




#QUESTÃO 9 
"""
Escreva um programa para receber o valor do raio de uma circunferência e calcular três informações: diâmetro, área e perímetro.

Entrada
A única linha da entrada é composta por um float r, que representa o raio da circunferência.

Saída
Imprima três linhas, cada uma contendo o diâmetro, a área e o perímetro (nessa ordem), apresentando duas casas decimais de precisão.

Observação

Utilize π=3.14159
"""
raio = float(input())
diametro = raio * 2
area = 3.14159*raio**2
perimetro = 2*3.141559*raio
print('%.2f' % diametro)
print(f'%.2f' % area)
print(f'%.2f' % perimetro)

#QUESTÃO 10 
"""
Dada a descrição de uma data, apresente-a conforme os formatos definidos abaixo.

Entrada
A entrada consiste de uma linha, composta por três números inteiros positivos representando uma data no formato DD/MM/AA (dia/mês/ano). É garantido que as datas serão sempre válidas.

Saída
A saída deve ser composta de 3 linhas (conforme os exemplos), cada uma como apresentada no formato a seguir: 
a data no formato "DD-MM-AA"; 
a data no formato "MM-DD-AA"; 
a data no formato "AA/MM/DD".
Atenção à quantidade de dígitos!
"""
dd, mm, aa = input().split('/')
print(f'{dd}-{mm}-{aa}')
print(f'{mm}-{dd}-{aa}')
print(f'{aa}/{mm}/{dd}')
