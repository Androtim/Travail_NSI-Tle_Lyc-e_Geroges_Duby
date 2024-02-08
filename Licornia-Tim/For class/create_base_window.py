import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((800, 600))

#Chargement et collage du fond
eau = pygame.image.load("eau.png").convert()
terre = pygame.image.load("terre.png").convert()
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0, 0))


#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = True
while continuer :
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            fenetre.blit(eau, (320, 260))
        if event.type == MOUSEBUTTONDOWN and event.button == 3:
            fenetre.blit(terre, (400, 260))

        if event.type == KEYDOWN and event.key == K_SPACE:
        	print("Espace")

pygame.quit()