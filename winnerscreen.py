import random, time, pygame, sys
from pygame.locals import *

pygame.init()

width = 800
height = 850

achtergrond = pygame.image.load('img/speelbord.png')
achtergrond1 = pygame.transform.smoothscale(achtergrond,(width,height))
img = pygame.image.load('img/ok.png')
img2 = pygame.transform.smoothscale(img,(200,70))
screen = pygame.display.set_mode((width,height))
defaultfont = pygame.font.get_default_font()
fontrenderer = pygame.font.Font(defaultfont,100)
fontrenderer1 = pygame.font.Font(defaultfont,50)
label = fontrenderer.render("Winner!!!",1,(0,0,0))
screen.fill((255,255,255))

class Winner:

    def __init__(self):
        self.running = True


    def winaar(self,winnaar):
        label1 = fontrenderer1.render("Player " + str(winnaar) + " won the game", 1, (0, 0, 0))

        while self.running:
            screen.blit(achtergrond1,(0,0))
            screen.blit(label,(166,75))
            screen.blit(label1,(60,300))
            screen.blit(img2,(width*0.35,height*0.55))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = pygame.mouse.get_pos()
                    if width * 0.35 <= mousex and width * 0.60 >= mousex and height * 0.55 <= mousey and height * 0.75 >= mousey:
                        self.running = False
                    elif width * 0.00 <= mousex and width * 0.10 >= mousex and height *0 <= mousey and height * 0.10 >= mousey:
                        pygame.quit()
                        quit()

            pygame.display.flip()

