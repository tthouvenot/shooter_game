import pygame

from player import Player

# On crée la classe qui représente le jeu
class Game:

    def __init__(self):
        # On charge le joueur
        self.player = Player() 
        self.pressed = {}
        