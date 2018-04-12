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

	def walkCycle(self):
		if self.walk > 38:
			self.walk = 0
		self.walk += 1
		return self.walk//10