import pygame
import time
import random

pygame.init()

dwidth = 600
dheight = 800

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

bcolor = (53,115,255)

cwidth = 73

gameDisplay = pygame.display.set_mode((dwidth,dheight))
pygame.display.set_caption('Ontsnapperdam')
clock = pygame.time.Clock()

diceImg = pygame.image.load('dobbelstenen.jpg')

def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged: "+str(count),True,black)
    gameDisplay.blit(text,(0,0))

def things(thinga,thingb,thingc,thingd,color):
    pygame.draw.rect(gameDisplay , color , [thinga,thingb,thingc,thingd])

def car(x,y):
    gameDisplay.blit(diceImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface , textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('Ontsnapperdam',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((dwidth/2),(dheight/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('you lost')

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('Ontsnapperdam',115)
        TextSurf,TextRect = text_objects("Ontsnapperdam",largeText)
        TextRect.center = ((dwidth/2),(dheight/2))
        gameDisplay.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(15)

def game_loop():
    x = (dwidth * 0.45)
    y = (dheight * 0.8)

    x_change = 0

    thing_starta = random.randrange(0,dwidth)
    thing_startb = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        things(thing_starta,thing_startb,thing_width,thing_height,bcolor)

        game_intro()
        game_loop()
        pygame.quit()
        quit()


