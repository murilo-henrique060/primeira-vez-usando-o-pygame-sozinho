import pygame,random

#definindo cores
PRETO = (0,0,0)
BRANCO = (255,255,255)
VERDE = (0,255,0)

#Definindo constantes
LARGURA_JANELA = 400
ALTURA_JANELA = 500
VELOCIDADE = 6
ITERACOES = 30
TAMANHO_BLOCO = 20

#Movendo o jogador
def moverJogador(jogador,teclas,dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]

    if teclas['esquerda'] and jogador['objRect'].left > borda_esquerda:
        jogador['objRect'].x -= jogador['vel']
    if teclas['direita'] and jogador['objRect'].right < borda_direita:
        jogador['objRect'].x += jogador['vel']
    if teclas['cima'] and jogador['objRect'].top > borda_superior:
        jogador['objRect'].y -= jogador['vel']
    if teclas['baixo'] and jogador['objRect'].bottom < borda_inferior:
        jogador['objRect'].y += jogador['vel']

#Movendo os blocos
def moverBloco(bloco):
    bloco['objRect'].y += bloco['vel']

#inicializando o pygame
pygame.init()

#Criando um timer
relogio = pygame.time.Clock()

#Criando Janela
janela = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA))
pygame.display.set_caption('Utilizando Teclado e Mouse')

#Criando jogador
jogador = {'objRect':pygame.Rect(300,100,50,50),'cor':VERDE,'vel':VELOCIDADE}

#Criando as teclas
teclas = {'esquerda':False,'direita':False,'cima':False,'baixo':False}

#Iniciando outras variáveis
contador = 0
blocos = []
deve_continuar = True

#Loop principal
while deve_continuar:
    for evento in pygame.event.get():
        #Checando se a pessoa saiu do jogo
        if evento.type == pygame.QUIT:
            deve_continuar = False

        #Se for pressionada uma tecla
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                deve_continuar = False
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas['esquerda'] = True
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas['direita'] = True
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas['cima'] = True
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas['baixo'] = True

        #Quando uma tecla é solta
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas['esquerda'] = False
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas['direita'] = False
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas['baixo'] = False
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas['cima'] = False

        #quando um botão do mouse é pressionado
        if evento.type == pygame.MOUSEBUTTONDOWN:
            blocos.append({'objRect':pygame.Rect(evento.pos[0],evento.pos[1],TAMANHO_BLOCO,TAMANHO_BLOCO),'cor':BRANCO,'vel':1})

        #aumentando o contador
        contador += 1
        if contador >= ITERACOES:
            #adicionando um novo bloco
            contador = 0
            posX = random.randint(0,LARGURA_JANELA-TAMANHO_BLOCO)
            posY = TAMANHO_BLOCO
            velRandom = random.randint(1,VELOCIDADE+3)
            blocos.append({'objRect':pygame.Rect(posX,posY,TAMANHO_BLOCO,TAMANHO_BLOCO),'cor':BRANCO,'vel':velRandom})

    #Preenchendo o fundo de preto
    janela.fill(PRETO)

    #Movendo o jogador
    moverJogador(jogador,teclas,(LARGURA_JANELA,ALTURA_JANELA))

    #Desenhando o jogador
    pygame.draw.rect(janela,jogador['cor'],jogador['objRect'])

    #Checando se o jogador bateu no bloco ou se o bloco saiu da tela
    for bloco in blocos[:]:
        bateu = jogador['objRect'].colliderect(bloco['objRect'])
        if bateu or bloco['objRect'].y > ALTURA_JANELA:
            blocos.remove(bloco)

    #Movendo e desenhando os blocos
    for bloco in blocos:
        moverBloco(bloco)
        pygame.draw.rect(janela,bloco['cor'],bloco['objRect'])

    #Atualizando a janela
    pygame.display.update()

    #Renderizando a 40 fps
    relogio.tick(40)