from typing import Final
import pygame
import exemple3
from pygame.locals import *


class Joueur:
    IMAGE = "OIP__1_-removebg-preview (1).png"
    TAILLE_BLOC = 44
    VITESSE_PIXEL_SECONDE: Final = 10
    VITESSE_PIXEL_FRAME: Final = VITESSE_PIXEL_SECONDE * exemple3.App.DURÉE_FRAME

    def __init__(self, x, y):
        self.dernière_direction = None
        self.x = x
        self.y = y
        self.image = pygame.image.load(self.IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.TAILLE_BLOC, self.TAILLE_BLOC))
        self.direction = None
        self.vitesse = 0

    def dessiner(self, surface_jeu):
        surface_jeu.blit(self.image, (self.x, self.y))

    def aller_gauche(self):
        self.x = max(self.x - self.vitesse, 0)

    def aller_droite(self):
        self.x += self.vitesse
        if self.x > 800 - self.TAILLE_BLOC:
            self.x = 800 - self.TAILLE_BLOC

    def aller_haut(self):
        self.y = max(self.y - self.vitesse, 0)

    def aller_bas(self):
        self.y += self.vitesse
        if self.y > 600 - self.TAILLE_BLOC:
            self.y = 600 - self.TAILLE_BLOC

    def maj_direction(self, key):
        self.direction = key

    def steve_bouge(self):
        if self.direction is None: return
        if self.vitesse == 0 or self.direction != self.dernière_direction:
            self.vitesse = self.VITESSE_PIXEL_FRAME
        else:
            self.vitesse += self.VITESSE_PIXEL_FRAME

        if self.direction == K_UP or self.direction == K_w:
            self.aller_haut()
        elif self.direction == K_DOWN or self.direction == K_s:
            self.aller_bas()
        elif self.direction == K_LEFT or self.direction == K_a:
            self.aller_gauche()
        elif self.direction == K_RIGHT or self.direction == K_d:
            self.aller_droite()
        else:
            pass
        self.dernière_direction = self.direction