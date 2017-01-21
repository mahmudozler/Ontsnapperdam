import pygame
import random

pygame.init()

done = False

class Player:
	def __init__(self,name,kleur,x,y):
		self.name = name
		self.kleur = kleur
		self.x = x
		self.y = y
		self.r = 10.5
		self.counter = 0

	def draw(self,screen):
		pygame.draw.circle(screen,self.kleur,(int(self.x),int(self.y)),int(self.r))

	def Update(self,screen,event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				#screen.fill((250, 250, 250))
				self.x -= 26
				self.draw(screen)
			elif event.key == pygame.K_RIGHT:
				#screen.fill((250, 250, 250))
				self.x += 26
				self.draw(screen)
			elif event.key == pygame.K_UP:
				#screen.fill((250, 250, 250))
				self.y -= 26
				self.draw(screen)
			elif event.key == pygame.K_DOWN:
				screen.fill((250, 250, 250))
				self.y += 26
				self.draw(screen)


	def Pos(self):
		#pos = str(self.x) + " - " + str(self.y)
		#return pos
		return self.x,self.y

class Game:
	def __init__(self,players):
		pygame.init()
		self.turn = 0
		self.steps = 0
		self.players = players
		self.thrown = 0
		self.size = (800,850)
		self.running = False

		#block width,height,margin
		self.w = 25
		self.h = 25
		self.m = 1

		#self.screen = pygame.display.set_mode(self.size)

	def Update(self,event):
		player = self.players[self.turn]
		if event.type == pygame.KEYDOWN:
			#Add arrow key constraints
			self.steps += 1
			player.Update(self.screen,event)

			#if all steps made
			if self.steps == self.thrown:
				self.thrown = 0
				print(player.Pos())
				#pygame.Rect.collidepoint(100,100)
				if self.turn == (len(self.players) - 1):
					self.turn = 0
				else:
					self.turn += 1
				self.steps = 0

	def Filter(self,x,y):
		map_list = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],[0,9,19],[0,9,10,19],[0,10,19],[0,10,19],
					[0,1,2,4,5,6,7,8,9,10,11,12,13,19],[0,2,4,8,13,17,18,19],[0,2,3,4,8,13,17,19],[0,4,8,11,12,13,14,15,16,17,19],[0,4,8,11,19],
					[0,4,5,6,7,8,11,13,14,15,16,17,18,19],[0,6,11,12,13,16,19],[0,6,13,14,15,16,19],[0,3,4,5,6,13,16,19],[0,3,6,7,8,9,10,11,12,13,16,17,18,19],
					[0,1,2,3,6,13,16,19],[0,3,6,13,16,19],[0,3,6,7,8,9,13,14,15,16,19],[0,2,3,4,5,6,9,13,19],[0,2,9,13,19],[0,2,9,10,11,12,13,19],[0,2,3,4,5,6,13,19],[0,6,13,14,15,19],
					[0,6,15,19],[0,6,7,8,9,10,11,12,13,14,15,19],[0,1,2,3,4,5,6,8,15,19],[3,8,13,14,15,19],[3,8,13,19],[3,8,13,19],[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]]
		if x in map_list[y]:
			return True
		return False

	def Draw(self):

		#draw canvas
		self.screen = pygame.display.set_mode(self.size)
		self.screen.fill((255, 255, 255))

		#draw dice
		pygame.draw.rect(self.screen, (0, 0, 0), (10, 10, 50, 50), 1)

		#draw all player
		for player in self.players:
			player.draw(self.screen)

		#draw game board
		for row in range(30):
			for col in range(20):
				if self.Filter(col, row):
					color = (0, 0, 0)
					pygame.draw.rect(self.screen, color, ((self.w + self.m) * col + (self.m + 40), ((self.h + self.m) * row + self.m) + 50, self.w, self.h),1)

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
						self.thrown = random.randint(1, 6)
						print(self.thrown)

				# execute if dice is thrown
				if event.type == pygame.KEYDOWN:
					if self.thrown > 0:
						self.Update(event)
			self.Draw()



player1 = Player("A",(155,255,140),210,38)
player2 = Player("B",(155,255,140),236,38)
player3 = Player("C",(91,183,211),262,38)
player4 = Player("D",(116,59,124),288,38)
player5 = Player("E",(237,65,56),314,38)
player6 = Player("F",(0,0,0),340,38)

players = [player1,player2,player3,player4]

game = Game(players)
game.Gameloop()


	

		