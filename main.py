
import pygame
import random
import time

#defines window dimensions
WIDTH = 640
HEIGHT = 480

#sets the possible moves for Hinmanmon
MOVES = ()

class Hmon():
	def __init__(self):
		self.stats = [random.randrange(0,32),random.randrange(0,32),random.randrange(0,32),random.randrange(0,32),random.randrange(0,32),random.randrange(0,32)]
		self.status = "normal"
		self.hp

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
	def __init__(self,file,mask,transfer,music,x,y,width,height):
		self.file = file
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.mask = pygame.mask.from_surface(mask)
		self.transfer = pygame.mask.from_surface(transfer)
		self.encounter = None
		self.music = music

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
	def __init__(self,name,file,portrait,dialogue,mon):
		trainer.name = name
		self.file = file
		self.portrait = portrait
		self.dialogue = dialogue + " "
		self.mon = mon

#instantiating the trainer objects
al_vos = trainer("Al Vos",None,pygame.image.load('art/character_portraits/al_vos.png'),"Hello, I'm Al Vos! Welcome to Hinman college! What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills.",())
		
def battle(p1,enemy):
	pass

def dialogue(win,trainer):
	font = pygame.font.SysFont("Courier New",20)
	drawTextBox(win,font,trainer)
	time.sleep(.2)
	index = 0
	text_y = 370
	while index < len(trainer.dialogue):
		line = trainer.dialogue[index:index + 46]
		index += 46
		print(line)
		text_sound = pygame.mixer.Sound('sound/sfx/talk.wav')
		while line[-1] != " ":
			line = line[:-1]
			index -= 1
			print(line)
		text_x = 30
		pygame.mixer.Sound.play(text_sound, -1)
		for i in line:
			win.blit(font.render(i, False,(0,0,0)), (text_x,text_y))
			time.sleep(.03)
			pygame.display.update()
			text_x += 10
		text_y += 20
		pygame.mixer.Sound.stop(text_sound)
		if text_y > 430 and index < len(trainer.dialogue):
			time.sleep(.5) #ASK FOR USER FOR INPUT TO CONTINUE
			drawTextBox(win,font,trainer)
			text_y = 370
			
	time.sleep(.5) #ASK FOR USER FOR INPUT TO CONTINUE

def drawTextBox(win,font,trainer):
	pygame.draw.rect(win,(20,20,80),(20,HEIGHT-150,600,130), 10)
	pygame.draw.rect(win,(220,220,220),(25,HEIGHT-145,590,120))
	pygame.draw.rect(win,(20,20,80),(20,HEIGHT-150,470,130), 10)
	win.blit(trainer.portrait,(495,335))
	win.blit(font.render(trainer.name, False,(0,0,0)), (30,340))
	pygame.display.update()

def encounter():
	pass

def fadeIn(win,loc,p1):
	image = pygame.image.load("art/environment/fade.png")
	for i in range(0,225,10):
		win.blit(loc.file,(loc.x,loc.y))
		win.blit(p1.file[0],(p1.x,p1.y))
		image.set_alpha(255-i)
		win.blit(image,(0,0))
		pygame.display.flip()

def fadeOut(win):
	image = pygame.image.load("art/environment/fade.png")
	for i in range(225):
		image.set_alpha(i)
		win.blit(image,(0,0))
		pygame.display.flip()
		pygame.time.delay(1)

def hasAccessTo(p1):
	pass

def interact(win):
	dialogue(win,al_vos)

def isNotCollided(loc,p1mask,p1x,p1y):
	offset = (p1x - loc.x,p1y - loc.y)
	return not(loc.mask.overlap(p1mask,offset))

def locationChange(win,locs,p1,loc):
	offset = (p1.x - locs[loc].x,p1.y - locs[loc].y)
	result = (locs[loc].transfer.overlap(p1.mask,offset))
	if result: #and hasAccessTo()
		fadeOut(win)
	if loc == 0 and p1.x > 500 and result: #Abstract to subfunction that takes loadzone coords and location as parameters
		loc = 1
		p1.x = 90
		p1.y = 300
		musicChange(locs[loc])
		fadeIn(win,locs[loc],p1)
	if loc == 1 and p1.y > 300 and result:
		loc = 0
		p1.x = 560
		p1.y = 220
		musicChange(locs[loc])
		fadeIn(win,locs[loc],p1)
	return loc

def playerInput(win,loc,p1):
	keys = pygame.key.get_pressed()
	offset = (p1.x - loc.x,p1.y - loc.y)
	result = loc.mask.overlap(p1.mask,offset)
	
	if isNotCollided(loc,p1.mask,p1.x,p1.y):
		pygame.display.set_caption("HIT")
	else:
		pygame.display.set_caption("NO HIT")
	
	if keys[pygame.K_a] and p1.x > 0 and isNotCollided(loc,p1.mask,p1.x-5,p1.y):
		if loc.x == 0 or p1.x >= WIDTH//2 - p1.width//2:
			p1.x -= p1.velocity
		else:
			loc.x += p1.velocity
	if keys[pygame.K_d] and p1.x < WIDTH + p1.width and isNotCollided(loc,p1.mask,p1.x+5,p1.y):
		if loc.x == -loc.width + WIDTH or p1.x < WIDTH//2 - p1.width//2:
			p1.x += p1.velocity
		else:
			loc.x -= p1.velocity
	if keys[pygame.K_w] and p1.y > 0 and isNotCollided(loc,p1.mask,p1.x,p1.y-5):
		if loc.y == 0 or p1.y >= HEIGHT//2 - p1.height//2:
			p1.y -= p1.velocity
		else:
			loc.y += p1.velocity
	if keys[pygame.K_s] and p1.y < HEIGHT - p1.height and isNotCollided(loc,p1.mask,p1.x,p1.y+5):
		if loc.y == -loc.height + HEIGHT or p1.y < HEIGHT//2 - p1.height//2:
			p1.y += p1.velocity
		else:
			loc.y -= p1.velocity
	if not(keys[pygame.K_a]) and not(keys[pygame.K_d]) and not(keys[pygame.K_w]) and not(keys[pygame.K_s]):
		p1.walk = 0

	if keys[pygame.K_e]:
		interact(win)

def musicChange(loc):
	pygame.mixer.music.load(loc.music)
	pygame.mixer.music.play(-1)

def pauseMenu():
	pass

def redraw(win,loc,p1):
	win.blit(loc.file,(loc.x,loc.y))
	p1.draw(win)
	pygame.display.update()

def main():
	pygame.init()
	pygame.mixer.init()
	run = True

	#sets up the window
	win = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Hinmanmon")

	#instantiating the player object
	char = (pygame.image.load('art/sprites/player_male_sprite_standing.png'),pygame.image.load('art/sprites/player_male_sprite_leftstep.png'),pygame.image.load('art/sprites/player_male_sprite_rightstep.png'))
	p1 = player(char,WIDTH//2 - 20,HEIGHT//2 - 20)
	pmask = pygame.image.load('art/sprites/player_mask.png').convert_alpha()
	p1.mask = pygame.mask.from_surface(pmask)

	#instantiating the location objects and setting current location
	locs = (location(pygame.image.load('art/environment/hinman_college.png'),pygame.image.load('art/environment/hinman_college_mask.png').convert_alpha(),pygame.image.load('art/environment/hinman_college_loadzones.png'),'sound/music/death.ogg',-1900,-1200,2600,2600),\
		location(pygame.image.load('art/environment/success_center.png'),pygame.image.load('art/environment/success_center_mask.png').convert_alpha(),pygame.image.load('art/environment/success_center_loadzones.png'),'sound/music/reslife.ogg',0,0,640,480))
	loc = 0

	while run:
		pygame.time.delay(50)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		playerInput(win,locs[loc],p1)
		redraw(win,locs[loc],p1)
		loc = locationChange(win,locs,p1,loc)
	pygame.quit()
main()