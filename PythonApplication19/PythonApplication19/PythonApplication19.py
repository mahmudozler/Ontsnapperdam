import pygame
from pygame.locals import *
import random
pygame.font.init()

pygame.init()

done = False

class Player:
	def __init__(self,name,kleur,x,y):
		self.name = name
		self.kleur = kleur
		self.x = x
		self.y = y
		self.r = 10
		self.rect = pygame.Rect(self.x, self.y, 20, 20)
		self.steps = 0
		self.startblock = pygame.Rect(249, 51, 103, 25)
		self.state = "start"

	def draw(self,screen):
		pygame.draw.circle(screen,self.kleur,(self.rect.center),self.r)

	def Update(self,screen,event,blocks,battleblocks):
		if event.type == pygame.KEYDOWN:
			# to check the new position is within the game blocks
			newpos = self.rect.copy()

			# If player on start block these sizes these steps else normal size steps
			if newpos.colliderect(self.startblock):
				#print("STARTBLOCK")
				self.state = "-"
				if event.key == pygame.K_LEFT:
					newpos.x -= 52
				elif event.key == pygame.K_RIGHT:
					newpos.x += 78
				elif event.key == pygame.K_DOWN:
					newpos.y += 26
			else:
				if event.key == pygame.K_LEFT:
					newpos.x -= 26
				elif event.key == pygame.K_RIGHT:
					newpos.x += 26
				elif event.key == pygame.K_UP:
					newpos.y -= 26
				elif event.key == pygame.K_DOWN:
					newpos.y += 26

			# bool check is newpos is inside game rectangles
			for rectangle in blocks:
				if newpos.colliderect(rectangle):
					print(newpos)
					# convert newpos in the new position
					self.steps += 1
					self.rect = newpos
					for rectangle in battleblocks:
						if newpos.colliderect(rectangle):
							print("LETS BATTLE!")
							break # stop check when battle block match
					# stop check when matched
					break

	def Pos(self):
		return self.x,self.y

class Game:
	def __init__(self,players):
		pygame.init()
		self.turn = 0
		self.players = players
		self.thrown = 0
		self.size = (800,850)
		self.running = False

		#game pic location
		self.img = pygame.image.load('img/soldier.png')
		self.img = pygame.transform.smoothscale(self.img,(30,20 ))

		self.img2 = pygame.image.load('img/hilton.png')
		self.img2 = pygame.transform.smoothscale(self.img2,(35,32 ))

		self.img3 = pygame.image.load('img/dedoelen.png')
		self.img3 = pygame.transform.smoothscale(self.img3,(60,60 ))

		self.img4 = pygame.image.load('img/police.png')
		self.img4 = pygame.transform.smoothscale(self.img4,(27,27 ))

		self.img5 = pygame.image.load('img/fusrodah.png')
		self.img5 = pygame.transform.smoothscale(self.img5,(23,23 ))

		self.img6 = pygame.image.load('img/bike.png')
		self.img6 = pygame.transform.smoothscale(self.img6,(24,24 ))

		self.img7 = pygame.image.load('img/luxor.png')
		self.img7 = pygame.transform.smoothscale(self.img7,(45,40 ))

		self.img8 = pygame.image.load('img/kfc.png')
		self.img8 = pygame.transform.smoothscale(self.img8,(30,30 ))

		self.img9 = pygame.image.load('img/bijenkorf.png')
		self.img9 = pygame.transform.smoothscale(self.img9,(80,80 ))

		self.img10 = pygame.image.load('img/abn.png')
		self.img10 = pygame.transform.smoothscale(self.img10,(70,85 ))

		self.img11 = pygame.image.load('img/house.png')
		self.img11 = pygame.transform.smoothscale(self.img11,(40,40 ))

		self.img12 = pygame.image.load('img/weed.png')
		self.img12 = pygame.transform.smoothscale(self.img12,(30,30 ))

		self.img13 = pygame.image.load('img/camuflage.png')
		self.img13 = pygame.transform.smoothscale(self.img13,(20,20 ))

		self.img14 = pygame.image.load('img/kabouter.png')
		self.img14 = pygame.transform.smoothscale(self.img14,(55,55 ))

		self.img15 = pygame.image.load('img/ufo.png')
		self.img15 = pygame.transform.smoothscale(self.img15,(25,25 ))
			 
		self.img16 = pygame.image.load('img/wok.png')
		self.img16 = pygame.transform.smoothscale(self.img16,(40,20 ))

		self.img17 = pygame.image.load('img/hro.png')
		self.img17 = pygame.transform.smoothscale(self.img17,(30,30 ))

		self.img18 = pygame.image.load('img/taxi.png')
		self.img18 = pygame.transform.smoothscale(self.img18,(23,23 ))

		self.img19 = pygame.image.load('img/erasmus.png')
		self.img19 = pygame.transform.smoothscale(self.img19,(80,50 ))

		self.img20 = pygame.image.load('img/tree.png')
		self.img20 = pygame.transform.smoothscale(self.img20,(30,30 ))

		self.img21 = pygame.image.load('img/inntel.png')
		self.img21 = pygame.transform.smoothscale(self.img21,(30,30 ))

		self.img22 = pygame.image.load('img/kunsthal.png')
		self.img22 = pygame.transform.smoothscale(self.img22,(30,50 ))

		self.img23 = pygame.image.load('img/euromast.png')
		self.img23 = pygame.transform.smoothscale(self.img23,(80,65 ))

		self.img24 = pygame.image.load('img/time.png')
		self.img24= pygame.transform.smoothscale(self.img24,(20,20 ))

		self.img25 = pygame.image.load('img/oriental.png')
		self.img25= pygame.transform.smoothscale(self.img25,(55,25 ))

		self.img26 = pygame.image.load('img/pijl.png')
		self.img26= pygame.transform.smoothscale(self.img26,(30,30 ))

		self.img27 = pygame.image.load('img/boat.png')
		self.img27= pygame.transform.smoothscale(self.img27,(110,110 ))

		self.img28 = pygame.image.load('img/fist.png')
		self.img28= pygame.transform.smoothscale(self.img28,(20,20 ))

		#text map
		self.font = pygame.font.SysFont(None,16)
		self.text=self.font.render("Rotterdam Centraal",True,(0,0,0))
		
		self.font = pygame.font.SysFont(None,30)
		self.text1=self.font.render("L",True,(0,0,0))

		self.font = pygame.font.SysFont(None,15)
		self.text2=self.font.render("Coffeeshop Amigo",True,(0,0,0))

		self.font = pygame.font.SysFont(None,15)
		self.text3=self.font.render("Huize Jansen",True,(0,0,0))
		
		self.font = pygame.font.SysFont(None,15)
		self.text4=self.font.render("Kabouter Buttplug",True,(0,0,0))

		self.font = pygame.font.SysFont(None,15)
		self.text5=self.font.render("Museumpark",True,(0,0,0))

		self.font = pygame.font.SysFont(None,15)
		self.text6=self.font.render("Euromast",True,(0,0,0))

		#!?
		self.font = pygame.font.SysFont(None,33)
		self.text7=self.font.render("!?",True,(244,152,66))


		#block width,height,margin
		self.w = 25
		self.h = 25
		self.m = 1

		#font
<<<<<<< HEAD
		#myfont = self.screen.font.SysFont("Comic Sans MS", 30)
=======
		self.font = pygame.font.SysFont("comicsansms", 57)
		#self.dice_text = self.font.render("Thrown: %s".format(self.thrown), True, (255, 9, 12))
		#self.dice_text = self.font.render("6", True, (0, 128, 0))

>>>>>>> 46b13b687f7bbfea9f6855fe4f708b212330ed25

		#colors
		self.red = (191,36,36)
		self.black = (23,20,20)

		#self.screen = pygame.display.set_mode(self.size)
		self.blocks = []
		self.battleblocks = []

		self.map_list = [[0,1,2,3,4,5,6,7,8,12,13,14,15,16,17,18,19],[0,9,19],[0,9,10,19],[0,10,19],[0,10,19],
					[0,1,2,4,5,6,7,8,9,10,11,12,13,19],[0,2,4,8,13,17,18,19],[0,2,3,4,8,13,17,19],[0,4,8,11,12,13,14,15,16,17,19],[0,4,8,11,19],
					[0,4,5,6,7,8,11,13,14,15,16,17,18,19],[0,6,11,12,13,16,19],[0,6,13,14,15,16,19],[0,3,4,5,6,13,16,19],[0,3,6,7,8,9,10,11,12,13,16,17,18,19],
					[0,1,2,3,6,13,16,19],[0,3,6,13,16,19],[0,3,6,7,8,9,13,14,15,16,19],[0,2,3,4,5,6,9,13,19],[0,2,9,13,19],[0,2,9,10,11,12,13,19],[0,2,3,4,5,6,13,19],[0,6,13,14,15,19],
					[0,6,15,19],[0,6,7,8,9,10,11,12,13,14,15,19],[0,1,2,3,4,5,6,8,15,19],[3,8,13,14,15,19],[3,8,13,19],[3,8,13,19],[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]]
		self.battle_map_list= [[],[],[],[0],[0],[0,1],[0],[13,17],[8,13,14,15,16,17],[8],[7,8],[],[13,14],[3,4,5,6,13],
			[3,6,13],[13],[13],[13,14],[],[],[],[],[],[],[],[3,4,5,6],[3,13],[13],[13],[11,12,13]]

		# Create list with all block position in the game
		for row in range(30):
			for col in range(30):
				if self.Filter(col, row,self.battle_map_list):
					self.battleblocks.append(
						pygame.Rect((self.w + self.m) * col + self.m + 40, ((self.h + self.m) * row + self.m + 50),
									self.w, self.h))
				elif self.Filter(col, row,self.map_list):
					self.blocks.append(
						pygame.Rect((self.w + self.m) * col + self.m + 40, ((self.h + self.m) * row + self.m + 50),
									self.w, self.h))

		# special blocks
		self.startblock = self.blocks[8]
		self.startblock.w = 103



	def Update(self, event):
		player = self.players[self.turn]
		if event.type == pygame.KEYDOWN:
			player.Update(self.screen, event, (self.blocks + self.battleblocks), self.battleblocks)

			# if all steps made
			if player.steps == self.thrown:
				self.thrown = 0
				if self.turn == (len(self.players) - 1):
					self.turn = 0
				else:
					self.turn += 1
				player.steps = 0

	def Filter(self, x, y,list):
		if x in list[y]:
			return True
		return False

	def Draw(self):

		#draw canvas
		self.screen = pygame.display.set_mode(self.size,RESIZABLE)
		self.screen.fill((255, 255, 255))

		if self.thrown > 0:
			#self.dice_text = self.thrown
			self.dice_text = self.font.render("{0}".format(self.thrown), True, (255, 9, 12))
			self.screen.blit(self.dice_text, (20, 20))

		#set all images
		self.screen.blit(self.img,(510,420))
		self.screen.blit(self.img2,(500,100))
		self.screen.blit(self.img3,(77,130))
		self.screen.blit(self.img4,(378,179))
		self.screen.blit(self.img4,(144,257))
		self.screen.blit(self.img4,(534,413))
		self.screen.blit(self.img5,(42,235))
		self.screen.blit(self.img6,(250,258))
		self.screen.blit(self.img7,(435,195))
		self.screen.blit(self.img8,(170,282))
		self.screen.blit(self.img9,(353,260))
		self.screen.blit(self.img10,(473,330))
		self.screen.blit(self.img11,(235,374))
		self.screen.blit(self.img12,(65,360))
		self.screen.blit(self.img13,(70,445))
		self.screen.blit(self.img14,(240,438))
		self.screen.blit(self.img4,(274,491))
		self.screen.blit(self.img15,(379,440))
		self.screen.blit(self.img16,(415,470))
		self.screen.blit(self.img17,(505,542))
		self.screen.blit(self.img18,(276,571))
		self.screen.blit(self.img8,(130,570))
		self.screen.blit(self.img19,(70,650))
		self.screen.blit(self.img20,(296,645))
		self.screen.blit(self.img20,(324,645))
		self.screen.blit(self.img20,(352,645))
		self.screen.blit(self.img21,(458,647))
		self.screen.blit(self.img4,(92,518))
		self.screen.blit(self.img22,(458,750))
		self.screen.blit(self.img4,(430,725))
		self.screen.blit(self.img23,(250,740))
		self.screen.blit(self.img24,(200,703))
		self.screen.blit(self.img25,(145,755))
		self.screen.blit(self.img26,(118,778))
		self.screen.blit(self.img27,(10,720))
		self.screen.blit(self.img28,(329,808))
		#text map
		self.screen.blit(self.text,(250,57))
		self.screen.blit(self.text2,(67,350))
		self.screen.blit(self.text3,(240,365))
		self.screen.blit(self.text4,(240,440))
		self.screen.blit(self.text5,(308,630))
		self.screen.blit(self.text6,(300,760))
		#L
		self.screen.blit(self.text1,(542,107))
		self.screen.blit(self.text1,(542,550))
		self.screen.blit(self.text1,(490,212))
		self.screen.blit(self.text1,(463,367))
		self.screen.blit(self.text1,(437,497))
		self.screen.blit(self.text1,(437,653))
		self.screen.blit(self.text1,(463,810))
		self.screen.blit(self.text1,(100,185))
		self.screen.blit(self.text1,(177,315))
		self.screen.blit(self.text1,(47,367))
		self.screen.blit(self.text1,(333,289))
		self.screen.blit(self.text1,(255,419))
		self.screen.blit(self.text1,(255,498))
		self.screen.blit(self.text1,(333,679))
		self.screen.blit(self.text1,(255,757))
		self.screen.blit(self.text1,(125,757))
		self.screen.blit(self.text1,(150,600))
		self.screen.blit(self.text1,(48,705))
		#!?
		self.screen.blit(self.text7,(121,54))
		self.screen.blit(self.text7,(408,54))
		self.screen.blit(self.text7,(305,105))
		self.screen.blit(self.text7,(356,184))
		self.screen.blit(self.text7,(200,184))
		self.screen.blit(self.text7,(200,313))
		self.screen.blit(self.text7,(200,470))
		self.screen.blit(self.text7,(200,600))
		self.screen.blit(self.text7,(44,184))
		self.screen.blit(self.text7,(95,235))
		self.screen.blit(self.text7,(122,391))
		self.screen.blit(self.text7,(122,704))
		self.screen.blit(self.text7,(122,808))
		self.screen.blit(self.text7,(44,522))
		self.screen.blit(self.text7,(382,262))
		self.screen.blit(self.text7,(382,495))
		self.screen.blit(self.text7,(382,600))
		self.screen.blit(self.text7,(382,677))
		self.screen.blit(self.text7,(485,262))
		self.screen.blit(self.text7,(538,313))
		self.screen.blit(self.text7,(538,392))
		self.screen.blit(self.text7,(538,678))
		self.screen.blit(self.text7,(252,678))
		self.screen.blit(self.text7,(434,313))
		self.screen.blit(self.text7,(330,340))
		self.screen.blit(self.text7,(460,443))
		self.screen.blit(self.text7,(305,808))
		self.screen.blit(self.text7,(512,808))


		#draw dice button
		pygame.draw.rect(self.screen, (0, 0, 0), (10, 10, 50, 50), 1)

		#draw all player
		for player in self.players:
			player.draw(self.screen)

		#draw game board
		for rectangle in self.blocks:
			pygame.draw.rect(self.screen, self.black, rectangle, 1)

		for rectangle in self.battleblocks:
			pygame.draw.rect(self.screen, self.red, rectangle, 1)

		#update whole screen
		pygame.display.flip()

	def Gameloop(self):

		self.Draw()

		while not self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = True

				# If click on dice
				if event.type == pygame.MOUSEBUTTONDOWN:
					mousex, mousey = pygame.mouse.get_pos()
					if mousex > 10 and mousex < 60 and mousey > 10 and mousey < 60:
						if self.thrown == 0:
							self.thrown = random.randint(1, 6)
							#self.dice_text = self.font.render(self.thrown, True, (0, 128, 0))
							#self.screen.blit(self.dice_text, (20, 20))
							if self.players[self.turn].state == "start":
								self.players[self.turn].rect.x = 278
								self.players[self.turn].rect.y = 54

							self.Draw()
						print(self.thrown)

				# execute if dice is thrown
				if event.type == pygame.KEYDOWN:
					if self.thrown > 0:
						self.Update(event)

						self.Draw()
			# ...
			#pygame.display.flip()


player1 = Player("A",(155,255,140),200,28)
player2 = Player("B",(155,255,140),226,28)
player3 = Player("C",(91,183,211),252,28)
player4 = Player("D",(116,59,124),278,28)
player5 = Player("E",(237,65,56),304,28)
player6 = Player("F",(0,0,0),330,28)

players = [player1,player2,player3]

game = Game(players)
for x in game.blocks:
	print(x)

game.Gameloop()



	

		