import pygame
from pygame.locals import *
import random
import copy
import winnerscreen
import PythonApplication25
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
		self.startblock = pygame.Rect(249, 34, 103, 25)
		self.endblock = pygame.Rect(119, 759, 25, 25)
		self.quests = []
		self.state = "lock"
		self.suprise = 0
		self.questpoints = 0 #0

	def draw(self,screen):
		pygame.draw.circle(screen,self.kleur,(self.rect.center),self.r)

	def Update(self,screen,event,blocks,battleblocks,landmarks,supriseblocks,policeblocks,thrown,picked_card):
		if event.type == pygame.KEYDOWN:
			# to check the new position is within the game blocks
			newpos = self.rect.copy()

			# If player on start block these sizes these steps else normal size steps
			if newpos.colliderect(self.startblock):
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

					#count steps
					if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_UP or event.key == K_DOWN:
						self.steps += 1

					# convert newpos in the new position
					self.rect = newpos

					#check if on end block and player has 3 quest points
					if newpos.colliderect(self.endblock) and self.questpoints >= 3:
						print("endblock!")
						self.state = "end"
						self.steps = thrown
				

					#check if player in battleblock
					for rectangle in battleblocks:
						if newpos.colliderect(rectangle):
							print("LETS BATTLE!")
							sound = pygame.mixer.Sound('img/battlesound.wav')
							sound.play()
							break # stop check when battle block match

					#chek if player in supriseblocks
					for rectangle in supriseblocks:
						if newpos.colliderect(rectangle):
							if self.steps == thrown: # if player ends on suprise block
								if picked_card != 1:
									print("SUPRISEEEE!!")
									sound1 = pygame.mixer.Sound('img/questionsound.wav')
									sound1.play()
							break # stop check when battle block match
				
					#chek if player in policeblocks
					for rectangle in policeblocks:
						if newpos.colliderect(rectangle):
							print("BUSTEDD!!")
							break # stop check when battle block match


					#block check if player in landmark block
					for rectangle in landmarks:
						if newpos.colliderect(rectangle[2]):
							print("LANDMARK HIT")
							sound2 = pygame.mixer.Sound('img/locationsound.wav')
							sound2.play()
							count = 0
							for quest in self.quests:
								if newpos.colliderect(quest[2]):
									#only count questpoint if quest was not doen yet
									if self.quests[count][1] == 0:
										self.questpoints += 1
									self.quests[count][1] = 1
									break
								else:
									count += 1
									print("no check")


					# stop check when matched
					break

	def Pos(self):
		return self.x,self.y

	def suprisePos(self,supriseblocks):
		for rectangle in supriseblocks:
			if self.rect.colliderect(rectangle):
				return True

class Game:
	def __init__(self,players):
		pygame.init()
		self.turn = 0
		self.players = players
		self.thrown = 0
		self.size = (850,850)
		self.running = False
		self.winner = []
		self.landmarks = []
		self.landmark_namelist = [["hilton hotel",0],["de doelen",0],["luxor theater",0],["bijenkorf",0],["kfc",0],["coffeeshop amigo",0],["abn amro",0],["janzen huizen",0],["kabouter buttplug",0],
		["wok to go",0],["hogeschool rotterdam",0],["de rotterdammer",0],["inntel hotel",0],["museumpark orientalis",0],["erasmus mc",0],["amazing oriental",0],["euromast",0],["kunsthall rotterdam",0]]

		# Load game pic locations
		self.dice_img = pygame.image.load('img/dice_throw.png')
		self.check_img = pygame.transform.smoothscale(pygame.image.load('img/check.png'),(13,13))

		self.img = pygame.image.load('img/soldier.png')
		self.img = pygame.transform.smoothscale(self.img,(30,20 ))

		self.img2 = pygame.image.load('img/hilton.png')
		self.img2 = pygame.transform.smoothscale(self.img2,(35,32 ))

		self.img3 = pygame.image.load('img/dedoelen.png')
		self.img3 = pygame.transform.smoothscale(self.img3,(75,60 ))

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
		self.img10 = pygame.transform.smoothscale(self.img10,(50,37 ))

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
		self.img25= pygame.transform.smoothscale(self.img25,(75,25 ))

		self.img26 = pygame.image.load('img/pijl.png')
		self.img26= pygame.transform.smoothscale(self.img26,(30,30 ))

		self.img27 = pygame.image.load('img/boat.png')
		self.img27= pygame.transform.smoothscale(self.img27,(110,100 ))

		self.img28 = pygame.image.load('img/fist.png')
		self.img28= pygame.transform.smoothscale(self.img28,(20,20 ))

		self.img29 = pygame.image.load('img/rotterdammer.png')
		self.img29 = pygame.transform.smoothscale(self.img29, (55, 55))

		#suprise cards
		self.suprise_1 = pygame.transform.smoothscale(pygame.image.load('img/suprise_cards/alien.jpg'),(200,230))
		self.suprise_2 = pygame.transform.smoothscale(pygame.image.load('img/suprise_cards/trump.jpg'),(200,230))
		self.suprise_3 = pygame.transform.smoothscale(pygame.image.load('img/suprise_cards/travesty.jpg'), (200, 230))
		self.suprise_4 = pygame.transform.smoothscale(pygame.image.load('img/suprise_cards/coffee.jpg'), (200, 230))
		self.suprise_5 = pygame.transform.smoothscale(pygame.image.load('img/suprise_cards/howbadah.jpg'), (200, 230))

		# Font list
		self.mapfont = pygame.font.SysFont(None,15)
		self.landmark_font = pygame.font.SysFont(None, 30)
		self.suprise_font = pygame.font.SysFont(None, 32)
		self.info_font = pygame.font.SysFont(None, 20)
		self.dice_font = pygame.font.SysFont(None, 50)

		# Write landmarks on map
		self.text = self.mapfont.render("Rotterdam centraal",True,(0,0,0))
		self.text1 = self.landmark_font.render("L",True,(0,0,0))
		self.text2 = self.mapfont.render("Coffeeshop Amigo",True,(0,0,0))
		self.text3 = self.mapfont.render("Huize Jansen",True,(0,0,0))
		self.text4 = self.mapfont.render("Kabouter Buttplug",True,(0,0,0))
		self.text5 = self.mapfont.render("Museumpark",True,(0,0,0))
		self.text6 = self.mapfont.render("Euromast",True,(0,0,0))
		self.text8 = self.mapfont.render("Rotterdammer", True, (0, 0, 0))
		self.text1 = self.landmark_font.render("L", True, (0, 0, 0))

		#!?(surprise cards)
		self.text7 = self.suprise_font.render("!?",True,(244,152,66))

		#block width,height,margin
		self.w = 25
		self.h = 25
		self.m = 1

		#colors
		self.red = (191,36,36)
		self.black = (23,20,20)
		self.white = (255,255,255)
		self.grey = (133,133,133)
		self.darkgreen = (22,117,35)

		#self.screen = pygame.display.set_mode(self.size)
		self.blocks = []
		self.battleblocks = []
		self.landmarkblocks = []
		self.supriseblocks = []
		self.policeblocks =[]

		self.map_list = [[0,1,2,3,4,5,6,7,8,12,13,14,15,16,17,18,19],[0,9,19],[0,9,10,19],[0,10,19],[0,10,19],
					[0,1,2,4,5,6,7,8,9,10,11,12,13,19],[0,2,4,8,13,17,18,19],[0,2,3,4,8,13,17,19],[0,4,8,11,12,13,14,15,16,17,19],[0,4,8,11,19],
					[0,4,5,6,7,8,11,13,14,15,16,17,18,19],[0,6,11,12,13,16,19],[0,6,13,14,15,16,19],[0,3,4,5,6,13,16,19],[0,3,6,7,8,9,10,11,12,13,16,17,18,19],
					[0,1,2,3,6,13,16,19],[0,3,6,13,16,19],[0,3,6,7,8,9,13,14,15,16,19],[0,2,3,4,5,6,9,13,19],[0,2,9,13,19],[0,2,9,10,11,12,13,19],[0,2,3,4,5,6,13,19],[0,6,13,14,15,19],
					[0,6,15,19],[0,6,7,8,9,10,11,12,13,14,15,19],[0,1,2,3,4,5,6,8,15,19],[3,8,13,14,15,19],[3,8,13,19],[3,8,13,19],[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]]
		self.battle_map_list= [[],[],[],[0],[0],[0,1],[0],[13,17],[8,13,14,15,16,17],[8],[7,8],[],[13,14],[3,4,5,6,13],
			[3,6,13],[13],[13],[13,14],[],[],[],[],[],[],[],[3,4,5,6],[3,13],[13],[13],[11,12,13]]
		self.landmark_maplist = [[],[],[19],[],[],[2],[17],[],[],[11],[5],[],[0,16],[],[8],[],[],[8,15],[],[19],[],[4],[],[15],[11],[0],[],[3,8],[],[16]]
		self.suprise_cards = [[3,14],[],[10],[],[],[0,6,12],[],[2],[13,17],[],[6,15,19],[11],[],[3,19],[11],[16],[6],[13],[0],[],[11],[6,13],[],[],[8,13,19],[3],[],[],[],[3,10,18]]
		self.police_map =[[],[],[],[],[],[13],[],[],[4],[],[],[],[],[],[19],[],[],[9],[2],[],[],[],[],[],[],[],[15],[],[],[],]
		# Create list with all block position in the game
		
		for row in range(30):
			for col in range(30):
				if self.Filter(col, row,self.battle_map_list):
					self.battleblocks.append(
						pygame.Rect((self.w + self.m) * col + self.m + 40, ((self.h + self.m) * row + self.m + 30),
									self.w, self.h))

					# create list with all suprise card blocks positions that are in the battlezones
					if self.Filter(col, row, self.suprise_cards):
						self.supriseblocks.append(
							pygame.Rect((self.w + self.m) * col + self.m + 40, ((self.h + self.m) * row + self.m + 30),
										self.w, self.h))

				elif self.Filter(col, row,self.map_list):
					self.blocks.append(
						pygame.Rect((self.w + self.m) * col + self.m + 40, ((self.h + self.m) * row + self.m + 30),
									self.w, self.h))

					#create list with all landmark block positions
					if self.Filter(col, row,self.landmark_maplist):
						self.landmarkblocks.append(
							pygame.Rect((self.w + self.m) * col + self.m + 40, ((self.h + self.m) * row + self.m + 30),
										self.w, self.h))

					#create list with all suprise card blocks positions
					if self.Filter(col, row,self.suprise_cards):
						self.supriseblocks.append(
							pygame.Rect((self.w + self.m) * col + self.m + 40, ((self.h + self.m) * row + self.m + 30),
										self.w, self.h))
				
					if self.Filter(col, row,self.police_map):
						self.policeblocks.append(
							pygame.Rect((self.w + self.m) * col + self.m + 40, ((self.h + self.m) * row + self.m + 30),
										self.w, self.h))
		# Create complete landmark list( name + cordinates + visit check)
		count = 0
		for l in range(18):
			self.landmarks.append(self.landmark_namelist[count])
			self.landmarks[count].append(self.landmarkblocks[count])
			count += 1

		# generate 3 unique quests or every player
		for player in self.players:
			count = 0
			while count < 3:
				new_landmark = random.choice(self.landmarks)
				if new_landmark not in player.quests:
					player.quests.append(
						copy.deepcopy(new_landmark))  # copy.deepcopy to not change the original list!!!!!
					count += 1

		# special blocks
		self.startblock = self.blocks[8]
		self.startblock.w = 103



	def Update(self, event):
		player = self.players[self.turn]

		# if player throws less than 4 in first turn don't let players make steps
		if self.thrown < 4 and player.state == "lock":
			return
		elif self.thrown < 6 and player.state == "end":
			return
		elif player.suprise == 1:
			return
		elif len(self.winner) == 1:
			print("winner chosen")
			return

		self.Draw()


		# if player throws 4 or more at start, let player in gameboard
		if self.thrown >= 4 and player.state == "lock":
			player.state = "start"

			if event.type == pygame.KEYDOWN:
				player.Update(self.screen, event, (self.blocks + self.battleblocks), self.battleblocks,self.landmarks,self.supriseblocks,self.policeblocks, self.thrown, self.picked_card)

				# if all steps made reset dice throw and set turn to next player
				if player.steps == self.thrown:

					self.thrown = 0
					if self.turn == (len(self.players) - 1):
						self.turn = 0
					else:
						self.turn += 1
					player.steps = 0

		# player throw regular process after start
		else:
			if event.type == pygame.KEYDOWN:
				player.Update(self.screen, event, (self.blocks + self.battleblocks), self.battleblocks,self.landmarks,self.supriseblocks,self.policeblocks, self.thrown, self.picked_card)

				# if all steps made reset dice throw and set turn to next player
				if player.steps == self.thrown:

					if player.suprisePos(self.supriseblocks):
						print("this is so ")
						player.suprise = 1
						return
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

	def Questbar(self):
		# display quests block
		pygame.draw.rect(self.screen, (227, 227, 227), (600, 180, 200, 170))
		self.screen.blit(self.info_font.render("Player {0} - Quests({1}/3)".format((self.turn + 1), self.players[self.turn].questpoints), True,self.black), (620, 190))
		count = 0
		for quest in self.players[self.turn].quests:
			self.screen.blit(self.info_font.render("- {}".format(quest[0]), True, self.black),(620, 220 + (40 * count)))
			# Display text if quest is done or not done
			if quest[1] == 0:
				self.screen.blit(self.info_font.render("not done yet", True, self.grey), (630, 235 + (40 * count)))
			else:
				self.screen.blit(self.info_font.render("done!", True, self.darkgreen), (630, 235 + (40 * count)))
				self.screen.blit(self.check_img, (667, 235 + (40 * count)))
			count += 1

	def Draw(self):

		#draw canvas
		self.screen = pygame.display.set_mode(self.size,RESIZABLE)
		self.screen.fill((250, 250, 250))

		# draw game board
		for rectangle in self.blocks:
			pygame.draw.rect(self.screen, self.grey, rectangle,1)

		for rectangle in self.battleblocks:
			pygame.draw.rect(self.screen, self.red, rectangle, 1)

		# draw dice button
		pygame.draw.rect(self.screen, (0, 0, 0), (600, 50, 70, 70), 1)

		# paste all images
		self.screen.blit(self.img, (510, 400))
		self.screen.blit(self.img2, (500, 80))
		self.screen.blit(self.img3, (70, 110))
		self.screen.blit(self.img4, (378, 159))
		self.screen.blit(self.img4, (144, 237))
		self.screen.blit(self.img4, (534, 393))
		self.screen.blit(self.img5, (42, 215))
		self.screen.blit(self.img6, (250, 238))
		self.screen.blit(self.img7, (435, 175))
		self.screen.blit(self.img8, (170, 262))
		self.screen.blit(self.img9, (353, 240))
		self.screen.blit(self.img10, (483, 340))
		self.screen.blit(self.img11, (235, 354))
		self.screen.blit(self.img12, (65, 340))
		self.screen.blit(self.img13, (70, 425))
		self.screen.blit(self.img14, (240, 418))
		self.screen.blit(self.img4, (274, 471))
		self.screen.blit(self.img15, (379, 420))
		self.screen.blit(self.img16, (415, 450))
		self.screen.blit(self.img17, (505, 522))
		self.screen.blit(self.img18, (276, 551))
		self.screen.blit(self.img29, (130, 527))
		self.screen.blit(self.img19, (70, 630))
		self.screen.blit(self.img20, (296, 625))
		self.screen.blit(self.img20, (324, 625))
		self.screen.blit(self.img20, (352, 625))
		self.screen.blit(self.img21, (458, 627))
		self.screen.blit(self.img4, (92, 498))
		self.screen.blit(self.img22, (458, 730))
		self.screen.blit(self.img4, (430, 705))
		self.screen.blit(self.img23, (250, 720))
		self.screen.blit(self.img24, (200, 683))
		self.screen.blit(self.img25, (145, 735))
		self.screen.blit(self.img26, (118, 758))
		self.screen.blit(self.img27, (10, 714))
		self.screen.blit(self.img28, (329, 788))

		# text map
		self.screen.blit(self.text, (254, 37))
		self.screen.blit(self.text2, (67, 330))
		self.screen.blit(self.text3, (240, 345))
		self.screen.blit(self.text4, (285, 440))
		self.screen.blit(self.text5, (308, 610))
		self.screen.blit(self.text6, (300, 740))
		self.screen.blit(self.text8, (185, 550))

		# L
		self.screen.blit(self.text1, (542, 87))
		self.screen.blit(self.text1, (542, 530))
		self.screen.blit(self.text1, (490, 192))
		self.screen.blit(self.text1, (463, 347))
		self.screen.blit(self.text1, (437, 477))
		self.screen.blit(self.text1, (437, 633))
		self.screen.blit(self.text1, (463, 790))
		self.screen.blit(self.text1, (100, 165))
		self.screen.blit(self.text1, (177, 295))
		self.screen.blit(self.text1, (47, 347))
		self.screen.blit(self.text1, (333, 269))
		self.screen.blit(self.text1, (255, 399))
		self.screen.blit(self.text1, (255, 478))
		self.screen.blit(self.text1, (333, 659))
		self.screen.blit(self.text1, (255, 737))
		self.screen.blit(self.text1, (125, 737))
		self.screen.blit(self.text1, (150, 580))
		self.screen.blit(self.text1, (48, 685))
		# !?
		self.screen.blit(self.text7, (121, 34))
		self.screen.blit(self.text7, (408, 34))
		self.screen.blit(self.text7, (305, 85))
		self.screen.blit(self.text7, (356, 164))
		self.screen.blit(self.text7, (200, 164))
		self.screen.blit(self.text7, (200, 293))
		self.screen.blit(self.text7, (200, 450))
		self.screen.blit(self.text7, (200, 580))
		self.screen.blit(self.text7, (44, 164))
		self.screen.blit(self.text7, (95, 215))
		self.screen.blit(self.text7, (122, 371))
		self.screen.blit(self.text7, (122, 684))
		self.screen.blit(self.text7, (122, 788))
		self.screen.blit(self.text7, (44, 502))
		self.screen.blit(self.text7, (382, 242))
		self.screen.blit(self.text7, (382, 475))
		self.screen.blit(self.text7, (382, 580))
		self.screen.blit(self.text7, (382, 657))
		self.screen.blit(self.text7, (485, 242))
		self.screen.blit(self.text7, (538, 293))
		self.screen.blit(self.text7, (538, 372))
		self.screen.blit(self.text7, (538, 658))
		self.screen.blit(self.text7, (252, 658))
		self.screen.blit(self.text7, (434, 293))
		self.screen.blit(self.text7, (330, 320))
		self.screen.blit(self.text7, (460, 423))
		self.screen.blit(self.text7, (305, 788))
		self.screen.blit(self.text7, (512, 788))


		# draw all player
		count = 0
		for player in self.players:
			count += 1
			player.draw(self.screen)
			self.screen.blit(self.info_font.render("{0}".format(count), 1, self.black),
							 ((player.rect.x + 6), (player.rect.y + 4)))


		# if dice is thrown
		if self.thrown > 0:
			#text handles
			self.screen.blit(self.dice_font.render("{0}".format(self.thrown), True, self.black), (625, 70))
			self.screen.blit(self.info_font.render("You have thrown:", True, self.black), (600, 30))
			if self.thrown < 4 and self.players[self.turn].state == "lock":
				self.screen.blit(self.info_font.render("player {0} ".format((self.turn + 1)), True,self.players[self.turn].kleur), (600, 130))
				self.screen.blit(self.info_font.render("you need to throw 4 or more".format(self.turn), True,self.black), (600, 145))
				self.screen.blit(self.info_font.render("to enter Rotterdam centraal!".format(self.turn), True, self.black),(600, 160))
				self.screen.blit(self.info_font.render("Press for 'Enter' to end your turn", True , self.black),(600, 190))

			#if player comes across surprise card
			elif self.players[self.turn].suprise == 1:
				self.Questbar()
				self.screen.blit(self.info_font.render("You have drawn a surprise card!", True, self.black),(600, 500))

				# print the surprise card that was picked
				if self.picked_card == 1:
					self.screen.blit(self.suprise_5, (600, 525))
					if self.picked_card == 1:
						sound = pygame.mixer.Sound('img/hobodah.wav')
						sound.play()
				elif self.picked_card == 2:
					self.screen.blit(self.suprise_2, (600, 525))
				elif self.picked_card == 3:
					self.screen.blit(self.suprise_3, (600, 525))
				elif self.picked_card == 4:
					self.screen.blit(self.suprise_4, (600, 525))
				elif self.picked_card == 5:
					self.screen.blit(self.suprise_1, (600, 525))


				self.screen.blit(self.info_font.render("Press 'Enter' to end your turn", True, self.black), (600, 785))

			#if player on endblock show text to throw 5 or more to enter ship and win
			elif self.thrown < 5 and self.players[self.turn].state == "end":
				self.screen.blit(self.info_font.render("you need to throw 5 to enter ship!".format(self.turn), True, self.black),(600, 130))
				self.screen.blit(self.info_font.render("Press 'Enter' to end turn", True, self.black), (600, 150))

				# display quests block
				self.Questbar()

			else:
				if self.players[self.turn].state == "end" and self.thrown >= 5:
					self.screen.blit(self.info_font.render("You have entered the ship :)", True, self.black),(600, 130))
					self.winner.append(self.players[self.turn])
					score = PythonApplication25.download_score(self.winner[0].name)
					new_score = score[0][0] + 5
					PythonApplication25.upload_score(new_score,self.winner[0].name)
					self.running = True
					Winscreen = winnerscreen.Winner()
					Winscreen.winaar(self.winner[0].name)


				else:
					self.screen.blit(self.info_font.render("player {0} ".format((self.turn + 1)), True, self.players[self.turn].kleur), (600, 130))
					self.screen.blit(self.info_font.render("may walk {0} steps".format(self.thrown), True,self.black), (655, 130))

				# display quests block
				self.Questbar()


		# if dice is not thrown yet-----------------------
		else:
			self.screen.blit(pygame.transform.smoothscale(self.dice_img,(50,50)),(610,60))
			self.screen.blit(self.info_font.render("Player {0} ".format((self.turn + 1)), True, self.players[self.turn].kleur), (600, 25))
			self.screen.blit(self.info_font.render("throw the dice!", True, (10, 10, 10)),(655, 25))

			# display quests block
			self.Questbar()

			# show text when players to throw 4 to get into game,
			if self.players[self.turn].state == "lock":
				self.screen.blit(self.info_font.render("Throw 4 or more to get",1,self.black),(600,130))
				self.screen.blit(self.info_font.render("on Rotterdam Centraal!", 1, self.black),(600, 145))
			# show text when players need to throw 5 to enter ship
			elif self.thrown < 6 and self.players[self.turn].state == "end":
				self.screen.blit(
					self.info_font.render("you need to throw 5 to enter ship!".format(self.turn), True, self.black),(600, 130))

		# if player completed all quests and has 3 questpoints
		if self.players[self.turn].questpoints >= 3:
			pygame.draw.rect(self.screen, (227, 227, 227), (600, 370, 200, 100))
			self.screen.blit(self.info_font.render("You have 3 questspoints!", True, self.black), (620, 390))
			self.screen.blit(self.info_font.render("Now hurry to the boat", True, self.black), (620, 410))
			self.screen.blit(self.info_font.render("entrance to escape!", True, self.black), (620, 430))


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
					if mousex > 600 and mousex < 670 and mousey > 50 and mousey < 120:
						print("its turn: " + str(self.turn))
						if self.thrown == 0:
							self.picked_card = random.randint(1, 2) #suprise card pick
							self.thrown = random.randint(1, 6)

							#If lower than 4 turn to next player
							if self.thrown < 4:
								self.Update(event)

							# if first turn 4 or higher set player in rotterdam central to start
							if self.players[self.turn].state == "lock" and self.thrown > 3:
								self.players[self.turn].rect.x = 278 #147 #278
								self.players[self.turn].rect.y = 34 #787 #34
							self.Draw()

							# if player on endblock and throw 5 or more
							if self.players[self.turn].state == "end" and self.thrown >= 5:
								self.players[self.turn].rect.x = 80
								self.players[self.turn].rect.y = 730
							self.Draw()

						print("has thrown:" + str(self.thrown))

				# execute if dice is thrown
				if event.type == pygame.KEYDOWN:
					if self.thrown > 0 and len(self.winner) == 0:
						self.Update(event)
						self.Draw()

					#if players throw below 4 in first turn, push turn to next player
					if event.key == K_RETURN and self.thrown > 0 and self.players[self.turn].state == "lock":
						self.thrown = 0
						if self.turn < (len(self.players) - 1):
							self.turn += 1
						else:
							self.turn = 0
						self.Draw()

					elif event.key == K_RETURN and self.thrown > 0 and self.players[self.turn].state == "end" and len(self.winner) == 0:
						self.thrown = 0
						if self.turn < (len(self.players) - 1):
							self.turn += 1
						else:
							self.turn = 0
						self.Draw()

					elif event.key == K_RETURN and self.players[self.turn].suprise == 1:
						self.picked_card = 0
						self.thrown = 0
						self.players[self.turn].suprise = 0
						self.players[self.turn].steps = 0
						if self.turn < (len(self.players) - 1):
							self.turn += 1
						else:
							self.turn = 0
						self.Draw()
			# ...
			#pygame.display.flip()


p1 = Player("Lord Satrya",(224,60,31),200,8)
p2 = Player("Cursed Mahmut",(16,209,84),226,8)
p3 = Player("Danger Perry",(16,112,209),252,8)
p4 = Player("Brede Mike",(140,99,170),278,8)
p5 = Player("Lillith Naga Shane",(234,184,46),304,8)


players = [p1,p2]



#game = Game(players)
#game.Gameloop()











	

		