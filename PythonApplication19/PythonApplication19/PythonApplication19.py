import pygame

size =(600,700)
screen = pygame.display.set_mode(size)
screen.fill((250,250,250))

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
	

	player1=Player((137,237,75),100,100,20)
	player1.draw(screen)
	player2=Player((255,255,0),150,100,20)
	player2.draw(screen)
	player3=Player((91,183,211),200,100,20)
	player3.draw(screen)
	player4=Player((116,59,124),250,100,20)
	player4.draw(screen)
	player5=Player((237,65,56),300,100,20)
	player5.draw(screen)
	player6=Player((0,0,0),350,100,20)
	player6.draw(screen)

	pygame.display.flip()



		