def computador_escolhe_jogada(n, m):
    out = 1
    while out != m:
        if (n - out) % (m + 1) == 0:
            return out
        else:
            out +=1
    return out

def usuario_escolher_jogada(n, m):
    play = False
    while not play:
        out = int(input('Informe sua jogada: '))
        if out < 1 or out > m:
            out = int(input('\nOops! Jogada inválida! Tente de novo: '))
        else:
            play = True
    return out    
        
def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    comp = False
    if n % (m + 1) == 0:
        print('\nVocê começa!')
    else:
        print('\nComputador começa!')
        comp - True
    while n > 0:
        if comp:
            out = computador_escolhe_jogada(n, m)
            n -= out
            if out == 1:
                print('Computador removeu uma peça.')
            else:
                print('Computador removeu {} peças.'.format(out))
            comp = False
        else:
            out = usuario_escolher_jogada(n, m)
            n -= out
            if out == 1:
                print('Usuário removeu uma peça.')
            else:
                print('Usuário removeu {} peças.'.format(out))
                
        
    
    if n == 0:
        print('O computador ganhou!')
    else:
        print('Você ganhou!')



if __name__ == "__main__":
    print('\n')
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('\n')
    print('1 - para jogar uma partida isolada')
    menu = int(input('2 - para jogar um campeonato '))
    
    if menu == 1:
        print('\n')
        print('Você escolheu uma partida isolada!')
        print('\n')
        partida()
    else:
        print('\n')
        print('Você escolheu um campeonato!')
        print('\n')
        
        