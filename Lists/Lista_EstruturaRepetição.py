#Questão 1
"""
Entrada
Os parâmetros da função são dois inteiros arg1,arg2≥1 e uma string forma. Em caso de retângulo, os argumentos representam a base e a altura da forma e caso a figura seja um losango, os argumentos representam o valor das duas diagonais.

Saída
A função deve imprimir a frase "O forma tem area de area", conforme os exemplos.

forma é a string que pode ter as formas geométricas retangulo ou losango e area é o valor inteiro do cálculo da área da forma geométrica dada na string forma, com arg1,arg2 assumindo as incógnitas de cada cálculo de área.
"""


def area(x, y, forma):
    if forma == 'losango':
        print(f'O losango tem {x*y//2} de area')
    else:
        print(f'O retangulo tem {x*y} de area')


#Questão 2
"""
Entrada
Os parâmetros da função são dois inteiros arg1,arg2≥1 e uma string forma. Em caso de retângulo ou triângulo, os argumentos representam a base e a altura da forma e caso a figura seja um losango, os argumentos representam o valor das duas diagonais.

Saída
A função deve imprimir a frase "O forma tem area de area".

forma é a string inserida, que pode tomar o nome de quatro formas geométricas: retangulo, losango e triangulo e area é somente o valor inteiro do cálculo da área da forma geométrica dada na string forma, com arg1,arg2 assumindo as incógnitas de cada cálculo de área.
"""


def area(x, y, forma):
    if forma == 'losango':
        print(f'O losango tem {x*y//2} de area')
    elif forma == 'retangulo':
        print(f'O retangulo tem {x*y} de area')
    else:
        print(f'O triangulo tem {x*y//2} de area')

#Questão 3
"""
Entrada
Os parâmetros da função são dois inteiros arg1,arg2≥1 e uma string forma. Em caso de retângulo ou triângulo, os argumentos representam a base e a altura da forma, caso a figura seja um losango, os argumentos representam o valor das duas diagonais, e caso a figura geométrica seja círculo, a variável arg1 será sempre o raio, e a variável arg2 sempre será igual a 3.

Saída
A função deve imprimir a frase O forma tem area de area

Onde forma é a string inserida, que pode tomar o nome de quatro formas geométricas: retangulo, losango, triangulo, circulo e area é somente o valor inteiro do cálculo da área da forma geométrica dada na string forma, com arg1,arg2 assumindo as incógnitas de cada cálculo de área.
"""


def area(x, y, forma):
    if forma == 'losango':
        print(f'O losango tem {x*y//2} de area')
    elif forma == 'retangulo':
        print(f'O retangulo tem {x*y} de area')
    elif forma == 'triangulo':
        print(f'O triangulo tem {x*y//2} de area')
    else:
        print(f'O circulo tem {int(3 *x*x)} de area')

#Questão 4
"""
Entrada
A função banner recebe como parâmetro um único inteiro n (−1000≤n≤1000), para utilizar em cada um dos quatro tipos de padrões.

Saída
Na saída deverá ser impresso o padrão, utilizando a seguinte lógica:

Se o número n for par e positivo, o padrão deve ser (sem as aspas): "| | | | | | | | | |"
Se o número n for ímpar e positivo, o padrão deve ser (sem as aspas): "- - - - - - - - - -"
Se o número n for par e negativo, o padrão deve ser (sem aspas): ". . . . . . . . . ."
Se o número n for ímpar e negativo, o padrão deve ser (sem aspas): "= = = = = = = = = ="
"""


def banner(n):
    if n > 0 and n % 2 == 0:
        print('| | | | | | | | | |')
    elif n > 0 and n % 2 != 0:
        print('- - - - - - - - - -')
    elif n < 0 and n % 2 == 0:
        print('. . . . . . . . . .')
    else:
        print('= = = = = = = = = =')

#Questão 5
"""
Em Campinas, cidade do interior de São Paulo, existem infintos galões de água de 1 litro, que custam a dinheiros, e infinitos galões de 2 litros, que custam b dinheiros, disponíveis para venda. Qual o menor número de dinheiros necessário para Fagundes comprar exatamente n litros de água?

Escreva uma função chamada dinheiros que recebe três parâmentros referentes ao número n de Litros desejado por Fagundes, o valor a de galões de 1L e o valor b de galões de 2L. A função deve imprime o pedido com menor valor.

Entrada
Os parâmetros da função são três inteiros n,a,b≥1.

Saída 
Imprima um único inteiro com a menor quantidade de dinheiro que Fagundes precisa gastar.

"""


def dinheiros(n, a, b):
    preco_litro = b/2
    valor_pago = 0
    litros_restantes = n
    litros_comprados = 0

    if a <= preco_litro:
        valor_pago = n * a
        litros_comprados = n*a
        litros_restantes = n - litros_comprados

    else:
        litros_comprados = int(n/2)*2
        valor_pago = litros_comprados * preco_litro
        litros_restantes = n - litros_comprados

    if litros_restantes == 1:
        valor_pago += a

    print(int(valor_pago))

#Questão 6
"""
Imagine que você tenha um tabuleiro com N×M quadrados, similar a um tabuleiro de xadrez que tem 8×8 quadrados. Também imagine que  você ganhou um suprimento infinito de peças de dominó, cada peça tem dimensão 2×1 e, por isso, ocupam dois quadrados do seu tabuleiro. Escreva uma função dominos(N, M) que imprima a quantidade máxima de dominós que podem ser colocados no tabuleiro.

Seu papel é colocar o máximo de dominós que puder no tabuleiro de modo que no fim as seguintes condições sejam satisfeitas:

Cada dominó colocado cobre completamente dois quadrados do tabuleiro. Não pode colocar uma peça de dominó com metade dentro do tabuleiro e metade fora por exemplo.
Nenhuma peça de dominó fica em cima de outra peça de dominó. Cada quadrado do tabuleiro só é coberta por até 1 dominó.
Cada dominó pode ser colocado tanto na orientação vertical como na horizontal.
Entrada
Os parâmetros da função são dois inteiros 1≤N≤M≤16.

Saída 
Um número inteiro representando a quantidade máxima de dominós que podem ser colocados no tabuleiro.
"""


def dominos(n, m):
    tamanho_tabuleiro = n*m
    tamanho_domino = 2
    print(tamanho_tabuleiro//2)

#Questão 7 
"""
Implemente a função chamada realidade que imprime se uma equação de segundo grau  a∗x2+b∗x+c=0 tem raízes reais ou complexas. A função deve receber os parâmetros a, b, e c que são números inteiros. 

Entrada
Os parâmetros da função são três inteiros a,b,c.

Saída
Imprima uma única linha com a mensagem "reais", se as raízes da equação são reais; ou a mensagem "complexas", se as raízes possuem parte imaginária não nula.
"""

def realidade(a,b,c):
    delta = b**2 -4*a*c
    if delta >= 0:
        print('reais')
    else:
        print('complexas')

#Questão 8 
"""
Entrada

Os parâmetros da função são três inteiros a,b,c onde a,b,c≥0.

Saída

Imprima uma linha para cada forma geométrica que a combinação desses números pode formar:

Utilizando os dois primeiros argumentos, imprima "pode ser quadrado" ou "pode ser retangulo", de acordo com a propriedade de formação da figura identificada. 

Utilizando os três argumentos, imprima baseado na propriedade de triângulos e suas classificações, na mesma linha:

pode ser triangulo – A soma de qualquer par é maior que o número restante da tripla.
escaleno – Satisfaz a propriedade triangulo e os três lados são distintos entre si.
isosceles – Satisfaz a propriedade triangulo e pelo menos dois lados são iguais.
equilatero – Satisfaz a propriedade triangulo e os três lados são iguais.
"""


def formamisteriosa(a, b, c):
    if a == b:
        print("pode ser quadrado")
    else:
        print("pode ser retangulo")
    if a + b > c and a + c > b and b + c > a:
        triangulo = 'pode ser triangulo'
        if a == b and b == c:
            tipo = 'equilatero'
        elif a == b or b == c or c == a:
            tipo = "isosceles"
        else:
            tipo = "escaleno"
        print(triangulo + ' ' + tipo)

#Questão 9 
"""
Entrada
Os parâmetros da função são três inteiros a,b,c.

Saída
Imprima uma linha para cada propriedade que a tripla de números satisfaz, na ordem indicada abaixo.

triangulo – A soma de qualquer par é maior que o número restante da tripla.
gondim sendo gondim – Não satisfaz a propriedade triangulo.
escaleno – Satisfaz a propriedade triangulo e os três lados são distintos entre si.
isosceles – Satisfaz a propriedade triangulo e pelo menos dois lados são iguais.
equilatero – Satisfaz a propriedade triangulo e os três lados são iguais.
retangulo – Satisfaz a propriedade triangulo e o quadrado do maior lado é a soma dos quadrados dos outros lados.
Caso o triângulo possua mais de uma das propriedades estas devem ser listadas na ordem apresentada acima, caso o triângulo seja um triangulo isosceles e retangulo a seguinte saída é considerada errada:

triangulo
retangulo
isosceles

Enquanto a seguinte saída está correta:

triangulo
isosceles
retangulo

"""


def classificador(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("triangulo")

        if a != b and b != c and c != a:
            print("escaleno")
        elif a == b or b == c or c == a:
            print("isosceles")

        if a == b and b == c:
            print("equilatero")

        if a*a == b*b+c*c or b*b == a*a+c*c or c*c == a*a+b*b:
            print("retangulo")
    else:
        print("gondim sendo gondim")

#Questão 10
"""
A família Cacãope está em crise. Eles não sabem qual dos dois filhos é o mais velho! Por sorte, encontraram você, um primo distante para ajudá-los.

Escreva uma função chamada older(ageA, ageB) que receberá a idade em anos completos dos filhos A e B e deverá imprimir A se o filho A for com certeza mais velho, B se o filho B for com certeza mais velho e Maybe twins se não for possível saber com certeza é o mais velho.
Entrada
A entrada consiste de dois inteiros ageA,ageB que indicam a idade em anos completos dos filhos A e B, respectivamente.

Saída
A saída deve conter A se o filho A for com certeza mais velho, B se o filho B for com certeza mais velho e Maybe twins se não for possível saber com certeza é o mais velho.
"""


def older(a: int, b: int):
    if a > b:
        print('A')
    elif a < b:
        print('B')
    else:
        print('Maybe twins')

#Questão 11
"""
O MMORPG mais famoso do momento, Instant Soul Crushing (ISC), permite que seus jogadores realizem duelos entre si sob o sistema RISCU. Este sistema recebe o nível de poder dos dois jogadores e diz qual jogador é o ganhador e qual jogador é o perdedor.

Você, como um membro de ISC,  deve implementar o sistema RISCU: escreva uma função chamada riscu(powerA, ṕowerB) que receberá o poder dos jogadores A e B e deverá imprimir: 

Se o jogador A for mais forte: Jogador A vence   
Se o jogador B for mais forte: Jogador B vence 
Se ambos jogadores têm a mesma força: Dois jogadores igualmente fracos
Entrada
A entrada consiste de dois inteiros powerA,powerB que indicam os poderes dos jogadores A e B, respectivamente.

Saída
A saída deve conter a frase Jogador A vence se o jogador A for mais forte, Jogador B vence se o jogador B for mais forte ou Dois jogadores igualmente fracos se ambos jogadores possuem a mesma força.
"""


def riscu(a, b):
    if a > b:
        print('Jogador A vence')
    elif b > a:
        print('Jogador B vence')
    else:
        print('Dois jogadores igualmente fracos')

#Questão 12
"""
Você foi convidado para jogar um jogo. Nesse jogo, você irá receber dois inteiros a e b. Em uma jogada, você pode escolher qualquer inteiro k entre 1 até 10 e adicionar em a ou subtrair de a. Em outras palavras, você escolhe um inteiro  k∈[1;10] e executa a:=a+k ou a:=a−k. Você pode usar valores diferentes de k em diferentes jogadas se quiser.

Seu papel é encontrar o número mínimo de jogadas para transformar a em b.

Escreva uma função jogadas(a, b) que imprima o que lhe é pedido.

Entrada
Os parâmetros da função são dois inteiros a,b≥1.

Saída
Imprima um número - o número mínimo de jogadas para transformar a em b.
"""


def jogadas(a, b):
    if a < b:
        a, b = b, a

    diff = a - b
    ans = diff // 10

    if diff % 10 != 0:
        ans += 1

    print(ans)

#Questão 13
"""
Na maior seca da história de Brasília, Lamá e Ladê decidiram comprar uma melancia. Eles escolheram a maior e mais madura que tinha, na opinião deles. Eles pesaram a melancia, viram que ela pesava w kg e então correram para casa, morrendo de sede. Ao chegar, foram dividir a melancia mas encontraram um grande problema.

Lamá e Ladê, fãs de matemática desde cedo, amam números pares. Por isso, eles querem dividir a melancia de um modo que cada uma das duas partes pese um exato número par de kilogramas. Eles estão extremamente cansados e querem comer o quanto  antes, logo eles decidiram pedir a ajuda do universitário, você, para descobrir se podem dividir a melancia do jeito que eles querem.

Claro, o peso de cada pedaço tem que ser um número inteiro maior do que 0.

Escreva a função sedeDeMelancia(w), para resolver o problema requisitado.

Entrada
A entrada consiste de um inteiro 1≤w≤100 que indica o peso da melancia trazida pelos dois.

Saída
Imprima "SIM" se os dois podem dividir a melancia em duas partes, cada uma delas pesando um número par de kg.  Imprima "NAO" caso não seja possível.
"""


def sedeDeMelancia(w):
    if w > 2 and w % 2 == 0:
        print('SIM')
    else:
        print('NAO')

#Questão 14
"""
Entrada
A entrada consiste de um inteiro 0≤n≤100 que indica quantos copos ele levou para você avaliar.

Saída
Imprima "Pode levar pros calourinhos, deivis!" se a quantidade de copos for divisível por 4.  Imprima "Pode voltar pro ceubinho, deivis! Falta(m) x copo(s)!" onde x é o número de copos restantes para que o número se torne divisível por 4, caso não seja possível dar copos para todos os calourinhos.

"""


def qtdcopos(x):
    if x > 0 and x % 4 == 0:
        print('Pode levar pros calourinhos, deivis!')
    else:
        print(
            f'Pode voltar pro ceubinho, deivis! Falta(m) {4 - x % 4} copo(s)!')

#Questão 15
"""
Entrada
A entrada consiste de 1 inteiro x tal que (1<x<105).

Saída
Cada linha da saída deve possuir um inteiro da sequência até o número um, conforme os exemplos.

Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos, por esse critério, caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
"""


def maravilhosos(x):
    if x == 1:
        print(1)
    elif x % 2:
        print(x)
        maravilhosos(x * 3 + 1)
    else:
        print(x)
        maravilhosos(x // 2)


v = int(input())
maravilhosos(v)

#Questão 16
"""
Agora que o Prof. Nerynho já construiu sua piscina, ele está testando um programa de localização pessoal que diz o que Nerynho está fazendo na área de sua piscina, baseado em uma representação cartesiana vista de um satélite!!!! Ajude o Prof Nerynho a desenvolver seu programa, escrevendo a função piscininha(x, y, w, h, a, b) cujas variáveis são:

As primeiras quatro variáveis, x,y,w,h | w,h≥2 representam a piscina, que é um retângulo de altura h e largura w, alinhado aos eixos cartesianos X e Y, cujo vértice inferior esquerdo está no ponto (x,y).
As duas ultimas variáveis,  a e b, representam as coordenadas cartesianas (a,b) de onde o Prof Nerynho está.
Entrada
Os parâmetros da função são seis inteiros x,y,w,h,a,b.

Saída
A saída depende da posição do Prof. Nerynho baseado em onde está sua piscina e:

Caso o professor esteja dentro da piscina, o programa deverá imprimir a frase Dando um tchibum;
Caso o professor esteja fora da piscina, o programa deverá imprimir a frase Tomando um solzin;
Caso o professor esteja na borda da piscina, o programa deverá imprimir a frase So com os pezin dentro da agua.

"""


def piscininha(x, y, w, h, a, b):
    if (a > x) and (a < w + x) and (b > y) and (b < y + h):
        print('Dando um tchibum')
    elif (a < x) or (a > w + x) or (b < y) or (b > y + h):
        print('Tomando um solzin')
    else:
        print('So com os pezin dentro da agua')

#Questão 17
"""
Entrada
Os parâmetros da função são quatro inteiros n,g,f,c≥0 indicando, respectivamente, a quantidade de pessoas existentes no banquete, a quantidade de garfos, a quantidade de facas e a quantidade de colheres.

Saída
Imprima um valor inteiro indicando a maior quantidade possível de pessoas presentes no banquete que conseguirão jantar.
"""


def quantosJantam(n, g, f, c):
    print(min(n, min(g, f) + c))

#Questão 18 
"""
Um triângulo é dito Pitorestico se o tamanho de todos os seus três lados são inteiros e divisíveis por 2, 3 e 5. Dados os tamanhos dos três lados de um triângulo, implemente uma função chamada pitorestico que recebe os três lados do triângulo a, b, c e imprima o que lhe é pedido.

Entrada
Os parâmetros da função são três inteiros a,b,c≥1.

Saída
Imprima "Pitorestico!!!" caso o triângulo formado pelos lados a,b,c seja pitorestico e "Nao foi dessa vez" caso contrário.

"""


def pitorestico(a, b, c):
    if (a % 30 == 0) and (b % 30 == 0) and (c % 30 == 0):
        print('Pitorestico!!!')
    else:
        print('Nao foi dessa vez')
