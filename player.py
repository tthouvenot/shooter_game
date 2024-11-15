import pygame

# On crée la classe player
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.shield = 0
        self.defense = 10
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('./assests/player/ship/S_PlayerShip_A1.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.y = 360

    def move_left(self):
        self.rect.x -= self.velocity
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self):
        self.rect.x += self.velocity
        if self.rect.x > 1080 - self.rect.width:
            self.rect.x = 1080 - self.rect.width

    def move_up(self):
        self.rect.y -= self.velocity
        if self.rect.y < 0:
            self.rect.y = 0
        
    def move_down(self):
        self.rect.y += self.velocity
        if self.rect.y > 720 - self.rect.height:
            self.rect.y = 720 - self.rect.height
    