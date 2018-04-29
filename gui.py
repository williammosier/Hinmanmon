import pygame
import time

COLORS = {
	'black': (0,0,0),
	'navy': (20,20,80),
	'lightgray': (220,220,220),
	'white': (255,255,255),
	'pantone342': (64,112,96),
	'darkgreen': (14,72,56),
	'greygreen': (204,252,236)
}

class GUI:
	def __init__(self,WIDTH,HEIGHT):
		self.window = pygame.display.set_mode((WIDTH,HEIGHT))
		self.HEIGHT = HEIGHT
		self.WIDTH = WIDTH

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
		pygame.draw.rect(self.window,COLORS['darkgreen'],(20,self.HEIGHT-150,600,130),10)
		pygame.draw.rect(self.window,COLORS['greygreen'],(25,self.HEIGHT-145,590,120))
		pygame.draw.rect(self.window,COLORS['darkgreen'],(20,self.HEIGHT-150,470,130),10)
		self.window.blit(trainer.portrait,(495,335))
		self.window.blit(font.render(trainer.name,False,COLORS['black']),(30,340))
		pygame.display.update()

	def fadeIn(self,model):
		image = pygame.image.load("art/environment/fade.png")
		for i in range(0,225,10):
			self.window.blit(model.locs[model.current_loc].file,(model.locs[model.current_loc].x,model.locs[model.current_loc].y))
			self.window.blit(model.player.sprites[model.player.direction][0],(model.player.x,model.player.y))
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

	def redrawBattle(self,state):
		font = pygame.font.Font("art/font/AnonymousPro-Bold.ttf",20)
		if state[2] == "dialogue screen":
			self.window.blit(pygame.image.load('art/environment/battle_screen.jpg'),(0,0))
			#self.dialogue(model.trainers["Al Vos"])
		if state[2] == "choose action":
			self.window.blit(pygame.image.load('art/environment/battle_screen.jpg'),(0,0))
			self.window.blit(font.render("Attack",False,COLORS['black']),(30,360))
			self.window.blit(font.render("Bag",False,COLORS['black']),(320,360))
			self.window.blit(font.render("Mon",False,COLORS['black']),(30,410))
			self.window.blit(font.render("Run",False,COLORS['black']),(320,410))
			pygame.draw.rect(self.window,COLORS['darkgreen'],(30+290*state[4][0],360+50*state[4][1],285,40),2)
		if state[2] == "choose move":
			self.window.blit(pygame.image.load('art/environment/battle_screen.jpg'),(0,0))
			self.window.blit(font.render("Move 1",False,COLORS['black']),(30,360))
			self.window.blit(font.render("Move 2",False,COLORS['black']),(320,360))
			self.window.blit(font.render("Move 3",False,COLORS['black']),(30,410))
			self.window.blit(font.render("Back",False,COLORS['black']),(320,410))
			pygame.draw.rect(self.window,COLORS['darkgreen'],(30+290*state[4][0],360+50*state[4][1],285,40),2)
		self.window.blit(state[1].sprites["backward"][0],(160,280))
		self.window.blit(state[0].portrait,(430,130))
		pygame.display.update()

	def redrawMain(self,model):
		self.window.blit(model.locs[model.current_loc].file,(model.locs[model.current_loc].x,model.locs[model.current_loc].y))
		num = model.player.walkCycle()
		self.window.blit(model.player.sprites[model.player.direction][num],(model.player.x,model.player.y))
		pygame.display.update()