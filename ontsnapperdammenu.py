import pygame
from pygame.locals import *
import sys
import time
import random
import PythonApplication19
from PythonApplication19 import *
import PythonApplication25
import Terminate_screen
import howtoplay
import setting



pygame.init()
width = 800
height = 850
img = pygame.image.load('img/play.png')
img3 = pygame.image.load('img/exit.png')
img5 = pygame.image.load('img/howtoplay.png')
img7 = pygame.image.load('img/highscores.png')
bg = pygame.image.load('img/speelbord.png')
ologo = pygame.image.load('img/ontsnapperdamlogo.png')
settingimg = pygame.image.load('img/settings.png')
img2 = pygame.transform.smoothscale(img,(200,70))
img4 = pygame.transform.smoothscale(img3,(200,70))
img6 = pygame.transform.smoothscale(img5,(200,70))
img8 = pygame.transform.smoothscale(img7,(200,70))
bg1 = pygame.transform.smoothscale(bg,(width,height))
ologo1 = pygame.transform.smoothscale(ologo,(800,230))
settings1 = pygame.transform.smoothscale(settingimg,(100,35))
screen = pygame.display.set_mode((width,height))


 #Main Loop
# p1 = PythonApplication19.Player("F",(0,0,0),330,20)
# p_list = [p1]


#Terminate screen


black = (0,0,0)
red = (255,0,0)
white = (255,255,255)



pygame.display.set_caption('Ontsnapperdam')
screen.fill(white)


defaultfont = pygame.font.get_default_font()
fontrenderer = pygame.font.Font(defaultfont,85)

label = fontrenderer.render("Ontsnapperdam",1,red)
highscores = PythonApplication25.hsscreen()

class start:
	def __init__(self):
		self.running = True
		self.waarheid = False




	def intro(self):

		while self.running:
			screen.blit(bg1,(0,0))
			screen.blit(img2,(width*0.35,height*0.35))
			screen.blit(img4,(width*0.35,height*0.45))
			screen.blit(ologo1,(15,70))
			screen.blit(settings1,(width-100,15))
			screen.blit(img8,(width*0.35,height*0.55))
			screen.blit(img6,(width*0.35,height*0.65))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					#Game(players)
				if event.type == pygame.MOUSEBUTTONDOWN:
					mousex, mousey = pygame.mouse.get_pos()
					if  width*0.35 <= mousex and  width*0.60 >= mousex and height*0.35 <=mousey and height*0.433 >= mousey:
						print(len(PythonApplication19.players))
						game = PythonApplication19.Game(players)
						game.Gameloop()

					elif width*0.35 <= mousex and width*0.60 >= mousex and height*0.45 <= mousey and height*0.533 >= mousey:
						termination.Gameloop()
                        #pygame.quit()
                        #quit()
					elif width-100 <= mousex and width >= mousex and 15 <= mousey and 50 >= mousey:
						sett.loop()
					elif width * 0.35 <= mousex and width * 0.60 >= mousex and height * 0.55 <= mousey and height * 0.633 >= mousey:
						highscores.introo()
					elif width * 0.35 <= mousex and width * 0.60 >= mousex and height * 0.65 <= mousey and height * 0.733 >= mousey:
						how.loop()



			pygame.display.flip()


menu = start()

termination = Terminate_screen.Termination()
how = howtoplay.mainloop()
sett = setting.Settings()
menu.intro()







