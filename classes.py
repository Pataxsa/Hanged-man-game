import pygame
import math

class Game:

    def __init__(self, screen):
        self.isplaying = False
        self.pendu = Pendu(screen)
        self.clavier = Clavier(screen)
        self.bar = pygame.transform.scale(pygame.image.load('assets/images/bar.png'), (40, 40))
        self.foundwords = []
        self.possiblewords = ["axel"]
    
    def update(self, screen, word):
        words = 0

        screen.blit(self.pendu.image, self.pendu.rect)
        screen.blit(self.clavier.image, self.clavier.rect)
        for wrd in word:
            words += 40

            screen.blit(self.bar, (280 + words,  math.ceil((screen.get_height()-self.bar.get_height())/2)))
            if wrd in self.foundwords:
                font = pygame.font.SysFont('Sans', 40)
                text = font.render(wrd, True, (255, 0, 0))
                
                screen.blit(text, (290 + words,  math.ceil((screen.get_height()-self.bar.get_height())/2) - 29))

class Pendu(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.parts = 0
        self.image = pygame.image.load('assets/images/hanged_man.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = math.ceil((screen.get_width()-self.image.get_width())/5)
        self.rect.y = math.ceil((screen.get_height()-self.image.get_height())/2)-40

class Clavier():

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load('assets/images/keyboard.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = math.ceil((screen.get_width()-self.image.get_width())/2)
        self.rect.y = math.ceil(screen.get_height()-self.image.get_height())
