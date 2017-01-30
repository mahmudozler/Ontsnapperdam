import random, time, pygame, sys
from pygame.locals import *


pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('How to play:')

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
YELL  = (249, 225,   7)

rulesImg = pygame.image.load('img/rules.png')
backImg = pygame.image.load('img/back4.png')

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('How to play:', True, BLACK)

textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (400, 15)



class mainloop:

	def loop(self):
		running = True
		while running:
			DISPLAYSURF.fill(WHITE)
			DISPLAYSURF.blit(rulesImg, (75, 100))
			DISPLAYSURF.blit(textSurfaceObj, textRectObj)
			DISPLAYSURF.blit(backImg, (0,0))
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					mousex, mousey = pygame.mouse.get_pos()
					if mousex <= 50 and mousey <= 50:
						running = False
			pygame.display.flip()
#how = howtoplay()
#how.loop()