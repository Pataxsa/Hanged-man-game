from classes import *
import pygame
import math
from random import randint

pygame.init()

pygame.display.set_caption("Le pendu")
pygame.display.set_icon(pygame.image.load('assets/images/logo.jpg'))
screen = pygame.display.set_mode((700, 431))
background = pygame.image.load('assets/images/background.jpg')
button = pygame.image.load('assets/images/playbutton.png')
button = pygame.transform.scale(button, (200, 200))
button_rect = button.get_rect()
button_rect.x = math.ceil((screen.get_width()-button.get_width())/2)
button_rect.y = math.ceil((screen.get_height()-button.get_height())/2)
buttons = {
    "a": pygame.rect.Rect(125, 314, 30, 30),
    "b": pygame.rect.Rect(160, 314, 30, 30),
    "c": pygame.rect.Rect(195, 314, 30, 30),
    "d": pygame.rect.Rect(195+35, 314, 30, 30),
    "e": pygame.rect.Rect(195+35+35, 314, 30, 30)
}

running = True

game = Game(screen)

rand = randint(0, len(game.possiblewords)-1)
word = game.possiblewords[rand]

while running:
    screen.blit(background, (0, 0))

    if game.isplaying:
        game.update(screen, word)
    else:
        screen.blit(button, button_rect)
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Jeu fermé")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if button_rect.collidepoint(event.pos) and not game.isplaying:
                print("Play !")
                game.isplaying = True
            for key in buttons:
                if buttons[key].collidepoint(event.pos) and game.isplaying:
                    print(key)
                    if not key in game.foundwords:
                        game.foundwords.append(key)