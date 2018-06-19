import pygame
from pygame.locals import *
import constantes



class dk:
	
	def __init__(self, image, pos, x, y):
		
		self.image = image # change l'image de direction quand dk change de direction
		self.pos = pos # position de dk 
		self.x = x
		self.y = y
		
		
		
		
	
	def deplacement(self, k):
		lv = stage(k)
		lv.niveau()
		
		for event in pygame.event.get():
			
			if event.type == KEYDOWN:
				if event.key == K_DOWN:
					self.image = pygame.image.load("dk_bas.png").convert_alpha()
					if self.y < 14:
						if not lv.sprite[self.y+1][self.x] == "m":	
							self.pos = self.pos.move(0, 30)
							self.y += 1
							
					
				if event.key == K_UP:
					self.image = pygame.image.load("dk_haut.png").convert_alpha()
					if self.y > 0:
						if not lv.sprite[self.y-1][self.x] == "m":
							self.pos = self.pos.move(0, -30)
							self.y -= 1
					
					
				if event.key == K_RIGHT:
					self.image = pygame.image.load("dk_droite.png").convert_alpha()
					if self.x < 14:
						if not lv.sprite[self.y][self.x+1] == "m":
							self.pos = self.pos.move(30, 0)
							self.x += 1
							
				if event.key == K_LEFT:
					self.image = pygame.image.load("dk_gauche.png").convert_alpha()
					if self.x > 0:
						if not lv.sprite[self.y][self.x-1] == "m":
							self.pos = self.pos.move(-30, 0)
							self.x -= 1
					
			
				
	
		
		
					
				


class stage:
	
	def __init__(self, k):
		
		sprite = list()
		self.sprite = sprite
		self.k = k		# k est le niveau dans lequel on joue
		
		
	def niveau(self):  # on genere le niveau
		
		c = "lvl" + str(self.k)+".txt"
			
		with open(c, "r") as niv: # lvl est une variable ayant pour valeur un fichier lvln.txt
			
			j = 0
			for ligne in niv:
				
				self.sprite.append([])
				for car in ligne:
					if car != "\n":
						self.sprite[j].append(car)
				j += 1
						
			
			
				
		
		
		
	def affiche_niveau(self, fenetre): # affichage du niveau
		
	
	
		m = 0
		i = 0
	
		while i < len(self.sprite):
			j = 0
			n = 0
			while j < len(self.sprite[i]):
				if self.sprite[i][j] == "a":
					fenetre.blit(pygame.image.load("arrivee.png").convert_alpha(), (n, m))
				
				if self.sprite[i][j] == "d":
					fenetre.blit(pygame.image.load("depart.png").convert(), (n, m))
				if self.sprite[i][j] == "m":
					fenetre.blit(pygame.image.load("mur.png").convert(), (n, m))

				j += 1
				n += 30
			i += 1
			m += 30
	
			
			
		
		
	
		
		
						
						
						
	
						
