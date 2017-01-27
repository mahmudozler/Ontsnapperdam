#imports
import pygame
from pygame.locals import *
import sys
import time
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
 
    for x in buffer:
        print(x)
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
img6 = pygame.transform.smoothscale(img5,(200, 70))
 
defaultfont = pygame.font.get_default_font()
fontrenderer = pygame.font.Font(defaultfont,85)
 
class hsscreen:
    def __init__(self):
        self.running = True
 
 
 
 
    def introo(self):
 
        while self.running:
            screen.blit(bg1,(0,0))
            screen.blit(label3,(200,15))
            screen.blit(img6,(50,730))
 
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
                    if mousex > 50 and mousex < 150 and mousey > 700 and mousey < 800:
                        self.running = False
                       
 
            pygame.display.flip()
 
