import pygame
import random
import time

import baldman
import hinmanmon
import location
import player
import trainer

WIDTH = 640
HEIGHT = 480

COLORS = {
	'black': (0,0,0),
	'navy': (20,20,80),
	'lightgray': (220,220,220),
	'white': (255,255,255),
	'pantone342': (64,112,96),
	'darkgreen': (14,72,56),
	'greygreen': (204,252,236)
}

class Hinman():
	def __init__(self):
		self.window = pygame.display.set_mode((WIDTH,HEIGHT))
		self.locs = {
			"hinman college":\
			location.Location(pygame.image.load('art/environment/hinman_college.png'),\
							pygame.image.load('art/environment/hinman_college_mask.png').convert_alpha(),\
							pygame.image.load('art/environment/hinman_college_loadzones.png'),'sound/music/death.ogg',-1900,-1200,2600,2600),

			"success center":\
			location.Location(pygame.image.load('art/environment/success_center.png'),\
							pygame.image.load('art/environment/success_center_mask.png').convert_alpha(),\
							pygame.image.load('art/environment/success_center_loadzones.png'),'sound/music/reslife.ogg',0,0,640,480),

			"hughes":\
			location.Location(pygame.image.load('art/environment/hughes.png'),\
							pygame.image.load('art/environment/hughes_mask.png').convert_alpha(),\
							pygame.image.load('art/environment/hughes_loadzones.png'),'sound/music/reslife.ogg',0,0,2000,500),

			"cleveland":\
			location.Location(pygame.image.load('art/environment/cleveland.png'),\
							pygame.image.load('art/environment/cleveland_mask.png').convert_alpha(),\
							pygame.image.load('art/environment/cleveland_loadzones.png'),'sound/music/reslife.ogg',0,0,2000,500),

			"lehman":\
			location.Location(pygame.image.load('art/environment/lehman.png'),\
							pygame.image.load('art/environment/lehman_mask.png').convert_alpha(),\
							pygame.image.load('art/environment/lehman_loadzones.png'),'sound/music/reslife.ogg',0,0,2000,500),

			"roosevelt":\
			location.Location(pygame.image.load('art/environment/roosevelt.png'),\
							pygame.image.load('art/environment/roosevelt_mask.png').convert_alpha(),\
							pygame.image.load('art/environment/roosevelt_loadzones.png'),'sound/music/reslife.ogg',0,0,2000,500)
			}

		char = {
			"forward":\
			(pygame.image.load('art/sprites/player/FS.png'),\
			pygame.image.load('art/sprites/player/FL.png'),\
			pygame.image.load('art/sprites/player/FS.png'),\
			pygame.image.load('art/sprites/player/FR.png')),

			"backward":\
			(pygame.image.load('art/sprites/player/BS.png'),\
			pygame.image.load('art/sprites/player/BL.png'),\
			pygame.image.load('art/sprites/player/BS.png'),\
			pygame.image.load('art/sprites/player/BR.png')),

			"left":\
			(pygame.image.load('art/sprites/player/LS.png'),\
			pygame.image.load('art/sprites/player/LL.png'),\
			pygame.image.load('art/sprites/player/LS.png'),\
			pygame.image.load('art/sprites/player/LR.png')),

			"right":\
			(pygame.image.load('art/sprites/player/RS.png'),\
			pygame.image.load('art/sprites/player/RL.png'),\
			pygame.image.load('art/sprites/player/RS.png'),\
			pygame.image.load('art/sprites/player/RR.png'))
			}

		pmask = pygame.image.load('art/sprites/player/mask.png').convert_alpha()
		pmask = pygame.mask.from_surface(pmask)

		self.current_loc = "success center"
		self.dialogues = None
		self.player = player.Player(char,WIDTH//2 - 20,HEIGHT//2 - 20,pmask)
		self.trainers = {
			"Al Vos": trainer.Trainer("Al Vos",None,pygame.image.load('art/character_portraits/al_vos.png'), "Hello, I'm Al Vos! Welcome to Hinman college! What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills.",())

			}

	def battle(self,mon,trainer=None):
		self.window.blit(pygame.image.load('art/environment/battle_screen.jpg'),(0,0))
		font = pygame.font.Font("art/font/AnonymousPro-Bold.ttf",20)
		if trainer != None:
			self.window.blit(font.render("You are challenged by" + trainer.name + "!",False,COLORS['black']),(30,350))
		else:
			self.window.blit(font.render("a wild " + mon.name + " appeared!",False,COLORS['black']),(30,350))
		self.window.blit(self.player.sprites["forward"][0],(100,300))
		self.window.blit(mon.portrait,(445,130))
		pygame.display.update()
		time.sleep(4)

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

	def encounter(self):
		if 650 < self.player.x - self.locs[self.current_loc].x < 1200 and 700 < self.player.y - self.locs[self.current_loc].y < 1250 and self.current_loc == "hinman college":
			x = random.randrange(1,201)
			if x > 199:
				mon = baldman.Baldman()
				self.battle(mon)

	def fadeIn(self):
		image = pygame.image.load("art/environment/fade.png")
		for i in range(0,225,10):
			self.window.blit(self.locs[self.current_loc].file,(self.locs[self.current_loc].x,self.locs[self.current_loc].y))
			self.window.blit(self.player.sprites[self.player.direction][0],(self.player.x,self.player.y))
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
		print(offset)
		return not(self.locs[self.current_loc].mask.overlap(self.player.mask, offset))

	def locationChange(self):
		offset = (self.player.x - self.locs[self.current_loc].x,self.player.y - self.locs[self.current_loc].y)
		result = (self.locs[self.current_loc].transfer.overlap(self.player.mask,offset))
		if result: #and hasAccessTo()
			self.fadeOut()
			
		self.specificLoadzone(result,"hinman college","success center",90,300,slx=2400,sly=1300,suy=1500)
		self.specificLoadzone(result,"success center","hinman college",560,215,sly=300)

		self.specificLoadzone(result,"hinman college","lehman",280,300,lx=0,ly=0,slx=1400,sux=1600,sly=1200,suy=1400)
		self.specificLoadzone(result,"hinman college","lehman",500,75,lx=-1300,slx=2000,sux=2200,suy=1200)
		self.specificLoadzone(result,"lehman","hinman college",250,250,lx=-1250,ly=-1150,sly=300)
		self.specificLoadzone(result,"lehman","hinman college",250,250,lx=-1850,ly=-1050,slx=1800,suy=100)

	def specificLoadzone(self,result,start,end,ex,ey,lx=None,ly=None,slx=0,sux=5000,sly=0,suy=5000):
		if self.current_loc == start and slx < self.player.x - self.locs[self.current_loc].x < sux and sly < self.player.y - self.locs[self.current_loc].y < suy and result:
			self.current_loc = end
			self.player.x = ex
			self.player.y = ey
			self.locs[self.current_loc].x = lx or self.locs[self.current_loc].x
			self.locs[self.current_loc].y = ly or self.locs[self.current_loc].y
			self.musicChange()
			self.fadeIn()

	##^#^#^#^#^#^#^#^#^## - MAKE THE ABOVE INTO A FUNCTION THAT TAKES IN THE LOCATIONS AND COORDINATES AS PARAMETERS - ##^#^#^#^#^#^#^#^#^##

	def musicChange(self):
		pygame.mixer.music.load(self.locs[self.current_loc].music)
		pygame.mixer.music.play(-1)

	def moveLeft(self):
		if self.locs[self.current_loc].x == 0 or self.player.x >= WIDTH//2 - self.player.width//2:
			self.player.x -= self.player.velocity
		else:
			self.locs[self.current_loc].x += self.player.velocity
		self.player.direction = "left"

	def moveRight(self):
		if self.locs[self.current_loc].x == -self.locs[self.current_loc].width + WIDTH or self.player.x < WIDTH//2 - self.player.width//2:
			self.player.x += self.player.velocity
		else:
			self.locs[self.current_loc].x -= self.player.velocity
		self.player.direction = "right"

	def moveUp(self):
		if self.locs[self.current_loc].y == 0 or self.player.y >= HEIGHT//2 - self.player.height//2:
			self.player.y -= self.player.velocity
		else:
			self.locs[self.current_loc].y += self.player.velocity
		self.player.direction = "backward"

	def moveDown(self):
		if self.locs[self.current_loc].y == -self.locs[self.current_loc].height + HEIGHT or self.player.y < HEIGHT//2 - self.player.height//2:
			self.player.y += self.player.velocity
		else:
			self.locs[self.current_loc].y -= self.player.velocity
		self.player.direction = "forward"

	def playerInput(self):
		keys = pygame.key.get_pressed()
		offset = (self.player.x - self.locs[self.current_loc].x,self.player.y - self.locs[self.current_loc].y)
		result = self.locs[self.current_loc].mask.overlap(self.player.mask,offset)

		if self.isNotCollided(self.player.x,self.player.y):
			pygame.display.set_caption("HIT"+" locx: "+str(self.locs[self.current_loc].x)+" locy: "+str(self.locs[self.current_loc].y))
		else:
			pygame.display.set_caption("NO HIT"+" locx: "+str(self.locs[self.current_loc].x)+" locy: "+str(self.locs[self.current_loc].y))

		if keys[pygame.K_w] and self.player.y > 0 and self.isNotCollided(self.player.x,self.player.y-5):
			self.moveUp()
		if keys[pygame.K_s] and self.player.y < HEIGHT - self.player.height and self.isNotCollided(self.player.x,self.player.y+5):
			self.moveDown()
		if keys[pygame.K_a] and self.player.x > 0 and self.isNotCollided(self.player.x-5,self.player.y):
			self.moveLeft()
		if keys[pygame.K_d] and self.player.x < WIDTH + self.player.width and self.isNotCollided(self.player.x+5,self.player.y):
			self.moveRight()

		if not(keys[pygame.K_a]) and not(keys[pygame.K_d]) and not(keys[pygame.K_w]) and not(keys[pygame.K_s]):
			self.player.walk = 0

		if keys[pygame.K_e]:
			self.interact()

		if keys[pygame.K_b] and self.player.velocity == 5:
			self.player.velocity *= 2
		elif keys[pygame.K_b] and self.player.velocity == 10:
			self.player.velocity /= 2

	def redraw(self):
		self.window.blit(self.locs[self.current_loc].file,(self.locs[self.current_loc].x,self.locs[self.current_loc].y))
		self.player.draw(self.window)
		pygame.display.update()