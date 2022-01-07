from classes import *
import pygame
import math
from random import randint

pygame.init()

pygame.display.set_caption("Hanged Man Game")
pygame.display.set_icon(pygame.image.load('assets/images/logo.jpg'))
screen = pygame.display.set_mode((700, 431))
background = pygame.image.load('assets/images/background.jpg')
button = pygame.image.load('assets/images/playbutton.png')
button = pygame.transform.scale(button, (200, 200))
button_rect = button.get_rect()
button_rect.x = math.ceil((screen.get_width()-button.get_width())/2)
button_rect.y = math.ceil((screen.get_height()-button.get_height())/2)

button2 = pygame.image.load('assets/images/mainmenubutton.png')
button2 = pygame.transform.scale(button2, (200, 57))
button_rect2 = button2.get_rect()
button_rect2.x = math.ceil((screen.get_width()-button2.get_width())/2)
button_rect2.y = math.ceil((screen.get_height()-button2.get_height())/1.8)

allwords = "abcdefghijklmnopqrstuvwxyz0123456789"
buttons = {}

block = [125, 315]
start_pos = [125, 315]
end_pos = [153, 343]
repeat = 0
for wrd in allwords:
    repeat += 1
    if repeat == 14:
        block = [125, 350]
        start_pos = [125, 350]
        end_pos = [153, 378]
    if repeat == 27:
        block = [125, 385]
        start_pos = [125, 385]
        end_pos = [153, 413]
    buttons[wrd] = {}
    buttons[wrd]["block"] = pygame.Rect(block[0], block[1], 30, 30)
    buttons[wrd]["start_pos"] = (start_pos[0], start_pos[1])
    buttons[wrd]["end_pos"] = (end_pos[0], end_pos[1])
    buttons[wrd]["closed"] = False
    block[0] += 35.75
    start_pos[0] += 35.75
    end_pos[0] += 35.75

running = True

game = Game(screen)

rand = randint(0, len(game.possiblewords)-1)
word = game.possiblewords[rand]

while running:
    screen.blit(background, (0, 0))

    if game.isplaying:
        if game.endgame["ended"] == True:
            game.end(screen, word, button2, button_rect2)
        else:
            game.update(screen, word)
            for key in buttons:
                    if buttons[key]["closed"] == True:
                        pygame.draw.line(screen, (255, 0, 0), buttons[key]["start_pos"], buttons[key]["end_pos"])
                        start_pos = (buttons[key]["start_pos"][0] + 28, buttons[key]["start_pos"][1])
                        end_pos = (buttons[key]["end_pos"][0] - 28, buttons[key]["end_pos"][1])
                        pygame.draw.line(screen, (255, 0, 0), start_pos, end_pos)
    else:
        screen.blit(button, button_rect)
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos) and not game.isplaying and not game.endgame["ended"]:
                game.isplaying = True
            if button_rect2.collidepoint(event.pos) and game.isplaying and game.endgame["ended"]:
                game.isplaying = False
                game.endgame["ended"] = False
                game.endgame["winned"] = False
                game.foundwords = []
                game.pendu.parts = 0
                game.pendu.image = pygame.image.load(f'assets/images/hanged_man_parts/hanged_man_part_{game.pendu.parts}.png')
                for key in buttons:
                    if buttons[key]["closed"] == True:
                        buttons[key]["closed"] = False
                rand = randint(0, len(game.possiblewords)-1)
                word = game.possiblewords[rand]
            for key in buttons:
                if buttons[key]["block"].collidepoint(event.pos) and game.isplaying and not game.endgame["ended"]:
                    if not key in game.foundwords:
                        buttons[key]["closed"] = True
                        game.foundwords.append(key)
                        if not key in word:
                            game.pendu.parts += 1