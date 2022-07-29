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

#QUESTÃO 11
"""
Nessa questão, você terá 5 pares de números e para cada um deles deverá ser impresso o maior número do par. A função responsável por realizar a essa operação deverá chamar maiorAB e receber dois valores numéricos.

Entrada
A entrada consiste de 5 linhas, com cada uma contendo 2 inteiros a,b separados por espaços.

Saída
Para cada par, imprima o maior dos dois números.


Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos, por esse critério, caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
"""

def maiorAB (x,y):
    z = max(x,y)
    print(z)
        
for i in range (1,6):
    x,y = input().split()
    x,y = int(x),int(y)
    
    maiorAB(x,y)

#QUESTÃO 12 
"""
Nessa questão, você terá de ler 5 pares de valores inteiros e imprimí-los com a ordem entre eles trocada. A função responsável por realizar a troca deverá chamar trocarAB e receber os dois valores a serem trocados.

Entrada
A entrada consiste de 5 linhas, com cada uma contendo 2 números a,b.

Saída
Para cada par, imprima o par inserido com a ordem trocada.

Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos, por esse critério, caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).


"""
def trocarAB(x,y):
    print(y,x)
    
for i in range (1,6):
    x,y = input().split()
    x,y = int(x),int(y)
    
    trocarAB(x,y)

#QUESTÃO 13
"""
Mellin é um lendário feiticeiro conhecido por toda a terra tupiniquim. Cercado por mistérios, ninguém conhece ao certo o que ele faz ou de onde veio, são apenas lendas. Recentemente, em uma de suas escavações, o Instituto Brilhante de Grandes Escavações (IBGE) encontrou três números misteriosos em ruínas de um lugar que Mellin supostamente viveu.  A principal teoria é que um destes números representa a idade de Mellin em dias, no momento em que foram escritos. O problema é que eles não conseguem saber qual desses números seria a idade e precisam compará-los, porém meros mortais têm dificuldade em entender idades em dias.

Dessa forma, o IBGE lançou um Programa Internacional Brilhante de Iniciação Científica (PIBIC) de modo que estudantes universitários ao redor do mundo iriam ajudar a entender estas datas. O seu papel é dizer quantos anos, meses e dias representam cada um dos três números misteriosos. Para facilitar o entendimento, o IBGE pediu que uma função chamada age que recebe a quantidade dias a serem calculadas fosse implementada. Essa função deve transformar e imprimir essa informação em anos, meses e dias.

IMPORTANTE: No mundo de Mellin, todos os anos têm 360 dias e todos os meses têm 30 dias.

Entrada
A entrada consiste de 3 números diferentes guardados pelas variáveis a,b,c≥3, separadas por espaço.


Saída
Para cada um dos três números, imprima quantos anos, meses e dias seriam no seguinte formato:



{A} ano(s), {M} mes(es) e {D} dia(s)
Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos, por esse critério, caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
"""


def age(num):
    anos = num//360
    meses = (num % 360)//30
    dias = (num % 360) % 30
    print(f'{anos} ano(s), {meses} mes(es) e {dias} dia(s)')


code = input('')
codes = code.split()
for item in codes:
    age(int(item))


#QUESTÃO 14
"""
Faça um programa que leia idades de três pessoas em dias e mostre suas idades em anos, meses e dias. Considere que todo ano contém 360 dias e todo mês tem 30 dias. A função deve chamar age e receber como parâmetro SOMENTE a quantidade de dias em uma única variável.

Entrada
A entrada contém três números inteiros 1≤d1,d2,d3≤106, a idade de cada uma das 3 pessoas, em dias.

Saída
Para cada uma das três idades, você deve imprimir: Três inteiros separados por espaço A, M e D , representando a idade da pessoa em anos, meses e dias, respectivamente.


Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos, por esse critério, caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
"""


def age(num):
    anos = num//360
    meses = (num % 360)//30
    dias = (num % 360) % 30
    print(f'{anos} {meses} {dias}')


code = input('')
codes = code.split()
for item in codes:
    age(int(item))


#QUESTÃO 15
"""
Escreva um programa que leia, para uma determina pessoa, a altura da mesma. Este programa deve utilizar uma função chamada peso_ideal que recebe como parâmetro a altura em ponto flutuante e  imprime o peso ideal para homem e mulher.

Para homens, deve-se calcular o peso ideal usando a fórmula de peso ideal = 72.7 x alt - 58 e, para mulheres, peso ideal = 62.1 x alt - 44.7.

Entrada
A entrada consiste de um de valor em ponto flutuante indicando a altura em metros (1.0≤alt≤2.2) 

Saída 
O peso ideal da pessoa, com duas casas decimais considerando o cálculo para homem e mulher.

Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos, por esse critério, caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
"""

z = input('')
z = float(z)


def peso_ideal(x):
    peso_mulher = 62.1 * x - 44.7
    peso_homem = 72.7 * x - 58
    print(f'%.2f' % (peso_homem,), f'%.2f' % (peso_mulher))


peso_ideal(z)

#QUESTÃO 16
"""
Dada a descrição de um horário, diga quantos segundos já se passaram no dia conforme o formato definido abaixo.

Entrada
A entrada consiste de uma linha, composta por três números inteiros representando um horário no dia, apresentados no formato "hh:mm:ss" (hora:minutos:segundo). 

Saída
A saída deve ser composta de uma linha apresentando a mensagem: "La se foram X segundos que nao voltam mais...", onde X é a quantidade total de segundos decorridos desde o início do horário.
"""

hora, minutos, segundos = [int(n) for n in input().split(':')]
total = hora*3600 + minutos*60 + segundos
print(f'La se foram {total} segundos que nao voltam mais...')

#QUESTÃO 17
"""
Escreva um programa que transforme números decimais em binário. Seu programa deve ler 5 números inteiros e para cada um deles deve imprimir sua representação em código binário. A função responsável pela transformação deve se chamar binario e receber como parâmetro um número inteiro. 

Entrada
A entrada consiste de 5 linhas, com cada uma contendo 1 número a≥0 inteiro.

Saída
Para cada número, imprima sua representação em binário no formato 0b[numero em binário]

Particularidade do Tópico

Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos, por esse critério, caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
"""


for i in range(5):
    x = int(input())

    def binario(x):
        bina = format(x, "b")
        print(f"0b{bina}")
    binario(x)

#QUESTÃO 18
"""
Escreva um programa que transforme números decimais em hexadecimal. Seu programa deve ler 5 números inteiros e para cada um deles deve imprimir sua representação em código hexadecimal. A função responsável pela transformação deve chamar hexadecimal e receber como parâmetro um número inteiro. 

Entrada
A entrada consiste de 5 linhas, com cada uma contendo 1 número a≥0 inteiro.

Saída
Para cada número, imprima sua representação em hexadecimal no formato 0x[numero em hexadecimal]

Particularidade do Tópico

Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos, por esse critério, caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
"""

for i in range (5):
    x = int(input())
    
    def hexadecimal (x):
        hexa = hex(x)
        print(hexa)
    hexadecimal(x)
    
#QUESTÃO 19 
"""
O Decanato de Graduação (DEG) está testando uma nova funcionalidade no SIGAA que permite apresentar a quantidade de períodos que um determinado estudante já concluiu na Universidade de Brasília. Para isso, o DEG aproveita as informações de ingresso na UnB existentes no próprio número de matrícula dos alunos e compara com o ano e o semestre atual. Como se sabe, os quatro dígitos mais significativos d1,d2,d3 e d4 do número de matrícula indicam o ano e o semestre de ingressos do aluno na UnB.

Por exemplo, se o número de matrícula de um estudante é 190199999, os quatro dígitos mais significativos formam o número 1901, em que adota-se a convenção (d1=1,d2=9,d3=0,d4=1). O número formado da combinação de d1 e d2, 19, indicam que o aluno ingressou na UnB em 2019 e o d4=1 mostra que o aluno ingressou no segundo semestre desse ano. Outro exemplo se trata do número de matrícula 180099899, que indica que estudante ingressou na UnB no primeiro semestre de 2018.

Elabore uma função chamada  quantosSemestres que receba como parâmetros três números inteiros m, a e s associados ao número de matrícula do aluno, o ano atual e o semestre atual, respectivamente. Essa função deve calcular a quantidade mínima de semestres (concluídos) em que o referido aluno está na UnB.

Entrada

A entrada compreende os parâmetros da função quantosSemestres, que são três números inteiros m, a e s  (100000000≤m≤500000000,2010≤a≤2050,s∈{0,1} ) associados ao número de matrícula do aluno, o ano atual e o semestre atual, respectivamente. É garantido que o ano e o semestre atual do aluno são maiores ou iguais ao ano e semestre de ingresso na UnB. 

Saída

A função quantosSemestres deve imprimir a quantidade mínima de semestres em que o aluno associado ao número de matrícula está na UnB.

Notas

i) No primeiro caso de teste, de acordo com o número de matrícula, o aluno ingressou na UnB no primeiro semestre de 2020 e o semestre atual também é o primeiro semestre de 2020. Portanto, o aluno ainda não concluiu nenhum semestre. 

ii) No segundo caso de teste, de acordo com o número de matrícula, o aluno ingressou na UnB no primeiro semestre de 2020 e o semestre atua é o segundo semestre de 2020. Portanto, o aluno concluiu um período na UnB.
"""

def quantosSemestres(registro, ano_corrente, semestre_corrente):
    ano = int(str(registro)[0:2]) + 2000
    semestre = int(str(registro)[3])
    print(((ano_corrente - ano)*2) - semestre + semestre_corrente)

#QUESTÃO 20

"""
O Decanato de Graduação (DEG) está testando uma nova funcionalidade no SIGAA que permite apresentar em qual semestre um aluno da Universidade de Brasília se encontra. Para isso, o DEG aproveita as informações de ingresso na UnB existentes no próprio número de matrícula dos alunos e compara com o ano e o semestre atual. Como se sabe, os quatro dígitos mais significativos d1,d2,d3 e d4 do número de matrícula indicam o ano e o semestre de ingressos do aluno na UnB.

Por exemplo, se o número de matrícula de um estudante é 190199999, os quatro dígitos mais significativos formam o número 1901, em que adota-se a convenção (d1=1,d2=9,d3=0,d4=1). O número formado da combinação de d1 e d2, 19, indicam que o aluno ingressou na UnB em 2019 e o d4=1 mostra que o aluno ingressou no segundo semestre desse ano. Outro exemplo se trata do número de matrícula 180099899, que indica que estudante ingressou na UnB no primeiro semestre de 2018.

Elabore uma função chamada  qualPeriodo que receba como parâmetros três números inteiros m, a e s associados ao número de matrícula do aluno, o ano atual e o semestre atual, respectivamente. Essa função deve calcular o semestre atual em que o aluno se encontra na UnB.

Entrada

A entrada compreende os parâmetros da função qualPeriodo, que são três números inteiros m, a e s  (100000000≤m≤500000000,≤a≤2050,s∈{0,1} ) associados ao número de matrícula do aluno, o ano atual e o semestre atual, respectivamente.  É garantido que o ano e o semestre atual do aluno são maiores ou iguais ao ano e semestre de ingresso na UnB. 

Saída

A função qualPeriodo deve retornar em qual semestre o aluno se encontra desde que ingressou na UnB.
"""


def qualPeriodo(registro, ano, semestre):
    registro = str(registro)
    ano = int(ano)
    semestre = int(semestre)

    ano_entrada = int(registro[0] + registro[1])
    ano_entrada += 2000
    semestre_entrada = int(registro[3])

    anos_dentro = ano - ano_entrada
    semestre_dentro = (semestre - semestre_entrada) + (anos_dentro*2)
    print(semestre_dentro + 1)
