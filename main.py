import pygame
import random

pygame.init()

class Hmon():
	def __init__(self):
		self.stats = [random.randrange(0,32),random.randrange(0,32),random.randrange(0,32),random.randrange(0,32),random.randrange(0,32),random.randrange(0,32)]
		self.status = "normal"

	def changeHealth(self):
		pass

	def levelUp(self):
		pass

class baldman(Hmon):
	def __init__(self):
		super().__init__(self)
		self.name = "baldman"
		self.type = "Harpur"

class location():
	def __init__(self,file,mask,x,y,width,height):
		self.file = file
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.mask = pygame.mask.from_surface(mask)

class player():
	def __init__(self,file,x,y):
		self.file = file
		self.x = x
		self.y = y
		self.width = 40
		self.height = 40
		self.velocity = 5
		self.mon = []
		self.walk = 0
		self.mask = None

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

def isEncounter():
	pass

def isNotCollided():
	pass

def locationChange():
	musicChange()

def moveLeft(loc,p1,keys):
	if keys[pygame.K_LEFT] and p1.x > 0:
		if loc.x == 0 or p1.x >= WIDTH//2 + p1.width//2:
			p1.x -= p1.velocity
		else:
			loc.x += p1.velocity

def moveRight(loc,p1,keys):
	if keys[pygame.K_RIGHT] and p1.x < WIDTH + p1.width:
		if loc.x == -loc.width + WIDTH or p1.x < WIDTH//2 - p1.width//2:
			p1.x += p1.velocity
		else:
			loc.x -= p1.velocity

def moveUp(loc,p1,keys):
	if keys[pygame.K_UP] and p1.y > 0:
		if loc.y == 0 or p1.y >= HEIGHT//2 + p1.height//2:
			p1.y -= p1.velocity
		else:
			loc.y += p1.velocity

def moveDown(loc,p1,keys):
	if keys[pygame.K_DOWN] and p1.y < HEIGHT - p1.height:
		if loc.y == -loc.height + HEIGHT or p1.y < HEIGHT//2 - p1.height//2:
			p1.y += p1.velocity
		else:
			loc.y -= p1.velocity

def isMoving(p1,keys):
	if (not(keys[pygame.K_LEFT]) and not(keys[pygame.K_RIGHT]) and not(keys[pygame.K_UP]) and not(keys[pygame.K_DOWN])) or (keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]) or (keys[pygame.K_UP] and keys[pygame.K_DOWN]):
		p1.walk = 0

def move(loc,p1):
	keys = pygame.key.get_pressed()
	offset = (p1.x - loc.x,p1.y - loc.y)
	result = loc.mask.overlap(p1.mask,offset)

	if result:
		pygame.display.set_caption("HIT")
	else:
		pygame.display.set_caption("NO HIT")

	moveLeft(loc,p1,keys)
	moveRight(loc,p1,keys)
	moveUp(loc,p1,keys)
	moveDown(loc,p1,keys)
	isMoving(p1,keys)

def musicChange():
	pass

def pauseMenu():
	pass

def redraw(win,loc,p1):
	win.blit(loc.file,(loc.x,loc.y))
	p1.draw(win)
	pygame.display.update()

#defines window dimensions
WIDTH = 600
HEIGHT = 400

#sets the possible moves for Hinmanmon
MOVES = ()

def main():
	run = True

	#sets up the window
	win = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Hinmanmon")

	#instantiating the player object
	char = [pygame.image.load('art/sprites/player_male_sprite_standing.png'),pygame.image.load('art/sprites/player_male_sprite_leftstep.png'),pygame.image.load('art/sprites/player_male_sprite_rightstep.png')]
	p1 = player(char,WIDTH//2 - 20,HEIGHT//2 - 20)
	pmask = pygame.image.load('art/sprites/player_mask.png').convert_alpha()
	p1.mask = pygame.mask.from_surface(pmask)

	#instantiating the location objects and setting current location
	locs = [location(pygame.image.load('art/environment/hinman_college.png'),pygame.image.load('art/environment/hinman_college_mask.png').convert_alpha(),-200,-500,3200,3200)]
	loc = 0

	while run:
		pygame.time.delay(50)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		move(locs[loc],p1)
		redraw(win,locs[loc],p1)
	pygame.quit()
main()
