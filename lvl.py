import pygame
from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((300, 300), RESIZABLE)
fenetre.blit(pygame.image.load("fond.jpg").convert(), (0,0))



class stage:
	
	def __init__(self):
		
		self.sprite = sprite
		
		
	def niveau (self):
		
		with open(lvl1.txt, "r") as niv: 
			for ligne in niv:
				for car in ligne:
					if car == "d":
						sprite = pygame.image.load("depart.png").convert_alpha()
					if car == "m":
						sprite = pygame.image.load("mur.png").convert_alpha()
					if car == "a":
						sprite = pygame.image.load("arrivee.png").convert_alpha()
						
						
continuer = 1
pygame.key.set_repeat(1, 4)
while continuer:
    for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
