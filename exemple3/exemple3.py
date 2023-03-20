from datetime import time
import time
from typing import Final

import pygame
from pygame.locals import *


class Joueur:
    IMAGE = "OIP__1_-removebg-preview (1).png"
    TAILLE_BLOC = 44
    VITESSE_PIXEL_SECONDE: Final = 10
    VITESSE_PIXEL_FRAME: Final = VITESSE_PIXEL_SECONDE * 1/30

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(self.IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.TAILLE_BLOC, self.TAILLE_BLOC))
        self.direction = None

    def dessiner(self, surface_jeu):
        surface_jeu.blit(self.image, (self.x, self.y))

    def aller_gauche(self):
        self.x = max(self.x - self.TAILLE_BLOC, 0)

    def aller_droite(self):
        self.x += self.TAILLE_BLOC
        if self.x > 800 - self.TAILLE_BLOC:
            self.x = 800 - self.TAILLE_BLOC

    def aller_haut(self):
        self.y = max(self.y - self.TAILLE_BLOC, 0)

    def aller_bas(self):
        self.y += self.TAILLE_BLOC
        if self.y > 600 - self.TAILLE_BLOC:
            self.y = 600 - self.TAILLE_BLOC

    def maj_direction(self, key):
        self.direction = key

    def steve_bouge(self):
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




class App:
    DURÉE_FRAME = 1 / 30
    DIMENSION = (800, 600)

    def __init__(self):
        pygame.init()
        self.surface_jeu = pygame.display.set_mode(self.DIMENSION, pygame.HWSURFACE)
        self.jeu_roule = True
        self.joueur = Joueur(self.DIMENSION[0] // 2, self.DIMENSION[1] // 2)


    def traiter_input(self):
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYUP and event.key == K_ESCAPE:
                self.jeu_roule = False
            elif event.type == MOUSEMOTION:
                pass
            elif event.type == KEYUP and event.key in [K_LEFT, K_RIGHT, K_UP, K_DOWN, K_w, K_s, K_d, K_a]:
                self.joueur.maj_direction(event.key)
            elif event.type == KEYUP and event.key == K_SPACE:
                self.joueur.STOP()
            else:
                print(event)

    def appliquer_logique(self):
        self.joueur.steve_bouge()

    def maj_écran(self):
        self.surface_jeu.fill((0, 100, 0))
        self.joueur.dessiner(self.surface_jeu)
        pygame.display.flip()

    def exécuter_game_loop(self):
        while self.jeu_roule:
            self.traiter_input()
            self.appliquer_logique()
            self.maj_écran()
            time.sleep(self.DURÉE_FRAME)


if __name__ == '__main__':
    app = App()
    app.exécuter_game_loop()
