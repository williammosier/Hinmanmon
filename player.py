import pygame

class Player():
	def __init__(self,sprites,x,y,pmask):
		self.sprites = sprites
		self.x = x
		self.y = y
		self.width = 52
		self.height = 34
		self.velocity = 2
		self.direction = "forward"
		self.mon = []
		self.walk = 0
		self.mask = pmask

	def draw(self,win):
		if self.walk > 39:
			self.walk = 0
		num = self.walk//10
		win.blit(self.sprites[self.direction][num],(self.x,self.y))
		self.walk += 1