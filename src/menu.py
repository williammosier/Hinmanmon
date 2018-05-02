import pygame
import time

WIDTH = 640
HEIGHT = 480

class SplashScreen:
	def __init__(self,window):
		'''
		Defines the menu screen.
		'''
		self.window = window
		self.bg = pygame.image.load("art/environment/menu/bg.png")
		self.bg_clouds = pygame.image.load("art/environment/menu/bg_clouds.png")
		self.bg_clouds_v = -.05
		self.bg_clouds_x = 140
		self.bg_clouds_y = 140
		self.fg_clouds = pygame.image.load("art/environment/menu/fg_clouds.png")
		self.fg_clouds_v = -.2
		self.fg_clouds_x = 200
		self.fg_clouds_y = -100
		self.title = pygame.image.load("art/environment/menu/logo.png")
		self.title_x = 70
		self.title_y = 50
		self.title_size_x = 500
		self.title_size_y = 100
		self.keypress = True
		self.music = pygame.mixer.music.load('sound/music/menu.ogg')
		self.music_on = True
		self.cutscene = 0
		self.text = ["Hello! ",
					"My name is Al Vos and I am the collegiate professor of Hinman College. Let me be the first to say welcome! Although Hinman may not have been your first choice, I promise you are in the right place. ",
					"In Hinman, we place an emphasis on caring relationships, memorable traditions, and genuine friendliness. Hinman’s residents have a reputation on campus for high levels of participation in programs and events. Dorm Wars, Hysteria, and Co-rec football are huge traditions in Hinman. ",
					"But unnique to all other communities, Hinman is also home to many spicy MEMES that are shared between everyone of the community. These memes are known as 'HinmanMon', and they can be used to battle one another. ",
					"During your time in Hinman, you'll make many friends, create memories, and raise several memes of your own. To get started, please meet me in my office as soon as you're done moving in! I hope you're excited for your very own Hinman adventure to begin! "
					]

	def scrollText(self,n):
		'''
		Scrolls through text when a key is pressed.
		'''
		self.window.blit(self.bg,(0,0))
		font = pygame.font.Font("art/font/AnonymousPro-Bold.ttf",20)
		time.sleep(.2)
		index = 0
		text_y = 370
		text_speed = .03
		while index < len(self.text[n]):
			next_tile = True
			line = self.text[n][index:index + 58]
			index += 58
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
				self.window.blit(font.render(i,False,(255,255,255)),(text_x,text_y))
				time.sleep(text_speed)
				pygame.display.update()
				text_x += 10
			text_y += 20
			pygame.mixer.Sound.stop(text_sound)
			if text_y > 430 and index < len(self.text[n]):
				while next_tile:
					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							next_tile = False
				self.window.blit(self.bg,(0,0))
				text_speed = .03
				text_y = 370
		while next_tile:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					next_tile = False

	def fadeOut(self):
		'''
		Defines an image fading out.
		'''
		image = pygame.image.load("art/environment/fade.png")
		for i in range(0,225,2):
			image.set_alpha(i)
			self.window.blit(image,(0,0))
			pygame.display.flip()
			pygame.time.delay(10)

	def growTitle(self):
		self.title_x -= .1
		self.title_y -= .024
		self.title_size_x += .2
		self.title_size_y += .048
		self.window.blit(pygame.transform.scale(self.title, (int(self.title_size_x),int(self.title_size_y))),(self.title_x,self.title_y))

	def moveClouds(self):
		'''
		Defines cloud movement.
		'''
		self.bg_clouds_x += self.bg_clouds_v
		self.fg_clouds_x += self.fg_clouds_v
		self.playMusic()
		self.update()

	def pauseClouds(self):
		self.bg_clouds_v = 0
		self.bg_clouds_x = -WIDTH
		self.bg_clouds_y = 0
		self.fg_clouds_v = 0
		self.fg_clouds_x = -WIDTH
		self.fg_clouds_y = 0

	def playMusic(self):
		'''
		Plays music.
		'''
		if self.music_on:
			pygame.mixer.music.play()
			self.music_on = False			

	def pressAnyKeyToContinue(self):
		'''
		Continue by pressing any key.
		'''
		font = pygame.font.Font("art/font/AnonymousPro-Bold.ttf",24)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN and self.keypress:
				self.bg_clouds_v *= 160
				self.fg_clouds_v *= 80
				self.keypress = False
		if self.keypress:
			if self.fg_clouds_x//10 % 2 == 0:
				self.window.blit(font.render("Press Any Key to Continue",False,(0,0,0)),(160,240))
		else:
			self.title_x += 8

	def shrinkTitle(self):
		'''
		Title shrinks.
		'''
		self.title_x += .1
		self.title_y += .024
		self.title_size_x -= .2
		self.title_size_y -= .048
		self.window.blit(pygame.transform.scale(self.title, (int(self.title_size_x),int(self.title_size_y))),(self.title_x,self.title_y))

	def stopMusic(self):
		'''
		Stops music.
		'''
		pygame.mixer.music.fadeout(3000)

	def titleAnimation(self):
		if self.fg_clouds_x < 175 and self.bg_clouds_x > -WIDTH:	
			if self.fg_clouds_x//25 % 2 == 0:
				self.shrinkTitle()
			else:
				self.growTitle()
			self.pressAnyKeyToContinue()
		if self.bg_clouds_x < -WIDTH:
			self.stopMusic()
			self.pauseClouds()
			self.fadeOut()
			time.sleep(3)
			self.cutscene += 1
			self.bg = pygame.image.load('art/environment/fade.png')
		if self.cutscene == 1:
			for i in range(len(self.text)):
				self.scrollText(i)
			self.cutscene += 1

	def update(self):
		'''
		Updating the menu.
		'''
		self.window.blit(self.bg,(0,0))
		self.window.blit(self.bg_clouds,(self.bg_clouds_x,self.bg_clouds_y))
		self.window.blit(self.fg_clouds,(self.fg_clouds_x,self.fg_clouds_y))
		self.titleAnimation()
		pygame.display.update()