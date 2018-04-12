import pygame

WIDTH = 640
HEIGHT = 480

class Controller:
	def __init__(self):
		pass

	def moveLeft(self,model):
		if model.locs[model.current_loc].x == 0 or model.player.x >= WIDTH//2 - model.player.width//2:
			model.player.x -= model.player.velocity
		else:
			model.locs[model.current_loc].x += model.player.velocity
		model.player.direction = "left"

	def moveRight(self,model):
		if model.locs[model.current_loc].x == -model.locs[model.current_loc].width + WIDTH or model.player.x < WIDTH//2 - model.player.width//2:
			model.player.x += model.player.velocity
		else:
			model.locs[model.current_loc].x -= model.player.velocity
		model.player.direction = "right"

	def moveUp(self,model):
		if model.locs[model.current_loc].y == 0 or model.player.y >= HEIGHT//2 - model.player.height//2:
			model.player.y -= model.player.velocity
		else:
			model.locs[model.current_loc].y += model.player.velocity
		model.player.direction = "backward"

	def moveDown(self,model):
		if model.locs[model.current_loc].y == -model.locs[model.current_loc].height + HEIGHT or model.player.y < HEIGHT//2 - model.player.height//2:
			model.player.y += model.player.velocity
		else:
			model.locs[model.current_loc].y -= model.player.velocity
		model.player.direction = "forward"

	def playerInput(self,model,view):
		keys = pygame.key.get_pressed()
		offset = (model.player.x - model.locs[model.current_loc].x,model.player.y - model.locs[model.current_loc].y)
		result = model.locs[model.current_loc].mask.overlap(model.player.mask,offset)

		if model.isNotCollided(model.player.x,model.player.y):
			pygame.display.set_caption("HIT"+" locx: "+str(model.locs[model.current_loc].x)+" locy: "+str(model.locs[model.current_loc].y))
		else:
			pygame.display.set_caption("NO HIT"+" locx: "+str(model.locs[model.current_loc].x)+" locy: "+str(model.locs[model.current_loc].y))

		if keys[pygame.K_w] and model.player.y > 0 and model.isNotCollided(model.player.x,model.player.y-model.player.velocity):
			self.moveUp(model)
		if keys[pygame.K_s] and model.player.y < HEIGHT - model.player.height and model.isNotCollided(model.player.x,model.player.y+model.player.velocity):
			self.moveDown(model)
		if keys[pygame.K_a] and model.player.x > 0 and model.isNotCollided(model.player.x-model.player.velocity,model.player.y):
			self.moveLeft(model)
		if keys[pygame.K_d] and model.player.x < WIDTH + model.player.width and model.isNotCollided(model.player.x+model.player.velocity,model.player.y):
			self.moveRight(model)

		if not(keys[pygame.K_a]) and not(keys[pygame.K_d]) and not(keys[pygame.K_w]) and not(keys[pygame.K_s]):
			model.player.walk = 0

		if keys[pygame.K_e]:
			model.interact(view)

		if keys[pygame.K_b] and model.player.velocity == 5:
			model.player.velocity *= 2
		elif keys[pygame.K_b] and model.player.velocity == 10:
			model.player.velocity /= 2