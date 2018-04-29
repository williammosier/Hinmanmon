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

MOVES = {"bop":5,"smash":10,"rotate":6}

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
		self.player = player.Player(char,230,250,pmask)

		self.dialogues = None
		self.trainers = {
			"Al Vos": trainer.Trainer("Al Vos",None,pygame.image.load('art/character_portraits/al_vos.png'), "Hello, I'm Al Vos! Welcome to Hinman college! What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills.",())

			}

	def battleCalc(self,state):
		print(state)

	def encounter(self):
		if 760 < self.player.x - self.locs[self.current_loc].x < 1387 and 790 < self.player.y - self.locs[self.current_loc].y < 1445 and self.current_loc == "hinman college":
			x = random.randrange(1,201)
			if x > 199:
				mon = baldman.Baldman()
				return (True,mon)
		return (False,None)


	def interact(self,view,model):
		if model.current_loc == "success center":
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

		self.specificLoadzone(result,view,"hinman college","smith",200,330,lx=-1,ly=-20,slx=1480,sux=1550,sly=2700,suy=2800)
		self.specificLoadzone(result,view,"smith","hinman college",302,214,lx=-1196,ly=-2470,slx=0,sux=170,sly=320,suy=360)
		self.specificLoadzone(result,view,"hinman college","smith",430,175,lx=-1276,slx=2200,sux=2250,sly=2450,suy=2550)
		self.specificLoadzone(result,view,"smith","hinman college",302,214,lx=-1908,ly=-2270,slx=1670,sux=1740,sly=0,suy=120)

		self.specificLoadzone(result,view,"hinman college","roosevelt",320,270,lx=-1360,ly=-20,slx=2300,sux=2380,sly=2460,suy=2500)
		self.specificLoadzone(result,view,"roosevelt","hinman college",302,214,lx=-1980,ly=-2270,slx=1660,sux=1732,sly=300,suy=400)
		self.specificLoadzone(result,view,"hinman college","roosevelt",160,70,lx=-1,ly=-1,slx=2480,sux=2540,sly=1645,suy=1650)
		self.specificLoadzone(result,view,"roosevelt","hinman college",302,214,lx=-2206,ly=-1410,slx=0,sux=150,sly=40,suy=80)
		
		# self.specificLoadzone(result,view,"hinman college","lehman",500,75,lx=-1300,slx=2450,sux=2500,sly=1350,suy=1450)
		# self.specificLoadzone(result,view,"lehman","hinman college",302,214,lx=-1850,ly=-1050,slx=1800,suy=100)
		# self.specificLoadzone(result,view,"hinman college","lehman",280,300,lx=0,ly=0,slx=1700,sux=1800,sly=1500,suy=1600)
		# self.specificLoadzone(result,view,"lehman","hinman college",302,214,lx=-1443,ly=-1383,sux=320,sly=350)

		# self.specificLoadzone(result,view,"hinman college","hughes",280,300,lx=0,ly=0,slx=1400,sux=1430,sly=460,suy=520)
		# self.specificLoadzone(result,view,"hughes","hinman college",302,214,lx=-1443,ly=-1383,sux=320,sly=350)
		# self.specificLoadzone(result,view,"hinman college","hughes",500,75,lx=-1300,slx=660,sux=730,sly=600,suy=670)
		# self.specificLoadzone(result,view,"hughes","hinman college",302,214,lx=-1850,ly=-1050,slx=1800,suy=100)

		self.specificLoadzone(result,view,"hinman college","cleveland",380,300,lx=-1300,slx=550,sux=630,sly=700,suy=760)
		self.specificLoadzone(result,view,"cleveland","hinman college",302,214,lx=-363,ly=-517,slx=1660,sux=1740,sly=300,suy=400)
		self.specificLoadzone(result,view,"hinman college","cleveland",200,65,lx=-1,ly=-1,slx=400,sux=450,sly=1400,suy=1480)
		self.specificLoadzone(result,view,"cleveland","hinman college",302,214,lx=-113,ly=-1283,slx=0,sux=180,sly=40,suy=80)

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