import pygame

size =(600,700)
screen = pygame.display.set_mode(size)
screen.fill((250,250,0))

done = False

class Player:
	def __init__(self,kleur,x,y,r):
		self.kleur = kleur
		self.x = x
		self.y = y
		self.r = r

	def draw(self,screen):
		pygame.draw.circle(screen,self.kleur,(int(self.x),int(self.y)),int(self.r))



while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.draw.circle(screen,(0,0,0),(30,30),15)

	player1=Player((137,237,75),100,100,20)
	player1.draw(screen)

	pygame.display.flip()



		