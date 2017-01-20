import pygame
import random

pygame.init()

size =(600,850)
screen = pygame.display.set_mode(size)
screen.fill((250,250,250))

w = 25
h = 25
m = 1

done = False

class Player:
	def __init__(self,name,kleur,x,y,r):
		self.name = name
		self.kleur = kleur
		self.x = x
		self.y = y
		self.r = r
		self.counter = 0

	def draw(self,screen):
		pygame.draw.circle(screen,self.kleur,(int(self.x),int(self.y)),int(self.r))

	def Update(self):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				screen.fill((250, 250, 250))
				self.x -= 26
				self.draw(screen)
			elif event.key == pygame.K_RIGHT:
				screen.fill((250, 250, 250))
				self.x += 26
				self.draw(screen)
			elif event.key == pygame.K_UP:
				screen.fill((250, 250, 250))
				self.y -= 26
				self.draw(screen)
			elif event.key == pygame.K_DOWN:
				screen.fill((250, 250, 250))
				self.y += 26
				self.draw(screen)

	def Pos(self):
		pos = str(self.x) + " - " + str(self.y)
		return pos

class Game:
	def __init__(self,players):
		self.turn = 0
		self.steps = 0
		self.players = players
		self.thrown = 0

	def Update(self,event):
		player = self.players[self.turn]
		if event.type == pygame.KEYDOWN:
			#Add arrow key constraints
			self.steps += 1
			player.Update()

			#if all steps made
			if self.steps == self.thrown:
				self.thrown = 0
				#print("next dice")
				print(player.Pos())
				if self.turn == 5:
					self.turn = 0
				else:
					self.turn += 1
				self.steps = 0

player1 = Player("A",(155,255,140),210,38,10.5)
player2 = Player("B",(155,255,140),236,38,10.5)
player3 = Player("C",(91,183,211),262,38,10.5)
player4 = Player("D",(116,59,124),288,38,10.5)
player5 = Player("E",(237,65,56),314,38,10.5)
player6 = Player("F",(0,0,0),340,38,10.5)

players = [player1,player2,player3,player4,player5,player6]
game = Game(players)
dice = 0

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		#click on dice to start
		if event.type == pygame.MOUSEBUTTONDOWN:
			mousex, mousey = pygame.mouse.get_pos()
			if mousex > 10 and mousex < 60 and mousey > 10 and mousey <60:
				game.thrown = random.randint(1,6)
				print(game.thrown)

		#execute if dice is thrown
		if event.type == pygame.KEYDOWN:
			if game.thrown > 0:
				game.Update(event)

	#player draw initial position
	player1.draw(screen)
	player2.draw(screen)
	player3.draw(screen)
	player4.draw(screen)
	player5.draw(screen)
	player6.draw(screen)

	# dice
	pygame.draw.rect(screen, (0, 0, 0), (10, 10, 50, 50), 1)

	#grid
	for row in range(30):
		for col in range(20):
			color = (0, 0, 0)
			if row == 0 or (row == 29 and col > 2) or (col == 0 and row < 26) or col == 19 or (col == 10 and row == 1) or (col == 10 and row == 2) or (col == 11 and row > 1 and row < 5) \
			or (col == 11 and row == 3) or (col == 11 and row == 5) or (row == 5 and col > 3 and col < 14) or (row == 5 and col < 3)\
			or (col == 2 and row > 5 and row < 8) or (row > 5 and row < 11 and col == 4) or (row > 5 and row < 11 and col == 8) or (col == 3 and row == 7)\
			or (row > 4 and row < 9 and col == 14) or (col > 11 and col < 18 and row == 8) or (row > 5 and row < 9 and col == 17)\
			or (row == 6 and col == 18) or (row > 7 and row < 12 and col == 11) or (row == 10 and col > 12) or (row > 9 and row < 23 and col == 13)\
			or (row > 9 and row < 18 and col == 16) or (row > 9 and row < 19 and col == 6) or (col > 3 and col < 9 and row == 10) or (row == 13 and col > 2 and col < 7)\
			or (row > 12 and row < 19 and col == 3) or (row == 18 and col > 1 and col < 7) or (col > 5 and col < 14 and row == 14) or (row > 17 and row < 22 and col == 2)\
			or (row == 21 and col > 1 and col < 7) or (row == 25 and col < 7) or (col == 6 and row > 20 and row < 26) or (row == 24 and col > 5 and col < 16)\
			or (col == 3 and row > 24) or (col == 8 and row > 23) or (col == 13 and row > 25) or (row == 20 and col > 8 and col < 14) or (row > 16 and row < 21 and col == 9)\
			or (col == 15 and row > 21 and row < 27) or (row == 22 and col == 14) or (row == 26 and col == 14) or (row == 17 and col > 13 and col < 16) or (row == 12 and col > 13 and col < 16)\
			or (row == 11 and col == 12) or (row == 17 and col > 6 and col < 9) or (row == 15 and col > 0 and col < 3) or (row == 14 and col > 16 and col < 19):
				pygame.draw.rect(screen, color, ((w + m) * col + (m + 40), ((h + m) * row + m) + 50, w, h), 1)

	pygame.display.flip()


	

		