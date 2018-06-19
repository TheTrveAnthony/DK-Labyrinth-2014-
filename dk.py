import pygame
from pygame.locals import *
from constantes import *
from classes import *


pygame.init()
fenetre.blit(fond, (0,0))



continuer = 1
while continuer:
	for event in pygame.event.get(): # boucle principale
		if event.type == QUIT:
			continuer = 0
	
		mennu = True
		game = True # booleen qui passera a faux pour quitter le menu
		while mennu: # boucle menu
			pygame.time.Clock().tick(30) # limitation de vitesse pour ne pas surcharger le processeur
			fenetre.blit(accueil, (0, 0))
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == QUIT:
					continuer = 0
					mennu = False
					game = False
					
				if event.type == KEYDOWN:
					if event.key == K_F1:
						lvl = 1
						mennu = False 
					if event.key == K_F2:
						lvl = 2
						mennu = False 
						
							
		
		 # pareillement que pour menu
		fenetre.blit(fond, (0, 0))
		fenetre.blit(dk_debut, pos_debut)
		niv = stage(lvl)
		niv.niveau()
		niv.affiche_niveau(fenetre)
		pygame.display.flip()
		donkey = dk(dk_debut, pos_debut, 0, 0)
		while game:
			pygame.time.Clock().tick(30)
			donkey.deplacement(lvl)
			fenetre.blit(fond, (0, 0))
			niv.affiche_niveau(fenetre)
			fenetre.blit(donkey.image, donkey.pos)
			pygame.display.flip()
			if niv.sprite[donkey.x][donkey.y] == "a":
				game = False
				
				
				
					
					
