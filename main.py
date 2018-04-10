import pygame
import time
import hinman
import menu


def main():
	pygame.init()
	pygame.mixer.init()
	clock = pygame.time.Clock()
	pygame.display.set_caption("Hinmanmon")

	game = hinman.Hinman()

	intro = True
	run = True

	game = hinman.Hinman()
	splash = menu.SplashScreen(game.window)

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		while splash.cutscene != 2:
			splash.moveClouds()
			clock.tick(60)

		game.playerInput()
		game.redraw()
		game.encounter()
		game.locationChange()
		clock.tick(60)

	pygame.quit()
main()
