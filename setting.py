import random, time, pygame, sys
from pygame.locals import *

pygame.init()

width = 800
height = 850
achtergrond = pygame.image.load('img/speelbord.png')
achtergrond1 = pygame.transform.smoothscale(achtergrond,(width,height))
img = pygame.image.load('img/aan.png')
img1 = pygame.transform.smoothscale(img,(200 , 200))
img2 = pygame.image.load('img/uit.png')
img3 = pygame.transform.smoothscale(img2,(200 , 200))
backImg = pygame.image.load('img/back4.png')
screen = pygame.display.set_mode((width,height))
defaultfont = pygame.font.get_default_font()
fontrenderer = pygame.font.Font(defaultfont,85)
screen.fill((255,255,255))
label = fontrenderer.render("Settings",1,(0,0,0))


class Settings:

    def __init__(self):
        self.running = True


    def loop(self):

        while self.running:
            screen.blit(achtergrond1, (0, 0))
            screen.blit(label, (225, 75))
            screen.blit(img1, (width*0.35, height*0.30))
            screen.blit(img3, (width * 0.35, height * 0.55))
            screen.blit(backImg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = pygame.mouse.get_pos()
                    if width * 0.35 <= mousex and width * 0.60 >= mousex and height * 0.30 <= mousey and height * 0.5 >= mousey:
                        print("geluid aan")
                    elif width * 0.35 <= mousex and width * 0.60 >= mousex and height * 0.55 <= mousey and height * 0.75 >= mousey:
                        print("geluid uit")
                    elif width * 0.00 <= mousex and width * 0.10 >= mousex and height *0 <= mousey and height * 0.10 >= mousey:
                        self.running = False




            pygame.display.flip()


