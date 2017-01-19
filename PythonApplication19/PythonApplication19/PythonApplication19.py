import pygame

#class game:
#	def __init__(self):
size =(900,600)
screen = pygame.display.set_mode(size)
screen.fill((250,250,250))

#		pygame.init()

#		self.screen = pygame.display.set_mode(size)

#		self.font = pygame.font.font(None ,30)

		
done = False

class Player:
	def __init__(self,kleur,x,y,r):
		self.kleur = kleur
		self.x = x
		self.y = y
		self.r = r

	"""def update(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.x -= 10"""


	def draw(self,screen):
		pygame.draw.circle(screen,self.kleur,(int(self.x),int(self.y)),int(self.r))

player1 = Player((137, 237, 75), 300, 30, 13)

while not done:
	#player1 = Player((137, 237, 75), 100, 100, 20)
	player1.draw(screen)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				screen.fill((250,250,250))
				player1.x -= 50
				player1.draw(screen)
			elif event.key == pygame.K_RIGHT:
				screen.fill((250, 250, 250))
				player1.x += 50
				player1.draw(screen)
			elif event.key == pygame.K_UP:
				screen.fill((250, 250, 250))
				player1.y -= 50
				player1.draw(screen)
			elif event.key == pygame.K_DOWN:
				screen.fill((250, 250, 250))
				player1.y += 50
				player1.draw(screen)

	player2=Player((155,255,140),340,30,13)
	player2.draw(screen)
	player3=Player((91,183,211),380,30,13)
	player3.draw(screen)
	player4=Player((116,59,124),420,30,13)
	player4.draw(screen)
	player5=Player((237,65,56),460,30,13)
	player5.draw(screen)
	player6=Player((0,0,0),500,30,13)
	player6.draw(screen)
		

	

	pygame.display.flip()


	

		