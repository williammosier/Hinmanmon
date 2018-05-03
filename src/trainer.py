import pygame


class Trainer:
	def __init__(self,name,file,portrait,dialogue,mon):
		'''
		Defines a trainer.
		'''
		self.name = name
		self.file = file
		self.portrait = portrait
		self.dialogue = dialogue + " "
		self.mon = mon
