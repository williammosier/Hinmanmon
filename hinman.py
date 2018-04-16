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

MOVES = {}

class Hinman():
	def __init__(self):
		self.window = pygame.display.set_mode((WIDTH,HEIGHT))
		self.locs = {
			"hinman college":\
			location.Location(pygame.image.load('art/environment/hinman_college.png'),\
			pygame.image.load('art/environment/hinman_college_mask.png').convert_alpha(),\
			pygame.image.load('art/environment/hinman_college_loadzones.png'),\
			'sound/music/death.ogg',-1900,-1200,3000,3000),

			"success center":\
			location.Location(pygame.image.load('art/environment/success_center.png'),\
			pygame.image.load('art/environment/success_center_mask.png').convert_alpha(),\
			pygame.image.load('art/environment/success_center_loadzones.png'),\
			'sound/music/reslife.ogg',0,0,640,480),

			"hughes":\
			location.Location(pygame.image.load('art/environment/hughes.png'),\
			pygame.image.load('art/environment/hughes_mask.png').convert_alpha(),\
			pygame.image.load('art/environment/hughes_loadzones.png'),\
			'sound/music/reslife.ogg',0,0,2000,500),

			"cleveland":\
			location.Location(pygame.image.load('art/environment/cleveland.png'),\
			pygame.image.load('art/environment/cleveland_mask.png').convert_alpha(),\
			pygame.image.load('art/environment/cleveland_loadzones.png'),\
			'sound/music/reslife.ogg',0,0,2000,500),

			"lehman":\
			location.Location(pygame.image.load('art/environment/lehman.png'),\
			pygame.image.load('art/environment/lehman_mask.png').convert_alpha(),\
			pygame.image.load('art/environment/lehman_loadzones.png'),\
			'sound/music/reslife.ogg',0,0,2000,500),

			"roosevelt":\
			location.Location(pygame.image.load('art/environment/roosevelt.png'),\
			pygame.image.load('art/environment/roosevelt_mask.png').convert_alpha(),\
			pygame.image.load('art/environment/roosevelt_loadzones.png'),\
			'sound/music/reslife.ogg',0,0,2000,500),

			"smith":\
			location.Location(pygame.image.load('art/environment/smith.png'),\
			pygame.image.load('art/environment/smith_mask.png').convert_alpha(),\
			pygame.image.load('art/environment/smith_loadzones.png'),\
			'sound/music/reslife.ogg',0,0,2000,500)
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
		self.player = player.Player(char,230,250,pmask)
		self.trainers = {
			"Al Vos": trainer.Trainer("Al Vos",None,pygame.image.load('art/character_portraits/al_vos.png'), "Hello, I'm Al Vos! Welcome to Hinman college! What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills.",())

			}

		#MAIN LOOP STARTS HERE#########################
		# pygame.init()
		# pygame.mixer.init()
		# clock = pygame.time.Clock()
		# pygame.display.set_caption("Hinmanmon")

		# run = True

		# view = gui.GUI(WIDTH,HEIGHT)
		# control = controller.Controller()
		# splash = menu.SplashScreen(view.window)

		# while run:
		# 	for event in pygame.event.get():
		# 		if event.type == pygame.QUIT:
		# 			run = False

		# 	# while splash.cutscene != 2:
		# 	# 	splash.moveClouds()
		# 	# 	clock.tick(60)

		# 	control.playerInput(self,view)
		# 	view.redraw(self)
		# 	self.encounter()
		# 	self.locationChange(view)
		# 	clock.tick(60)

		# pygame.quit()
		#MAIN LOOP ENDS HERE###########################

	def battleCalc(self,state):
		pass

	def encounter(self):
		if 650 < self.player.x - self.locs[self.current_loc].x < 1200 and 700 < self.player.y - self.locs[self.current_loc].y < 1250 and self.current_loc == "hinman college":
			x = random.randrange(1,201)
			if x > 199:
				mon = baldman.Baldman()
				return (True,mon)
		return (False,None)


	def interact(self,view):
		view.dialogue(self.trainers["Al Vos"])

	def isNotCollided(self,player_x,player_y):
		offset = (player_x - self.locs[self.current_loc].x,player_y - self.locs[self.current_loc].y)
		print(((player_x,player_y),offset))
		return not(self.locs[self.current_loc].mask.overlap(self.player.mask, offset))

	def locationChange(self,view):
		offset = (self.player.x - self.locs[self.current_loc].x,self.player.y - self.locs[self.current_loc].y)
		result = (self.locs[self.current_loc].transfer.overlap(self.player.mask,offset))
			
		self.specificLoadzone(result,view,"hinman college","success center",90,300,slx=2850,sly=1600,suy=1700)
		self.specificLoadzone(result,view,"success center","hinman college",460,220,lx=-2359,ly=-1415,sly=300)

		self.specificLoadzone(result,view,"hinman college","lehman",280,300,lx=0,ly=0,slx=1700,sux=1800,sly=1500,suy=1600)
		self.specificLoadzone(result,view,"lehman","hinman college",302,214,lx=-1443,ly=-1383,sux=320,sly=350)
		self.specificLoadzone(result,view,"hinman college","lehman",500,75,lx=-1300,slx=2450,sux=2500,sly=1350,suy=1450)
		self.specificLoadzone(result,view,"lehman","hinman college",302,214,lx=-1850,ly=-1050,slx=1800,suy=100)

		self.specificLoadzone(result,view,"hinman college","smith",500,75,lx=-1300,slx=2450,sux=2500,sly=1350,suy=1450)
		self.specificLoadzone(result,view,"smith","hinman college",302,214,lx=-1850,ly=-1050,slx=1800,suy=100)
		self.specificLoadzone(result,view,"hinman college","smith",430,175,lx=-1300,slx=2200,sux=2250,sly=2450,suy=2550)
		self.specificLoadzone(result,view,"smith","hinman college",302,214,lx=-1850,ly=-1050,slx=1800,suy=100)

	def specificLoadzone(self,result,view,start,end,ex,ey,lx=None,ly=None,slx=0,sux=5000,sly=0,suy=5000):
		if self.current_loc == start and slx < self.player.x - self.locs[self.current_loc].x < sux and sly < self.player.y - self.locs[self.current_loc].y < suy and result:
			view.fadeOut()
			self.current_loc = end
			self.player.x = ex
			self.player.y = ey
			self.locs[self.current_loc].x = lx or self.locs[self.current_loc].x
			self.locs[self.current_loc].y = ly or self.locs[self.current_loc].y
			self.musicChange()
			view.fadeIn(self)

	def moveLeft(self):
		if self.locs[self.current_loc].x >= 0 or self.player.x >= WIDTH//2 - self.player.width//2:
			self.player.x -= self.player.velocity
		else:
			self.locs[self.current_loc].x += self.player.velocity
		self.player.direction = "left"

	def moveRight(self):
		if self.locs[self.current_loc].x <= -self.locs[self.current_loc].width + WIDTH or self.player.x < WIDTH//2 - self.player.width//2:
			self.player.x += self.player.velocity
		else:
			self.locs[self.current_loc].x -= self.player.velocity
		self.player.direction = "right"

	def moveUp(self):
		if self.locs[self.current_loc].y >= 0 or self.player.y >= HEIGHT//2 - self.player.height//2:
			self.player.y -= self.player.velocity
		else:
			self.locs[self.current_loc].y += self.player.velocity
		self.player.direction = "backward"

	def moveDown(self):
		if self.locs[self.current_loc].y <= -self.locs[self.current_loc].height + HEIGHT or self.player.y < HEIGHT//2 - self.player.height//2:
			self.player.y += self.player.velocity
		else:
			self.locs[self.current_loc].y -= self.player.velocity
		self.player.direction = "forward"

	def musicChange(self):
		pygame.mixer.music.load(self.locs[self.current_loc].music)
		pygame.mixer.music.play(-1)