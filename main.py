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
<<<<<<< HEAD
		self.dialogue = dialogue + " "
		self.mon = mon

#instantiating the trainer objects
al_vos = trainer("Al Vos",None,pygame.image.load('art/character_portraits/al_vos.png'),"Hello, I'm Al Vos! Welcome to Hinman college!",())
=======
		self.dialogue = dialogue
		self.mon = mon

#instantiating the trainer objects
al_vos = trainer("Al Vos",None,pygame.image.load('art/character_portraits/al_vos.png'),"Hello, I'm Al Vos! Welcome to Hinman college! What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.",())
>>>>>>> refs/remotes/origin/master
		
def battle(p1,enemy):
	pass

def dialogue(win,trainer):
<<<<<<< HEAD
	font = pygame.font.SysFont("Courier New",20)
	drawTextBox(win,font,trainer)
	time.sleep(.2)
	index = 0
	text_y = 370
	while index < len(trainer.dialogue):
		line = trainer.dialogue[index:index + 41]
		index += 41
		print(line[-1])
=======
	drawTextBox(win,trainer)
	font = pygame.font.SysFont("Courier New",20)
	index = 0
	text_y = 360
	while index < len(trainer.dialogue):
		line = trainer.dialogue[index:index + 41]
		index += 40
		print(line)
>>>>>>> refs/remotes/origin/master
		while line[-1] != " ":
			line = line[:-1]
			index -= 1
			print(line)
		text_x = 30
		for i in line:
			win.blit(font.render(i, False,(0,0,0)), (text_x,text_y))
			time.sleep(.05)
			pygame.display.update()
			text_x += 10
		text_y += 20
<<<<<<< HEAD
		if text_y > 430:
			time.sleep(.5) #ASK FOR USER INPUT BEFORE ADVANCING TO NEXT PANEL
			drawTextBox(win,font,trainer)
			text_y = 370
	time.sleep(.5) #ASK FOR USER INPUT BEFORE ADVANCING TO NEXT PANEL
	
=======
		if text_y > 420:
			drawTextBox(win,trainer)
			text_y = 360
>>>>>>> refs/remotes/origin/master
	"""
	for i in range(len(trainer.dialogue)):
		win.blit(font.render(trainer.dialogue[i], False,(0,0,0)), (text_x,text_y))
		time.sleep(.03)
		pygame.display.update()
		text_x += 10
		if text_x % 400 == 0:
			text_x = 30
			text_y += 20
	"""
<<<<<<< HEAD

def drawTextBox(win,font,trainer):
	pygame.draw.rect(win,(20,20,80),(20,HEIGHT-150,600,130), 10)
	pygame.draw.rect(win,(220,220,220),(25,HEIGHT-145,590,120))
	pygame.draw.rect(win,(20,20,80),(20,HEIGHT-150,470,130), 10)
	win.blit(trainer.portrait,(495,335))
	win.blit(font.render(trainer.name, False,(0,0,0)), (30,340))
	pygame.display.update()

=======

def drawTextBox(win,trainer):
	pygame.draw.rect(win,(20,20,80),(20,HEIGHT-150,600,130), 10)
	pygame.draw.rect(win,(220,220,220),(25,HEIGHT-145,590,120))
	pygame.draw.rect(win,(20,20,80),(20,HEIGHT-150,470,130), 10)
	win.blit(trainer.portrait,(495,335))
	win.blit(font.render(trainer.name, False,(0,0,0)), (30,340))

>>>>>>> refs/remotes/origin/master
def encounter():
	pass

def interact(win):
	dialogue(win,al_vos)
<<<<<<< HEAD

def isNotCollided(loc,p1mask,p1x,p1y):
	offset = (p1x - loc.x,p1y - loc.y)
	return not(loc.mask.overlap(p1mask,offset))


def locationChange(loc,p1,l):
	offset = (p1.x - loc.x,p1.y - loc.y)
	result = (loc.transfer.overlap(p1.mask,offset))
	if l == 0 and p1.x > 500 and result:
		l = 1
		p1.x = 100
		p1.y = 200
		musicChange(loc)
	if l == 1 and p1.y > 300 and result:
		l = 0
		p1.x = 2400
		p1.y = -1200
		musicChange(loc)
	return l

def playerInput(win,loc,p1):
	keys = pygame.key.get_pressed()
	offset = (p1.x - loc.x,p1.y - loc.y)
	result = loc.mask.overlap(p1.mask,offset)

	if isNotCollided(loc,p1.mask,p1.x,p1.y):
		pygame.display.set_caption("HIT")
	else:
		pygame.display.set_caption("NO HIT")

=======

def isNotCollided(loc,p1mask,p1x,p1y):
	offset = (p1x - loc.x,p1y - loc.y)
	return not(loc.mask.overlap(p1mask,offset))


def locationChange(loc,p1,l):
	offset = (p1.x - loc.x,p1.y - loc.y)
	result = (loc.transfer.overlap(p1.mask,offset))
	if l == 0 and p1.x > 500 and result:
		l = 1
		p1.x = 100
		p1.y = 200
		musicChange(loc)
	if l == 1 and p1.y > 300 and result:
		l = 0
		p1.x = 2400
		p1.y = -1200
		musicChange(loc)
	return l

def playerInput(win,loc,p1):
	keys = pygame.key.get_pressed()
	offset = (p1.x - loc.x,p1.y - loc.y)
	result = loc.mask.overlap(p1.mask,offset)

	if isNotCollided(loc,p1.mask,p1.x,p1.y):
		pygame.display.set_caption("HIT")
	else:
		pygame.display.set_caption("NO HIT")

>>>>>>> refs/remotes/origin/master
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
	pygame.mixer.music.play()

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
	locs = (location(pygame.image.load('art/environment/hinman_college.png'),pygame.image.load('art/environment/hinman_college_mask.png').convert_alpha(),pygame.image.load('art/environment/hinman_college_loadzones.png'),'music/death.ogg',-1900,-1200,2600,2600),\
		location(pygame.image.load('art/environment/success_center.png'),pygame.image.load('art/environment/success_center_mask.png').convert_alpha(),pygame.image.load('art/environment/success_center_loadzones.png'),'music/reslife.ogg',0,0,600,400))
	loc = 0

	while run:
		pygame.time.delay(50)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		playerInput(win,locs[loc],p1)
		loc = locationChange(locs[loc],p1,loc)
		redraw(win,locs[loc],p1)
	pygame.quit()
main()