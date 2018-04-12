import pygame
import random

import controller
import gui
import hinman
import menu

def main():
	pygame.init()
	pygame.mixer.init()
	clock = pygame.time.Clock()
	pygame.display.set_caption("Hinmanmon")

	run = True

	model = hinman.Hinman()
	view = gui.GUI()
	control = controller.Controller()
	splash = menu.SplashScreen(view.window)

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		# while splash.cutscene != 2:
		# 	splash.moveClouds()
		# 	clock.tick(60)

		control.playerInput(model,view)
		view.redraw(model)
		model.encounter()
		model.locationChange(view)
		clock.tick(60)

	pygame.quit()
main()