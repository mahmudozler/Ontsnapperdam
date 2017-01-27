import pygame, sys
from pygame.locals import *

pygame.init()

#maak het scherm aan
Background = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption('Terminating game')

#maak de kleur aan
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

#background colour
Background.fill(WHITE)

#loading the images
Yes = pygame.image.load('img/Yes.png')
No = pygame.image.load('img/No.png')
YesButton = pygame.transform.smoothscale(Yes, (175, 175))
NoButton = pygame.transform.smoothscale(No, (175, 175))


#loading the font
fontObj = pygame.font.Font('freesansbold.ttf', 64)
textSurfaceObj = fontObj.render('Do you want to quit?', True, BLACK, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (400,100)


RandomText = pygame.font.Font('freesansbold.ttf', 32)
RandomSurfaceObj = RandomText.render('click the goddamn yes button!!!!!', True, BLACK, WHITE)
RandomRectObj = RandomSurfaceObj.get_rect()
RandomRectObj.center = (400,200)


#main game loop
while True:

    Background.blit(textSurfaceObj, textRectObj)
    Background.blit(YesButton,(150, 300))
    Background.blit(NoButton,(450, 300))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            if 450 <= mousex and 625.5 >= mousex and 212.5 <= mousey and 475 >= mousey:
                Background.blit(RandomSurfaceObj, RandomRectObj)
            elif 150 <= mousex and 325  >= mousex and 212.5 <= mousey and 475 >= mousey:
                pygame.quit()
                quit()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


