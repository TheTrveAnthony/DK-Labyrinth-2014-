import pygame
from pygame.locals import *

pygame.display.init()
nb_sprite = 15
taille_sprite = [30, 30]
taille_fenetre = [nb_sprite*taille_sprite[0], nb_sprite*taille_sprite[1]]
fenetre = pygame.display.set_mode((taille_fenetre[0], taille_fenetre[1]))
fond = pygame.image.load("fond.jpg").convert()
accueil = pygame.image.load("accueil.png").convert()
depart = pygame.image.load("depart.png").convert()
arrive = pygame.image.load("arrivee.png").convert()
mur = pygame.image.load("mur.png").convert()
dk_debut = pygame.image.load("dk_bas.png").convert_alpha()
pos_debut = dk_debut.get_rect()
