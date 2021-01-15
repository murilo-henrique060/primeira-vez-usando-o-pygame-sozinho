import pygame
pygame.init()

LARGURA_JANELA = 700
ALTURA_JANELA = 600

VELOCIDADEX = 8
VELOCIDADEY = 4

TAMANHO_BOLA = 30

BRANCO = (255,255,255)
PRETO = (0,0,0)

class Bola(pygame.sprite.Sprite):

    def __init__(self,cor,tamanho):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([tamanho,tamanho])
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect[0] = LARGURA_JANELA/2
        self.rect[1] = ALTURA_JANELA/2
janela = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA))
pygame.display.set_caption('Classes')

bola_grupo = pygame.sprite.Group()
bola = Bola(BRANCO,TAMANHO_BOLA)
bola_grupo.add(bola)

deve_continuar = True
while deve_continuar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False
    bola_grupo.update()
    bola_grupo.draw(janela)
    pygame.display.update()