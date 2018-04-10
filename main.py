import pygame
import random
import time
import Hinman
import Hmon
import location
import player
import trainer

#sets the possible moves for Hinmanmon
MOVES = ()

def main():
	pygame.init()
	pygame.mixer.init()
	run = True

	pygame.display.set_caption("Hinmanmon")

	game = Hinman.Hinman()

	while run:
		pygame.time.delay(50)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		game.playerInput()
		game.redraw()
		game.locationChange()
	pygame.quit()
main()