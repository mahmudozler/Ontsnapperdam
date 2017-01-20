import pygame
import random

pygame.init()

size =(900,600)
screen = pygame.display.set_mode(size)
screen.fill((250,250,250))

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
				self.x -= 40
				self.draw(screen)
			elif event.key == pygame.K_RIGHT:
				screen.fill((250, 250, 250))
				self.x += 40
				self.draw(screen)
			elif event.key == pygame.K_UP:
				screen.fill((250, 250, 250))
				self.y -= 40
				self.draw(screen)
			elif event.key == pygame.K_DOWN:
				screen.fill((250, 250, 250))
				self.y += 40
				self.draw(screen)

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
				print("next dice")
				if self.turn == 5:
					self.turn = 0
				else:
					self.turn += 1
				self.steps = 0

player1 = Player("A",(155,255,140),300,30,13)
player2 = Player("B",(155,255,140),340,30,13)
player3 = Player("C",(91,183,211),380,30,13)
player4 = Player("D",(116,59,124),420,30,13)
player5 = Player("E",(237,65,56),460,30,13)
player6 = Player("F",(0,0,0),500,30,13)

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

	pygame.display.flip()