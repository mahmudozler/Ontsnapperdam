import pygame, sys
from pygame.locals import *

pygame.init()

Background = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption('Kans kaartjes')


BLACK = (0,0,0)
WHITE = (255,255,255)

BGcolor = WHITE
Background.fill(BGcolor)
score = 0

Kanskaart = pygame.image.load('kans.png')
flip = pygame.image.load('kaart.png')
YesButton = pygame.transform.smoothscale(Kanskaart, (175, 175))
NoButton = pygame.transform.smoothscale(flip, (175, 175))

fontObj = pygame.font.Font('freesansbold.ttf', 64)
textSurfaceObj = fontObj.render('Click the card', True, BLACK, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (400,100)

scoreText = pygame.font.Font('freesansbold.ttf', 24)
scoreSurfaceObj = scoreText.render('Score', True, BLACK, WHITE)
scoreRectObj = scoreSurfaceObj.get_rect()
scoreRectObj.center = (600,50)

myfont = pygame.font.SysFont("monospace", 16)

Background.blit(textSurfaceObj, textRectObj)
Background.blit(Kanskaart, (450, 300))
# Background.blit(scoreSurfaceObj, scoreRectObj)

while True:


    for event in pygame.event.get():
        Background.fill(BGcolor)
        Background.blit(textSurfaceObj, textRectObj)
        Background.blit(Kanskaart, (450, 300))
        scoretext = myfont.render("Score {0}".format(score), 1, (0, 0, 0))
        Background.blit(scoretext, (5, 10))
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            if 450 <= mousex and 625.5 >= mousex and 212.5 <= mousey and 475 >= mousey:
                Background.blit(flip, (50, 300))
                if Background.blit(flip, (50,300)):
                    score += 200
            elif 150 <= mousex and 325 >= mousex and 212.5 <= mousey and 475 >= mousey:
                pygame.quit()
                quit()

        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()