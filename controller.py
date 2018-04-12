import pygame

WIDTH = 640
HEIGHT = 480

class Controller:
	def __init__(self):
		pass

	def playerInput(self,model,view):
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