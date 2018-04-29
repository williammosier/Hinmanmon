import pygame

class Location:
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

