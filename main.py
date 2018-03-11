import pygame
import random

pygame.init()

class Hinmanmon():
	def __init__(self):
		self.stats = []
		self.type = ""
		self.status = "normal"

	def changeHealth(self):
		pass

class location():
	def __init__(self,file,x,y,width,height):
		self.file = file
		self.x = x
		self.y = y
		self.width = width
		self.height = height

class player():
	def __init__(self,file,x,y):
		self.x = x
		self.y = y
		self.width = 40
		self.height = 40
		self.velocity = 5
		self.mon = []
		self.walk = 0
		self.file = file

	def draw(self,win):
		if self.walk > 2:
			self.walk = 0
		win.blit(self.file[self.walk],(self.x,self.y))
		self.walk += 1

class trainer():
	def __init__(self,file,dialog,mon):
		self.file = file
		self.dialog = dialog
		self.mon = mon
		
def battle(p1,enemy):
	pass

def move(loc,p1):
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and p1.x > 0:
		if loc.x == 0 or p1.x >= WIDTH//2 + p1.width//2:
			p1.x -= p1.velocity
		else:
			loc.x += p1.velocity
	if keys[pygame.K_RIGHT] and p1.x < WIDTH + p1.width:
		if loc.x == -loc.width + WIDTH or p1.x < WIDTH//2 - p1.width//2:
			p1.x += p1.velocity
		else:
			loc.x -= p1.velocity
	if keys[pygame.K_UP] and p1.y > 0:
		if loc.y == 0 or p1.y >= HEIGHT//2 + p1.height//2:
			p1.y -= p1.velocity
		else:
			loc.y += p1.velocity
	if keys[pygame.K_DOWN] and p1.y < HEIGHT - p1.height:
		if loc.y == -loc.height + HEIGHT or p1.y < HEIGHT//2 - p1.height//2:
			p1.y += p1.velocity
		else:
			loc.y -= p1.velocity

def redraw(win,loc,p1):
	win.blit(loc.file,(loc.x,loc.y))
	p1.draw(win)
	pygame.display.update()

WIDTH = 600
HEIGHT = 400

def main():
	run = True

	char = [pygame.image.load('art/player_male_sprite_standing.png'),pygame.image.load('art/player_male_sprite_leftstep.png'),pygame.image.load('art/player_male_sprite_rightstep.png')]
	p1 = player(char,WIDTH//2 - 20,HEIGHT//2 - 20)
	locs = [location(pygame.image.load('art/hinman_prototype.png'),-200,-500,1600,1600)]
	loc = 0

	win = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Hinmanmon")

	while run:
		pygame.time.delay(100)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		move(locs[loc],p1)
		redraw(win,locs[loc],p1)
	pygame.quit()
main()