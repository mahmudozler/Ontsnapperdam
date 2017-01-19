import pygame
from pygame.locals import *
import sys
import time


pygame.init()
width = 800
height = 600
img = pygame.image.load('start knop.png')
img3 = pygame.image.load('exit knop.png')
img2 = pygame.transform.smoothscale(img,(200, 70))
img4 = pygame.transform.smoothscale(img3,(200,70))
screen = pygame.display.set_mode((width,height))



black = (0,0,0)
red = (255,0,0)
white = (255,255,255)



pygame.display.set_caption('Ontsnapperdam')
screen.fill(white)

defaultfont = pygame.font.get_default_font()
fontrenderer = pygame.font.Font(defaultfont,85)

label = fontrenderer.render("Ontsnapperdam",1,red)

screen.blit(label,(40,15))



def mainloop():
    running = True
    while running:
        screen.blit(img2,(300,250))
        screen.blit(img4,(300,350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if 300 <= mousex and 500 >= mousex and 250 <= mousey and 320 >= mousey:
                    print("skip")
                elif 300 <= mousex and 500 >= mousex and 350 <= mousey and 420 >= mousey:
                    running = False


        pygame.display.flip()

print(mainloop())


