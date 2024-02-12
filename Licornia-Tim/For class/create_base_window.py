import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((800, 600))

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0, 0))

#chargement des sprites
eau = pygame.image.load("eau.png").convert()
eau_x = -1000
eau_y = -1000

terre = pygame.image.load("terre.png").convert()
terre_x = -1000
terre_y = -1000

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = True
while continuer :
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == MOUSEBUTTONDOW:
            if event.button == 1:
            	eau_x = 320
            	eau_y = 260
        	if event.button == 3:
            	terre_x = 400
            	terre_y = 260

	fenetre.blit(eau, (eau_x, eau,y))
	fenetre.blit(terre, (terre_x, terre_y))
	pygame.display.flip()

pygame.quit()