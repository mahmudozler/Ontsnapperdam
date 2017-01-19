import pygame

pygame.init()


size =(900,600)
screen = pygame.display.set_mode(size)
screen.fill((250,250,250))

#		pygame.init()

#		self.screen = pygame.display.set_mode(size)

#		self.font = pygame.font.font(None ,30)

		
done = False

class Player:
	def __init__(self,name,kleur,x,y,r):
		self.name = name
		self.kleur = kleur
		self.x = x
		self.y = y
		self.r = r

	def draw(self,screen):
		pygame.draw.circle(screen,self.kleur,(int(self.x),int(self.y)),int(self.r))

def Update(key,player):
	if key == pygame.K_LEFT:
		screen.fill((250, 250, 250))
		player.x -= 40
		player.draw(screen)
	elif key == pygame.K_RIGHT:
		screen.fill((250, 250, 250))
		player.x += 40
		player.draw(screen)
	elif key == pygame.K_UP:
		screen.fill((250, 250, 250))
		player.y -= 40
		player.draw(screen)
	elif key == pygame.K_DOWN:
		screen.fill((250, 250, 250))
		player.y += 40
		player.draw(screen)

class Turn:
	def __init__(self,players):
		self.players = players


player1 = Player("A",(155,255,140),300,30,13)
player2 = Player("B",(155,255,140),340,30,13)
player3 = Player("C",(91,183,211),380,30,13)
player4 = Player("D",(116,59,124),420,30,13)
player5 = Player("E",(237,65,56),460,30,13)
player6 = Player("F",(0,0,0),500,30,13)

players = [player1,player2,player3]
turn = Turn(players)

for x in turn.players:
	print(x.name)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
			Update(event.key,player1)


	#player draw
	player1.draw(screen)
	player2.draw(screen)
	player3.draw(screen)
	player4.draw(screen)
	player5.draw(screen)
	player6.draw(screen)

	pygame.display.flip()


	

		