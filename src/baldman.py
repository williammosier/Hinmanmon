import pygame
from src import hinmanmon

class Baldman(hinmanmon.Hinmanmon):
	def __init__(self):
		'''
		Creates Baldman.
		'''
		super().__init__()
		self.name = "baldman"
		self.type = "Harpur"
		self.portrait = pygame.image.load('art/sprites/standing.png')