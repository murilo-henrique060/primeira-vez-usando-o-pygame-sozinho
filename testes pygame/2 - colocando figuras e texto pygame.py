#iniciando o Pygame
import pygame
from pygame.constants import QUIT
pygame.init()

#Definindo o tamanho da janela
LARGURA_JANELA = 600
ALTURA_JANELA = 600

#Definindo Cores:
PRETO = (0,0,0)
BRANCO = (255,255,255)
VERMELHO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

#Definindo Arredondamento de Pi:
PI = 3.1416

#Criando Janela e Dando Nome De Figuras e texto
janela = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA))
pygame.display.set_caption('Figuras e texto')

#Preenchendo o Fundo de Branco
janela.fill(BRANCO)

#Trabalhando com Texto
fonte = pygame.font.Font(None,42)
texto = fonte.render('Estou escrevendo com Pygame',True,BRANCO,AZUL)

#Escrevendo na Tela
janela.blit(texto,[(100), (ALTURA_JANELA / 2)])

#Desenhando na tela
pygame.draw.line(janela, VERDE, (30,30), (500,30), 5)

#Desenhando um poligono
pygame.draw.polygon(janela,PRETO,((300,350),(500,550),(100,550)),0)

#Desenhando um círculo
pygame.draw.circle(janela, AZUL, (300,150), 20.0, 0)

#Desenhando uma elipse
pygame.draw.ellipse(janela,VERMELHO ,(50,100,50,100),1)

#Desenhando um retângulo
pygame.draw.rect(janela, VERDE, (400,125,100,50), 0)

#Desenhando um arco
pygame.draw.arc(janela, VERMELHO, (150,100,75,100), PI/2 , 3*PI/2)

continuar = True

while continuar:
    pygame.display.update()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            continuar = False