import json
import jsonpickle
from src import location
import pygame
pygame.init()
pygame.display.set_mode((640,480))

def readFromJSONFile(path, filename):
	filePathNameWExt = './' + path + '/' + filename + '.json'
	with open(filePathNameWExt, 'r') as fp:
		data = json.loads(fp)
		data = jsonpickle.decode(data)
		print(data)

path = 'dictionaries'
filename = "locations"

readFromJSONFile(path, filename)