from datetime import time
import time
import pygame
from pygame.locals import *

class Joueur:
    IMAGE = "images/OIP__1_-removebg-preview (1).png"
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(self.IMAGE).convert_alpha()

    def dessiner(self, surface_jeu):
        surface_jeu.blit(self.image, (self.x, self.y))



class App:
    DURÉE_FRAME = 1 / 30
    DIMENSION = (800, 600)

    def __init__(self):
        pygame.init()
        self.surface_jeu = pygame.display.set_mode(self.DIMENSION, pygame.HWSURFACE)
        self.jeu_roule = True
        self.joueur = Joueur(self.DIMENSION[0] // 2, self.DIMENSION[1] // 2)
        self.image = pygame.transform.scale(self.image, (44,44))



    def traiter_input(self):
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYUP and event.key == K_ESCAPE:
                self.jeu_roule = False
            elif event.type == MOUSEMOTION:
                pass
            else:
                print(event)

    def appliquer_logique(self):
        pass

    def maj_écran(self):
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
