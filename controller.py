import pygame
import gui
import hinman
import menu

WIDTH = 640
HEIGHT = 480

class Controller:
	def __init__(self):
		pygame.init()
		pygame.mixer.init()
		clock = pygame.time.Clock()
		pygame.display.set_caption("Hinmanmon")

		run = True

		view = gui.GUI(WIDTH,HEIGHT)
		model = hinman.Hinman()
		splash = menu.SplashScreen(view.window)

		while run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

			# while splash.cutscene != 2:
			# 	splash.moveClouds()
			# 	clock.tick(60)

			self.playerInputMain(model,view)
			view.redrawMain(model)
			encounter = model.encounter()
			if encounter[0]:
				battleState = [encounter[1],model.player,"dialogue screen","battle intro"]
				self.playerInputBattle(battleState)
				model.battleCalc(battleState)
				view.redrawBattle(battleState)
			model.locationChange(view)
			clock.tick(60)

		pygame.quit()

	def playerInputBattle(self,state):
		keys = pygame.key.get_pressed()
		if state[2] == "dialogue screen":
			pass
		if state[2] == "choose action":
			pass

	def playerInputMain(self,model,view):
		keys = pygame.key.get_pressed()
		offset = (model.player.x - model.locs[model.current_loc].x,model.player.y - model.locs[model.current_loc].y)
		result = model.locs[model.current_loc].mask.overlap(model.player.mask,offset)

		if model.isNotCollided(model.player.x,model.player.y):
			pygame.display.set_caption("HIT"+" locx: "+str(model.locs[model.current_loc].x)+" locy: "+str(model.locs[model.current_loc].y))
		else:
			pygame.display.set_caption("NO HIT"+" locx: "+str(model.locs[model.current_loc].x)+" locy: "+str(model.locs[model.current_loc].y))

		if keys[pygame.K_w] and model.player.y > 0 and model.isNotCollided(model.player.x,model.player.y-model.player.velocity):
			model.moveUp()
		if keys[pygame.K_s] and model.player.y < HEIGHT - model.player.height and model.isNotCollided(model.player.x,model.player.y+model.player.velocity):
			model.moveDown()
		if keys[pygame.K_a] and model.player.x > 0 and model.isNotCollided(model.player.x-model.player.velocity,model.player.y):
			model.moveLeft()
		if keys[pygame.K_d] and model.player.x < WIDTH + model.player.width and model.isNotCollided(model.player.x+model.player.velocity,model.player.y):
			model.moveRight()

		if not(keys[pygame.K_a]) and not(keys[pygame.K_d]) and not(keys[pygame.K_w]) and not(keys[pygame.K_s]):
			model.player.walk = 0

		if keys[pygame.K_e]:
			model.interact(view)

		if keys[pygame.K_b] and model.player.velocity == 5:
			model.player.velocity *= 2
		elif keys[pygame.K_b] and model.player.velocity == 10:
			model.player.velocity /= 2