#Importando o Pygame e o Time
import pygame, time

#Definindo as cores
PRETO = (0,0,0)
AMARELO = (255,255,0)
VERMELHO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

#Definindo o tamanho da janela
LARGURA_JANELA = 500
ALTURA_JANELA = 400

#Criando uma função Mover
def mover(figura,dim_janela):
    """[Função Para Fazer Animações Simples]

    Args:
        figura ([dict]): [figura]
        dim_janela ([tuple]): [dimensões da janela]
    """
    #Dimensões da janela
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]

    #Verifica Se o objeto saiu da tela por cima ou por baixo
    if figura['objRect'].top < borda_superior or figura['objRect'].bottom > borda_inferior:
        #Figura atingiu o tobo ou a base
        figura['vel'][1] = -figura['vel'][1]

    #Verifica Se o objeto saiu da tela pela direita ou pela esquerda
    if figura['objRect'].left < borda_esquerda or figura['objRect'].right > borda_direita:
        #Figura atingiu a esquerda ou a direita
        figura['vel'][0] = -figura['vel'][0]

    #atualizando a posição dos objetos
    figura['objRect'].y += figura['vel'][1]
    figura['objRect'].x += figura['vel'][0]

#Inicializando o pygame
pygame.init()

#Criando Janela
janela = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA))
pygame.display.set_caption('Animação')

#Criando as figuras
f1 = {'objRect':pygame.Rect(300,80,40,80),'cor': VERMELHO,'vel':[0,-5],'forma': 'ELIPSE'}
f2 = {'objRect':pygame.Rect(200,200,20,20),'cor':VERDE,'vel':[5,5],'forma':'ELIPSE'}
f3 = {'objRect':pygame.Rect(100,150,60,60),'cor':AZUL,'vel':[-5,5],'forma': 'RETANGULO'}
f4 = {'objRect':pygame.Rect(200,150,80,40),'cor':AMARELO,'vel':[5,0],'forma':'RETANGULO'}

figuras = [f1,f2,f3,f4]

#Iniciando Variável deve continuar
deve_continuar = True

#Loop principal
while deve_continuar:
    #Se Algo acontecer
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False

    #Preenchendo O Fundo de Preto
    janela.fill(PRETO)

    for figura in figuras:
        #Reposicionando figura
        mover(figura, (LARGURA_JANELA, ALTURA_JANELA))

        #Desenhando as figuras na tela
        if figura['forma'] == 'RETANGULO':
            pygame.draw.rect(janela,figura['cor'],figura['objRect'])
        elif figura['forma'] == 'ELIPSE':
            pygame.draw.ellipse(janela,figura['cor'],figura['objRect'])

    #Atualizando tela
    pygame.display.update()

    #Delay da Atualização
    time.sleep(0.02)