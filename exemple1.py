import pygame

jeu_roule = True

def traiter_input():
    pygame.event.pump()

def appliquer_logique():
    pass

def maj_écran():
    pass

def main():
    pygame.init()
    pygame.display.set_mode((800, 600), pygame.HWSURFACE)

    while jeu_roule:
        traiter_input()
        appliquer_logique()
        maj_écran()

    pygame.quit()

if __name__ == '__main__':
    main()
