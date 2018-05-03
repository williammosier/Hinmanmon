import pygame
from src import gui
from src import hinman
from src import menu

WIDTH = 640
HEIGHT = 480

class Controller:
	def __init__(self):
		pygame.init()
		pygame.mixer.init()
		self.clock = pygame.time.Clock()
		pygame.display.set_caption("Hinmanmon")

		run = True

		view = gui.GUI(WIDTH,HEIGHT)
		model = hinman.Hinman()
		splash = menu.SplashScreen(view.window)

		while run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

			while splash.cutscene != 2:
				splash.moveClouds()
				self.clock.tick(60)

			self.playerInputMain(model,view)
			view.redrawMain(model)
			encounter = model.encounter()
			if encounter[0]:
				print("encounter")
				battleState = [encounter[1],model.player,"dialogue screen","battle intro",[0,0]]
				while battleState[3] != "finished":
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							run = False
							battleState[3] = "finished"
					battleState = self.playerInputBattle(battleState)
					model.battleCalc(battleState)
					view.redrawBattle(battleState)
					self.clock.tick(60)
			model.locationChange(view)
			self.clock.tick(60)

		pygame.quit()

	def playerInputBattle(self,state):
		keys = pygame.key.get_pressed()
		if state[2] == "choose action" or state[2] == "choose move":
			if keys[pygame.K_a]:
				state[4][0] = 0
			if keys[pygame.K_d]:
				state[4][0] = 1
			if keys[pygame.K_w]:
				state[4][1] = 0
			if keys[pygame.K_s]:
				state[4][1] = 1
			if keys[pygame.K_q]:
				state[3] = "finished"

		if keys[pygame.K_e] and state[2] == "dialogue screen":
			state[2] = "choose action"
		if keys[pygame.K_e] and state[2] == "choose action" and state[4] == [1,1]:
			state[3] = "finished"
		if keys[pygame.K_e] and state[2] == "choose action" and state[4] == [0,0]:
			state[2] = "choose move"
		if keys[pygame.K_e] and state[2] == "choose move" and state[4] != [1,1]:
			print(state[4][0] + 2*state[4][1])
		if keys[pygame.K_e] and state[2] == "choose move" and state[4] == [1,1]:
			state[2] = "choose action"
		keys = []

		return state

	def playerInputMain(self,model,view):
		keys = pygame.key.get_pressed()
		offset = (model.player.x - model.locs[model.current_loc].x, model.player.y - model.locs[model.current_loc].y)
		result = model.locs[model.current_loc].mask.overlap(model.player.mask,offset)
		buttons_pressed = len([i for i in keys if i != 0])

		if model.isNotCollided(model.player.x,model.player.y):
			pygame.display.set_caption("HIT"+" locx: "+str(model.locs[model.current_loc].x)+" locy: "+str(model.locs[model.current_loc].y))
		else:
			pygame.display.set_caption("NO HIT"+" locx: "+str(model.locs[model.current_loc].x)+" locy: "+str(model.locs[model.current_loc].y))

		if buttons_pressed < 3:
			if keys[pygame.K_w] and model.player.y > 0 and model.isNotCollided(model.player.x,model.player.y-model.player.velocity):
				model.moveUp()
			if keys[pygame.K_s] and model.player.y < HEIGHT - model.player.height and model.isNotCollided(model.player.x,model.player.y+model.player.velocity):
				model.moveDown()
			if keys[pygame.K_a] and model.player.x > 0 and model.isNotCollided(model.player.x-model.player.velocity,model.player.y):
				model.moveLeft()
			if keys[pygame.K_d] and model.player.x < WIDTH + model.player.width and model.isNotCollided(model.player.x+model.player.velocity,model.player.y):
				model.moveRight()

		if not(keys[pygame.K_a]) and not(keys[pygame.K_d]) and not(keys[pygame.K_w]) and not(keys[pygame.K_s]) or (keys[pygame.K_w] and keys[pygame.K_s] or keys[pygame.K_a] and keys[pygame.K_d]):
			model.player.walk = 0

		if keys[pygame.K_e]:
			model.interact(view,model)

		if keys[pygame.K_b] and model.player.velocity == 2:
			model.player.velocity = 8
		elif keys[pygame.K_b] and model.player.velocity == 8:
			model.player.velocity = 2