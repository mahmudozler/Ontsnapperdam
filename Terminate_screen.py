import pygame, sys
from pygame.locals import *


pygame.init()

class Termination:
    def __init__(self):
        pygame.init()
        self.size = (800,850)


        #maak de kleur aan
        BLACK = (0,0,0)
        GREEN = (0,255,0)
        BLUE = (0,0,255)
        WHITE = (255,255,255)

        #loading the images
        self.Yes = pygame.image.load('img/Yes.png')
        self.No = pygame.image.load('img/No.png')
        self.YesButton = pygame.transform.smoothscale(self.Yes, (175, 175))
        self.NoButton = pygame.transform.smoothscale(self.No, (175, 175))


        #loading the font
        self.fontObj = pygame.font.Font('freesansbold.ttf', 64)
        self.textSurfaceObj = self.fontObj.render('Do you want to quit?', True, BLACK, WHITE)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (400,100)


        self.RandomText = pygame.font.Font('freesansbold.ttf', 32)
        self.RandomSurfaceObj = self.RandomText.render('click the goddamn yes button!!!!!', True, BLACK, WHITE)
        self.RandomRectObj = self.RandomSurfaceObj.get_rect()
        self.RandomRectObj.center = (400,200)

    def draw(self):
        self.Background = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Terminating game')

        self.Background.fill((255,255,255))

        #putting images on the background
        self.Background.blit(self.textSurfaceObj, self.textRectObj)
        self.Background.blit(self.YesButton, (150, 300))
        self.Background.blit(self.NoButton, (450, 300))

        #flipping the image
        pygame.display.flip()

        #main game loop
    def Gameloop(self):
        self.running = True
        self.draw()

        while self.running:



            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = pygame.mouse.get_pos()
                    if 450 <= mousex and 625.5 >= mousex and 212.5 <= mousey and 475 >= mousey:
                        self.running = False
                    elif 150 <= mousex and 325  >= mousex and 212.5 <= mousey and 475 >= mousey:
                        pygame.quit()
                        quit()


                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
