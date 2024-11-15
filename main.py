#  On importe le module pygame et on initialise le module
import pygame
from game import Game

pygame.init()

#  On génère la fenêtre
pygame.display.set_caption("Shooter Game")
screen = pygame.display.set_mode((1080, 720))

# On charge une image de fond
background = pygame.image.load('./assests/principal.png')

#  On charge le jeu
game = Game()

#  On gère les fps
clock = pygame.time.Clock()

#  On gère la boucle principale
running = True
while running:

    # On applique l'image de fond à la fenêtre
    screen.blit(background, (0, 0))

    # On affiche le joueur
    screen.blit(game.player.image, game.player.rect)

    # On déplace le joueur
    if game.pressed.get(pygame.K_LEFT):
        game.player.move_left()
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    if game.pressed.get(pygame.K_UP):
        game.player.move_up()
    if game.pressed.get(pygame.K_DOWN):
        game.player.move_down()

    # On affiche les changements à l'écran
    pygame.display.flip()
    
    # On vérifie sur le joueur ferme la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # On détecte le joueur appuie sur les touches directionnelles
        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

             


    
    clock.tick(60)  # On limite les fps à 60

    