import pygame
import math

class Game:

    def __init__(self, screen):
        self.isplaying = False
        self.pendu = Hanged(screen)
        self.clavier = KeyBoard(screen)
        self.foundwords = []
        self.possiblewords = ["bed", "computer", "0BL1V10N", "incredible", "destroy", "cat", "potato", "developper", "minecraft"]
        self.endgame = {"winned": False, "ended": False}
    
    def update(self, screen, word):
        wordsspace = 0
        validwords = 0

        screen.blit(self.pendu.image, self.pendu.rect)
        screen.blit(self.clavier.image, self.clavier.rect)

        self.pendu.image = pygame.image.load(f'assets/images/hanged_man_parts/hanged_man_part_{self.pendu.parts}.png')
        for wrd in word:
            wordsspace += 40
            wrd = wrd.lower()

            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(235 + wordsspace,  math.ceil((screen.get_height()/2)), 30, 6))
            if wrd in self.foundwords:
                validwords += 1
                font = pygame.font.SysFont('Sans', 40)
                text = font.render(wrd.upper(), True, (60, 60, 60))
                    
                screen.blit(text, (240 + wordsspace,  math.ceil((screen.get_height()/2)) - 43))

        if validwords == len(word):
            self.endgame["ended"] = True
            self.endgame["winned"] = True
        elif self.pendu.parts == 6:
                self.endgame["ended"] = True
                self.endgame["winned"] = False
            

    def end(self, screen, word, button, button_rect):
        if self.endgame["winned"]:
            font = pygame.font.SysFont('Sans', 40)
            text = font.render("You win !", True, (60, 60, 60))
            text_rect = text.get_rect()
            text_rect.x = math.ceil((screen.get_width()-text.get_width())/2)
            text_rect.y = math.ceil((screen.get_height()-text.get_height())/3.5)
        else:
            font = pygame.font.SysFont('Sans', 40)
            text = font.render("You lost !", True, (60, 60, 60))
            text_rect = text.get_rect()
            text_rect.x = math.ceil((screen.get_width()-text.get_width())/2)
            text_rect.y = math.ceil((screen.get_height()-text.get_height())/3.5)

        text2 = font.render(f"The word was: {word}", True, (60, 60, 60))
        text2_rect = text2.get_rect()
        text2_rect.x = math.ceil((screen.get_width()-text2.get_width())/2)
        text2_rect.y = math.ceil((screen.get_height()-text2.get_height())/2.5)
                    
        screen.blit(text, text_rect)
        screen.blit(text2, text2_rect)
        screen.blit(button, button_rect)

class Hanged():

    def __init__(self, screen):
        super().__init__()
        self.parts = 0
        self.image = pygame.image.load('assets/images/hanged_man_parts/hanged_man_part_0.png')
        self.rect = self.image.get_rect()
        self.rect.x = math.ceil((screen.get_width()-self.image.get_width())/5)
        self.rect.y = math.ceil((screen.get_height()-self.image.get_height())/2)-40

class KeyBoard():

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load('assets/images/keyboard.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = math.ceil((screen.get_width()-self.image.get_width())/2)
        self.rect.y = math.ceil(screen.get_height()-self.image.get_height())
