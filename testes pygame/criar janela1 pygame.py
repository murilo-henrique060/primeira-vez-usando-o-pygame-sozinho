#Importar o pygame:
import pygame

#Iniciando os Módulos Do pygame
pygame.init()


#Constantes São Variáveis Imutáveis e São Representadas por palavras com todas as letras maiúsculas:
LARGURA_JANELA = 500
ALTURA_JANELA = 700

#Comando Para criar janela:
janela = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA))
#A Largura e a Altura Ficam Dentro de uma Tupla

#Dando um Título Para a Janela
pygame.display.set_caption('Título')

#Variável Para Informar Se A Pessoa Fechou a Janela
deve_continuar = True

#Loop Principal:
#Se a Pessoa Não Fechar a janela, o loop continua:
while deve_continuar:
    #Verificando Se Algo Aconteceu
    for evento in pygame.event.get():
        #Se a Pessoa Apertou Para Sair:
        if evento.type == pygame.QUIT:
            #A Variável deve_continuar encerra o programa:
            deve_continuar = False

#Fechando todos os módulos PyGame:
pygame.quit()