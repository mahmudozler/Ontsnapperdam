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
		self.r = 10
		self.rect = pygame.Rect(self.x, self.y, 20, 20)
		self.steps = 0

	def draw(self,screen):
		pygame.draw.circle(screen,self.kleur,(self.rect.center),self.r)

	def Update(self,screen,event,blocks,battleblocks):
		if event.type == pygame.KEYDOWN:
			# to check the new position is within the game blocks
			newpos = self.rect.copy()

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

		#block width,height,margin
		self.w = 25
		self.h = 25
		self.m = 1

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

		self.blocks[8].w = 103

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
		self.screen = pygame.display.set_mode(self.size)
		self.screen.fill((255, 255, 255))

		#draw dice
		pygame.draw.rect(self.screen, (0, 0, 0), (10, 10, 50, 50), 1)

		#draw all player
		for player in self.players:
			player.draw(self.screen)

		#draw game board
		for rectangle in self.blocks:
			"""if rectangle.x == 249 and rectangle.y == 51:
				#this.w = 9"""
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
						print(self.thrown)

				# execute if dice is thrown
				if event.type == pygame.KEYDOWN:
					if self.thrown > 0:
						self.Update(event)

						self.Draw()
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



	

		