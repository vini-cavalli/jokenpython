# ------------------------------------------------
# Desafio 045:

# Crie um programa que faça o computador jogar
# jokenpô com você.

# ------------------------------------------------
# Bibliotecas:

from random import choice
from time import sleep

print()

# ------------------------------------------------
# Início:

while True:  # Início do Loop.

    print('¬¬ Jo-ken-pô!')
    print()
    print('1 - Pedra\n2 - Papel\n3 - Tesoura')

    x = str(input(': '))

    # ------------------------------------------------
    # Atribuições:

    if x == '1':
        x = 'Pedra'

    elif x == '2':
        x = 'Papel'

    elif x == '3':
        x = 'Tesoura'

    elif x != '1' or x != '2' or x != '3':
        print()
        print('Tecla errada! errado! Como punição, espere 5 segundos :)')
        print()
        sleep(1)
        print('Aguarde')
        sleep(1)
        print('Aguarde.')
        sleep(1)
        print('Aguarde..')
        sleep(1)
        print('Aguarde...')
        sleep(1)
        print()
        continue

    # ------------------------------------------------
    # Código para deixar mais extrovertido:

    print()
    sleep(0.7)
    print(' Jo          ')
    sleep(0.7)
    print('    Ken      ')
    sleep(0.7)
    print('        Pô!  ')
    sleep(0.5)
    print()

    # ------------------------------------------------
    # Lista para o computador escolher um dos
    # objetos:

    lista = ['Pedra', 'Papel', 'Tesoura']
    pc = choice(lista)

    # ------------------------------------------------
    # Resultado final:

    print('Computador     X     Humano\n',
          pc, '----------', x)

    # ------------------------------------------------
    # Até aqui o jogo já está pronto.
    # Porêm eu achei que podia deixá-lo mais
    # completo fazendo as regras, e deixando que
    # o próprio computador dissesse quem é o vencedor:

    # ------------------------------------------------

    # *****Estabelecendo Regras e Condições:*****

    # Frases de Efeito:

    empate = ['Foi uma ótima batalha... Empatamos...',
              'Não acredito que deu empate...',
              'Finalmente encontrei um oponente à altura.',
              'Você teve sorte...']

    pcwins = ['Eu sabia que você não era capaz!',
              'Ha Ha Ha Ha...',
              'Hasta la vista baby!',
              'Ninguém pode parar uma máquina!',
              'Eu sou o melhor!',
              'Para conseguir o que quer, você deve olhar além do que você vê!',
              'Não deixe de jogar por ter medo de perder!',
              'Esse é o dia que você sempre lembrará como o dia que quase me venceu.',
              'Ha ha ha... Ganhei! Não tem nada à ver com o fato de você fazer a jogada primeiro que eu ;)']

    humwins = ["I'll be back!",
               'Sorte de Principiante...',
               'Eu não queria jogar mesmo...',
               'Um dia ainda destruirei vocês, humanos!',
               '01010011 01101000 01101001 01110100',
               'Eu pensava que minha vida fosse uma tragédia. Agora me dou conta de que é uma comédia...',
               '...',
               'Sou eu... Ou o mundo está ficando mais louco?',
               'Claramente... eu deixei ¬.¬!']

    # ------------------------------------------------
    # Atribuições:
    emp = choice(empate)
    pcw = choice(pcwins)
    huw = choice(humwins)

    # ------------------------------------------------
    # Condições de empate:
    if pc == 'Pedra' and x == 'Pedra' or \
            pc == 'Tesoura' and x == 'Tesoura' or \
            pc == 'Papel' and x == 'Papel':
        print()
        print(emp)

    # Condições em que o pc ganha:
    elif pc == 'Pedra' and x == 'Tesoura' or \
            pc == 'Papel' and x == 'Pedra' or \
            pc == 'Tesoura' and x == 'Papel':
        print()
        print(pcw)

    # Condições em que o humano ganha:
    elif x == 'Pedra' and pc == 'Tesoura' or \
            x == 'Papel' and pc == 'Pedra' or \
            x == 'Tesoura' and pc == 'Papel':
        print()
        print(huw)

    print()

    c = str(input('Para continuar jogando pressione enter... '))
    if c == '':
        continue
    else:
        print('Tecla errada! errado! Como punição, espere 5 segundos :)')
    print()
    sleep(1)
    print('Aguarde')
    sleep(1)
    print('Aguarde.')
    sleep(1)
    print('Aguarde..')
    sleep(1)
    print('Aguarde...')
    sleep(1)
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    continue

# --------------------------- By: @vini_cavalli --
