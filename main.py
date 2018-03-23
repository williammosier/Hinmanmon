import pygame
import random
import time

#defines window dimensions
WIDTH = 640
HEIGHT = 480

#set several fixed color values for future reference
COLORS = {
	'black': (0,0,0),
	'navy': (20,20,80),
	'lightgray': (220,220,220),
	'white': (255,255,255),
	'pantone342': (64,112,96),
	'darkgreen': (14,72,56),
	'greygreen': (204,252,236)
}

#sets the possible moves for Hinmanmon
MOVES = ()

class Hinman():
	def __init__(self):
		self.window = pygame.display.set_mode((WIDTH,HEIGHT))
		self.locs = {"hinman college":location(pygame.image.load('art/environment/hinman_college.png'),pygame.image.load('art/environment/hinman_college_mask.png').convert_alpha(),pygame.image.load('art/environment/hinman_college_loadzones.png'),'sound/music/death.ogg',-1900,-1200,2600,2600)}
		self.locs["success center"] = location(pygame.image.load('art/environment/success_center.png'),pygame.image.load('art/environment/success_center_mask.png').convert_alpha(),pygame.image.load('art/environment/success_center_loadzones.png'),'sound/music/reslife.ogg',0,0,640,480)
		self.locs["hughes"] = location(pygame.image.load('art/environment/hughes.png'),pygame.image.load('art/environment/hughes_mask.png').convert_alpha(),pygame.image.load('art/environment/hughes_loadzones.png'),'sound/music/reslife.ogg',0,0,2000,500)
		self.locs["cleveland"] = location(pygame.image.load('art/environment/cleveland.png'),pygame.image.load('art/environment/cleveland_mask.png').convert_alpha(),pygame.image.load('art/environment/cleveland_loadzones.png'),'sound/music/reslife.ogg',0,0,2000,500)
		self.locs["lehman"] = location(pygame.image.load('art/environment/lehman.png'),pygame.image.load('art/environment/lehman_mask.png').convert_alpha(),pygame.image.load('art/environment/lehman_loadzones.png'),'sound/music/reslife.ogg',0,0,2000,500)
		self.locs["roosevelt"] = location(pygame.image.load('art/environment/roosevelt.png'),pygame.image.load('art/environment/roosevelt_mask.png').convert_alpha(),pygame.image.load('art/environment/roosevelt_loadzones.png'),'sound/music/reslife.ogg',0,0,2000,500)
		self.current_loc = "hinman college"
		self.dialogues = None
		char = (pygame.image.load('art/sprites/player_male_sprite_standing.png'),pygame.image.load('art/sprites/player_male_sprite_leftstep.png'),pygame.image.load('art/sprites/player_male_sprite_rightstep.png'))
		self.player = player(char,WIDTH//2 - 20,HEIGHT//2 - 20)
		pmask = pygame.image.load('art/sprites/player_mask.png').convert_alpha()
		self.player.mask = pygame.mask.from_surface(pmask)
		self.trainers = {"Al Vos": trainer("Al Vos",None,pygame.image.load('art/character_portraits/al_vos.png'),"Hello, I'm Al Vos! Welcome to Hinman college! What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills.",())}

	def dialogue(self,trainer):
		font = pygame.font.Font("art/font/AnonymousPro-Bold.ttf",20)
		self.drawTextBox(font,trainer)
		time.sleep(.2)
		index = 0
		text_y = 370
		text_speed = .03
		while index < len(trainer.dialogue):
			next_tile = True
			line = trainer.dialogue[index:index + 46]
			index += 46
			text_sound = pygame.mixer.Sound('sound/sfx/talk.wav')
			while line[-1] != " ":
				line = line[:-1]
				index -= 1
			text_x = 30
			pygame.mixer.Sound.play(text_sound, -1)
			for i in line:
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						text_speed = 0
				self.window.blit(font.render(i,False,COLORS['black']),(text_x,text_y))
				time.sleep(text_speed)
				pygame.display.update()
				text_x += 10
			text_y += 20
			pygame.mixer.Sound.stop(text_sound)
			if text_y > 430 and index < len(trainer.dialogue):
				while next_tile:
					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							next_tile = False
				self.drawTextBox(font,trainer)
				text_speed = .03
				text_y = 370
				
		while next_tile:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					next_tile = False

	def drawTextBox(self,font,trainer):
		pygame.draw.rect(self.window,COLORS['darkgreen'],(20,HEIGHT-150,600,130),10)
		pygame.draw.rect(self.window,COLORS['greygreen'],(25,HEIGHT-145,590,120))
		pygame.draw.rect(self.window,COLORS['darkgreen'],(20,HEIGHT-150,470,130),10)
		self.window.blit(trainer.portrait,(495,335))
		self.window.blit(font.render(trainer.name,False,COLORS['black']),(30,340))
		pygame.display.update()

	def fadeIn(self):
		image = pygame.image.load("art/environment/fade.png")
		for i in range(0,225,10):
			self.window.blit(self.locs[self.current_loc].file,(self.locs[self.current_loc].x,self.locs[self.current_loc].y))
			self.window.blit(self.player.file[0],(self.player.x,self.player.y))
			image.set_alpha(225-i)
			self.window.blit(image,(0,0))
			pygame.display.flip()

	def fadeOut(self):
		image = pygame.image.load("art/environment/fade.png")
		for i in range(225):
			image.set_alpha(i)
			self.window.blit(image,(0,0))
			pygame.display.flip()
			pygame.time.delay(1)

	def interact(self):
		self.dialogue(self.trainers["Al Vos"])

	def isNotCollided(self,player_x,player_y):
		offset = (player_x - self.locs[self.current_loc].x,player_y - self.locs[self.current_loc].y)
		return True #not(self.locs[self.current_loc].mask.overlap(self.player.mask, offset))

	def locationChange(self):
		offset = (self.player.x - self.locs[self.current_loc].x,self.player.y - self.locs[self.current_loc].y)
		result = (self.locs[self.current_loc].transfer.overlap(self.player.mask,offset))
		if result: #and hasAccessTo()
			self.fadeOut()
		if self.current_loc == "hinman college" and self.player.x > 500 and result:
			self.current_loc = "success center"
			self.player.x = 90
			self.player.y = 300
			self.musicChange()
			self.fadeIn()
		# if self.current_loc == "hinman college" and self.locs[self.current_loc].y > -1000 and -1900 < self.locs[self.current_loc].x < -1800 and result:
		# 	self.current_loc = "cleveland"
		# 	self.player.x = 500
		# 	self.player.y = 80
		# 	self.locs[self.current_loc].x = -1300
		# 	self.locs[self.current_loc].y = 0
		# 	self.musicChange()
		# 	self.fadeIn()
		# if self.current_loc == "hinman college" and self.locs[self.current_loc].y > -1000 and -1900 < self.locs[self.current_loc].x < -1800 and result:
		# 	self.current_loc = "hughes"
		# 	self.player.x = 500
		# 	self.player.y = 80
		# 	self.locs[self.current_loc].x = -1300
		# 	self.locs[self.current_loc].y = 0
		# 	self.musicChange()
		# 	self.fadeIn()
		if self.current_loc == "hinman college" and -1150 < self.locs[self.current_loc].y < -1050 and -1250 < self.locs[self.current_loc].x < -1150 and result:
			self.current_loc = "lehman"
			self.player.x = 280
			self.player.y = 300
			self.locs[self.current_loc].x = 0
			self.locs[self.current_loc].y = 0
			self.musicChange()
			self.fadeIn()
		if self.current_loc == "hinman college" and -1000 < self.locs[self.current_loc].y and -1900 < self.locs[self.current_loc].x < -1800 and result:
			self.current_loc = "lehman"
			self.player.x = 500
			self.player.y = 80
			self.locs[self.current_loc].x = -1300
			self.locs[self.current_loc].y = 0
			self.musicChange()
			self.fadeIn()
		# if self.current_loc == "hinman college" and self.locs[self.current_loc].y > -1000 and -1900 < self.locs[self.current_loc].x < -1800 and result:
		# 	self.current_loc = "roosevelt"
		# 	self.player.x = 500
		# 	self.player.y = 80
		# 	self.locs[self.current_loc].x = -1300
		# 	self.locs[self.current_loc].y = 0
		# 	self.musicChange()
		# 	self.fadeIn()
		if self.current_loc == "success center" and self.player.y > 300 and result:
			self.current_loc = "hinman college"
			self.player.x = 560
			self.player.y = 220
			self.musicChange()
			self.fadeIn()

	def musicChange(self):
		pygame.mixer.music.load(self.locs[self.current_loc].music)
		pygame.mixer.music.play(-1)

	def playerInput(self):
		keys = pygame.key.get_pressed()
		offset = (self.player.x - self.locs[self.current_loc].x,self.player.y - self.locs[self.current_loc].y)
		result = self.locs[self.current_loc].mask.overlap(self.player.mask,offset)
		if self.isNotCollided(self.player.x,self.player.y):
			pygame.display.set_caption("HIT"+" locx: "+str(self.locs[self.current_loc].x)+" locy: "+str(self.locs[self.current_loc].y))
		else:
			pygame.display.set_caption("NO HIT"+" locx: "+str(self.locs[self.current_loc].x)+" locy: "+str(self.locs[self.current_loc].y))

		if keys[pygame.K_a] and self.player.x > 0 and self.isNotCollided(self.player.x-5,self.player.y):
			if self.locs[self.current_loc].x == 0 or self.player.x >= WIDTH//2 - self.player.width//2:
				self.player.x -= self.player.velocity
			else:
				self.locs[self.current_loc].x += self.player.velocity
		if keys[pygame.K_d] and self.player.x < WIDTH + self.player.width and self.isNotCollided(self.player.x+5,self.player.y):
			if self.locs[self.current_loc].x == -self.locs[self.current_loc].width + WIDTH or self.player.x < WIDTH//2 - self.player.width//2:
				self.player.x += self.player.velocity
			else:
				self.locs[self.current_loc].x -= self.player.velocity
		if keys[pygame.K_w] and self.player.y > 0 and self.isNotCollided(self.player.x,self.player.y-5):
			if self.locs[self.current_loc].y == 0 or self.player.y >= HEIGHT//2 - self.player.height//2:
				self.player.y -= self.player.velocity
			else:
				self.locs[self.current_loc].y += self.player.velocity
		if keys[pygame.K_s] and self.player.y < HEIGHT - self.player.height and self.isNotCollided(self.player.x,self.player.y+5):
			if self.locs[self.current_loc].y == -self.locs[self.current_loc].height + HEIGHT or self.player.y < HEIGHT//2 - self.player.height//2:
				self.player.y += self.player.velocity
			else:
				self.locs[self.current_loc].y -= self.player.velocity
		if not(keys[pygame.K_a]) and not(keys[pygame.K_d]) and not(keys[pygame.K_w]) and not(keys[pygame.K_s]):
			self.player.walk = 0

		if keys[pygame.K_e]:
			self.interact()

	def redraw(self):
		self.window.blit(self.locs[self.current_loc].file,(self.locs[self.current_loc].x,self.locs[self.current_loc].y))
		self.player.draw(self.window)
		pygame.display.update()

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
		self.name = name
		self.file = file
		self.portrait = portrait
		self.dialogue = dialogue + " "
		self.mon = mon

"""		
def battle(p1,enemy):
	pass
<<<<<<< HEAD
def encounter():
	pass
def hasAccessTo(p1):
	pass
=======

def encounter():
	pass

def hasAccessTo(p1):
	pass

>>>>>>> a94f0692120c9ba1a354b893086cd3c408d361f3
def pauseMenu():
	pass
"""
def main():
	pygame.init()
	pygame.mixer.init()
	run = True

	pygame.display.set_caption("Hinmanmon")

	game = Hinman()

	while run:
		pygame.time.delay(50)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		game.playerInput()
		game.redraw()
		game.locationChange()
	pygame.quit()
main()