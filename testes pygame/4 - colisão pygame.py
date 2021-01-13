#Importando o pygame
import pygame

#Definindo as cores
PRETO = (0,0,0)
BRANCO = (255,255,255)
AMARELO = (255,255,0)
VERMELHO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

#Definindo o tamanho da tela
LARGURA_JANELA = 500
ALTURA_JANELA = 400

#Definindo a função mover()
def mover(figura,dim_janela):
    borda_esquerda = 0
    borda_topo = 0
    borda_direita = dim_janela[0]
    borda_baixo = dim_janela[1]
    if figura['objRect'].top < borda_topo or figura['objRect'].bottom > borda_baixo:
        #O objeto atingiu o topo ou a base da janela
        figura['vel'][1] = -figura['vel'][1]
    if figura['objRect'].left < borda_esquerda or figura['objRect'].right > borda_direita :
        #O objeto atingiu a parede esquerda ou a direita
        figura['vel'][0] = -figura['vel'][0]
    #Atualizando a posição
    figura['objRect'].x += figura['vel'][0]
    figura['objRect'].y += figura['vel'][1]

#Inicializndo o pygame
pygame.init()

#Criando uma função relogio com pygame.time.Clock()
relogio = pygame.time.Clock()

#Criando a janela
janela = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA))
pygame.display.set_caption('Colisão')

#Criando blocos e colocando-os em uma lista
b1 = {'objRect': pygame.Rect(375,80,40,40),'cor':VERMELHO,'vel':[0,2]}
b2 = {'objRect': pygame.Rect(175,200,40,40),'cor':VERDE,'vel':[0,-3]}
b3 = {'objRect': pygame.Rect(275,150,40,40),'cor':AMARELO,'vel':[0,-1]}
b4 = {'objRect': pygame.Rect(75,150,40,40),'cor':AZUL,'vel':[0,4]}
blocos = [b1,b2,b3,b4]

#Criando a bola
bola = {'objRect':pygame.Rect(270,330,30,30),'cor':BRANCO,'vel':[3,3]}

#Criando a variável deve continuar
deve_continuar = True

#Loop principal
while deve_continuar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False

    #preenchendo a janela de preto
    janela.fill(PRETO)

    for bloco in blocos:
        #Reposicionando os blocos
        mover(bloco,(LARGURA_JANELA,ALTURA_JANELA))

        #Desenhando o bloco na janela
        pygame.draw.rect(janela,bloco['cor'],bloco['objRect'])

        #Mudando a cor da bola caso ela colida com algum bloco
        mudarCor = bola['objRect'].colliderect(bloco['objRect'])
        if mudarCor:
            bola['cor'] = bloco['cor']

    #Reposicionando ee desenhando a bola
    mover(bola,(LARGURA_JANELA,ALTURA_JANELA))
    pygame.draw.ellipse(janela,bola['cor'],bola['objRect'])

    #Mostrando tudo o que foi desenhado
    pygame.display.update()

    #Limitando a 40 quadros por segundo
    relogio.tick(40)