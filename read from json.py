import json
import jsonpickle
import location
import pygame
pygame.init()
win = pygame.display.set_mode((640,480))

def readFromJSONFile(path, filename):
	filePathNameWExt = './' + path + '/' + filename + '.json'
	with open(filePathNameWExt, 'r') as fp:
		data = fp.read()
		data = jsonpickle.decode(data)
		print(data)
		data = json.load(data)
		win.blit(data["hughes"].file,(0,0))
	fp.close()

path = 'dictionaries'
filename = "locations"

readFromJSONFile(path, filename)