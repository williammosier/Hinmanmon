import pygame
from inputs import get_gamepad

pygame.init()
"""class Hinmanmon(self):
	
	def __init__(self):
		self.stats = []
		self.type = ""
		self.status = "normal"

	def statusEffect(self):
		self.status = 

	def 
"""
class location():
	def __init__(self,file,x,y):
		self.file = file
		self.x = x
		self.y = y

class player():
	def __init__(self,file,x,y):
		self.x = x
		self.y = y
		self.velocity = 7
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

"""def move():
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and p1.x > 0:
		if loc1.x == 0:
			p1.x -= p1.velocity
		else:
			loc1.x += p1.velocity
	if keys[pygame.K_RIGHT] and p1.x < 460:
		if loc1.x == -700 or p1.x <= 250:
			p1.x += p1.velocity
		else:
			loc1.x -= p1.velocity
	if keys[pygame.K_UP] and p1.y > 0:
		if loc1.y == 0:
			p1.y -= p1.velocity
		else:
			loc1.y += p1.velocity
	if keys[pygame.K_DOWN] and p1.y < 440:
		if loc1.y == -1000:
			p1.y += p1.velocity
		else:
			loc1.y -= p1.velocity"""

def redraw(win,loc,p1):
	win.blit(loc.file,(loc.x,loc.y))
	p1.draw(win)
	pygame.display.update()

def main():
	run = True

	char = [pygame.image.load('art/sprites/player_male_sprite_standing.png'),pygame.image.load('art/sprites/player_male_sprite_leftstep.png'),pygame.image.load('art/sprites/player_male_sprite_rightstep.png')]
	p1 = player(char,300,200)
	loc1 = location(pygame.image.load('art/environment/hinman_college.png'),-200,-500)

	win = pygame.display.set_mode((600,400))
	pygame.display.set_caption("Hinmanmon")

	while run:
		pygame.time.delay(100)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()
		buttons = gamepadInput()

		if keys[pygame.K_LEFT] and p1.x > 0:		#MOVES THE PLAYER LEFT
			if loc1.x == 0:
				p1.x -= p1.velocity
			else:
				loc1.x += p1.velocity

		if keys[pygame.K_RIGHT] and p1.x < 460:		#MOVES THE PLAYER RIGHT
			if loc1.x == -700 or p1.x <= 250:
				p1.x += p1.velocity
			else:
				loc1.x -= p1.velocity

		if keys[pygame.K_UP] and p1.y > 0:			#MOVES THE PLAYER UP
			if loc1.y == 0:
				p1.y -= p1.velocity
			else:
				loc1.y += p1.velocity

		if keys[pygame.K_DOWN] and p1.y < 440:		#MOVES THE PLAYER DOWN
			if loc1.y == -1000:
				p1.y += p1.velocity
			else:
				loc1.y -= p1.velocity
				
		#move()
		redraw(win,loc1,p1)
	pygame.quit()
main()