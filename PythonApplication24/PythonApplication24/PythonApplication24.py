#imports
import pygame
from pygame.locals import *
import sys
import time
import random
import psycopg2


# Use the database
def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=postgres user=postgres password='2450086'")
    cursor = connection.cursor()
    
    # Execute the command
    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # Nothing to fetch
        pass

    # Close connection
    cursor.close()
    connection.close()
    
    return results



# Uploads a score into the hiscore table
def upload_score(name, score):
    interact_with_database("UPDATE users SET score = {} WHERE name = '{}'")


# Downloads score data from database
def download_scores():
    return interact_with_database("SELECT * FROM users")


# Downloads the top score from database
def download_top_score():
    result = interact_with_database("SELECT * FROM users ORDER BY name")[0][1]
    return result





pygame.init()
width = 800
height = 850

screen = pygame.display.set_mode((width,height))

#colors

black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
grey = (158,158,158)
done = True


#highscore screen---

pygame.display.set_caption('HighScore')


defaultfont = pygame.font.get_default_font()
fontrenderer = pygame.font.Font(defaultfont,85)

#highscorelabel
label3 = fontrenderer.render("HighScore",1,black)
screen.blit(label3,(200,15))

#select *from users func
score = download_scores()

#print table of users and score
def table():
	buffer=[] 
	for i in score:
		x = "{} --> {}".format(i[0],i[1])
		buffer.append(x)

	#for x in buffer:
		#print(x)
	return buffer
	
list = table()



#data from database
font = pygame.font.SysFont(None, 40)


#---------------------------------------------------------------------------

#gameboard background
bg = pygame.image.load('speelbord.png')
bg1 = pygame.transform.smoothscale(bg,(width,height))
screen = pygame.display.set_mode((width,height))

#back button
img5 = pygame.image.load('back.png')
img6 = pygame.transform.smoothscale(img5,(100, 100))

defaultfont = pygame.font.get_default_font()
fontrenderer = pygame.font.Font(defaultfont,85)

class hsscreen:
	def __init__(self):
		self.running = True




	def introo(self):

		while self.running:
			screen.blit(bg1,(0,0))
			screen.blit(label3,(200,15))
			#screen.blit(score_text, (100, 175))
			screen.blit(img6,(50,25))

			#list
			count = 0
			for s in list:
				count += 1
				screen.blit(font.render("{}".format(s),1,black),(250 ,(150 + (100 * count))))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					Game(players)
				if event.type == pygame.MOUSEBUTTONDOWN:
					mousex, mousey = pygame.mouse.get_pos()
					if mousex > 50 and mousex < 150 and mousey > 25 and mousey < 125:
						self.running = False
						

			pygame.display.flip()


hs = hsscreen()

done = False

pygame.init()
width = 800
height = 850
img = pygame.image.load('play.png')
img3 = pygame.image.load('exit.png')
ologo = pygame.image.load('ontsnapperdam logo.png')
img2 = pygame.transform.smoothscale(img,(200, 70))
img4 = pygame.transform.smoothscale(img3,(200,70))
bg1 = pygame.transform.smoothscale(bg,(width,height))
ologo1 = pygame.transform.smoothscale(ologo,(400,80))
screen = pygame.display.set_mode((width,height))



defaultfont = pygame.font.get_default_font()
fontrenderer = pygame.font.Font(defaultfont,85)

label = fontrenderer.render("Ontsnapperdam",1,red)
label2 = fontrenderer.render("Settings",1,black)


class start:
	def __init__(self):
		self.running = True




	def intro(self):

		while self.running:
			screen.blit(bg1,(0,0))
			screen.blit(img2,(width*0.35,height*0.35))
			screen.blit(img4,(width*0.35,height*0.55))
			screen.blit(ologo1,(15,15))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					Game(players)
				if event.type == pygame.MOUSEBUTTONDOWN:
					mousex, mousey = pygame.mouse.get_pos()
					if  width*0.35 <= mousex and  width*0.60 >= mousex and height*0.35 <=mousey and height*0.466 >= mousey:
						self.running = False
					elif width*0.35 <= mousex and width*0.60 >= mousex and height*0.55 <= mousey and height*0.766 >= mousey:
						pygame.quit()
						quit()

			pygame.display.flip()


menu=start()

done = False


class Player:
    def __init__(self, name, kleur, x, y):
        self.name = name
        self.kleur = kleur
        self.x = x
        self.y = y
        self.r = 10
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.steps = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.kleur, (self.rect.center), self.r)

    def Update(self, screen, event, blocks):
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
                    # convert newpos in the new position
                    self.steps += 1
                    self.rect = newpos
                    # stop check when matched
                    break

    def Pos(self):
        return self.x, self.y


class Game:
    def __init__(self, players):
        pygame.init()
        self.turn = 0
        self.players = players
        self.thrown = 0
        self.size = (800, 850)
        self.running = False

        # block width,height,margin
        self.w = 25
        self.h = 25
        self.m = 1

        # colors
        self.red = (191, 36, 36)
        self.black = (23, 20, 20)

        # self.screen = pygame.display.set_mode(self.size)
        self.blocks = []
        self.battleblocks = []

        # Create list with all block position in the game
        for row in range(30):
            for col in range(30):
                if self.Filter(col, row) == "battleblock":
                    self.battleblocks.append(
                        pygame.Rect((self.w + self.m) * col + self.m + 40, ((self.h + self.m) * row + self.m + 50),
                                    self.w, self.h))
                elif self.Filter(col, row) == "normalblock":
                    self.blocks.append(
                        pygame.Rect((self.w + self.m) * col + self.m + 40, ((self.h + self.m) * row + self.m + 50),
                                    self.w, self.h))

    def Update(self, event):
        player = self.players[self.turn]
        if event.type == pygame.KEYDOWN:
            player.Update(self.screen, event, self.blocks)

            # if all steps made
            if player.steps == self.thrown:
                self.thrown = 0
                print(player.Pos())
                if self.turn == (len(self.players) - 1):
                    self.turn = 0
                else:
                    self.turn += 1
                player.steps = 0

    def Filter(self, x, y):
        map_list = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0, 9, 19], [0, 9, 10, 19],
                    [0, 10, 19], [0, 10, 19],
                    [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 19], [0, 2, 4, 8, 13, 17, 18, 19],
                    [0, 2, 3, 4, 8, 13, 17, 19], [0, 4, 8, 11, 12, 13, 14, 15, 16, 17, 19], [0, 4, 8, 11, 19],
                    [0, 4, 5, 6, 7, 8, 11, 13, 14, 15, 16, 17, 18, 19], [0, 6, 11, 12, 13, 16, 19],
                    [0, 6, 13, 14, 15, 16, 19], [0, 3, 4, 5, 6, 13, 16, 19],
                    [0, 3, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19],
                    [0, 1, 2, 3, 6, 13, 16, 19], [0, 3, 6, 13, 16, 19], [0, 3, 6, 7, 8, 9, 13, 14, 15, 16, 19],
                    [0, 2, 3, 4, 5, 6, 9, 13, 19], [0, 2, 9, 13, 19], [0, 2, 9, 10, 11, 12, 13, 19],
                    [0, 2, 3, 4, 5, 6, 13, 19], [0, 6, 13, 14, 15, 19],
                    [0, 6, 15, 19], [0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 19], [0, 1, 2, 3, 4, 5, 6, 8, 15, 19],
                    [3, 8, 13, 14, 15, 19], [3, 8, 13, 19], [3, 8, 13, 19],
                    [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
        battle_blocks = [[], [], [], [0], [0], [0, 1], [0], [13, 17], [8, 13, 14, 15, 16, 17], [8], [7, 8], [],
                         [13, 14], [3, 4, 5, 6, 13],
                         [3, 6, 13], [13], [13], [13, 14], [], [], [], [], [], [], [], [3, 4, 5, 6], [3, 13], [13],
                         [13], [11, 12, 13]]
        if x in battle_blocks[y]:
            return "battleblock"
        elif x in map_list[y]:
            return "normalblock"
        return False

    def Draw(self):

        # draw canvas
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill((255, 255, 255))

        # draw dice
        pygame.draw.rect(self.screen, (0, 0, 0), (10, 10, 50, 50), 1)

        # draw all player
        for player in self.players:
            player.draw(self.screen)

        # draw game board
        for rectangle in self.blocks:
            pygame.draw.rect(self.screen, self.black, rectangle, 1)
        for rectangle in self.battleblocks:
            pygame.draw.rect(self.screen, self.red, rectangle, 1)

        # update whole screen
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
                        # pygame.display.flip()


player1 = Player("A", (155, 255, 140), 200, 28)
player2 = Player("B", (155, 255, 140), 226, 28)
player3 = Player("C", (91, 183, 211), 252, 28)
player4 = Player("D", (116, 59, 124), 278, 28)
player5 = Player("E", (237, 65, 56), 304, 28)
player6 = Player("F", (0, 0, 0), 330, 28)

players = [player1, player2, player3, player4]

game = Game(players)

class Program:
	menu.intro()
	hs.introo()
	game.Gameloop()


Program()