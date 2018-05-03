import json
import jsonpickle
import location
import pygame
pygame.init()
pygame.display.set_mode((640,480))

def writeToJSONFile(path, filename, data):
	filePathNameWExt = './' + path + '/' + filename + '.json'
	data = jsonpickle.encode(data)
	with open(filePathNameWExt, 'w') as fp:
		json.dump(data, fp)
	fp.close()

path = 'dictionaries'
filename = "locations"
data = {
	"hinman college":\
	location.Location(pygame.image.load('art/environment/hinman_college.png'),\
	pygame.image.load('art/environment/hinman_college_mask.png').convert_alpha(),\
	pygame.image.load('art/environment/hinman_college_loadzones.png'),\
	'sound/music/death.ogg',-1900,-1200,3000,3000),

	"success center":\
	location.Location(pygame.image.load('art/environment/success_center.png'),\
	pygame.image.load('art/environment/success_center_mask.png').convert_alpha(),\
	pygame.image.load('art/environment/success_center_loadzones.png'),\
	'sound/music/reslife.ogg',0,0,640,480),

	"hughes":\
	location.Location(pygame.image.load('art/environment/hughes.png'),\
	pygame.image.load('art/environment/hughes_mask.png').convert_alpha(),\
	pygame.image.load('art/environment/hughes_loadzones.png'),\
	'sound/music/reslife.ogg',0,0,2000,500),

	"cleveland":\
	location.Location(pygame.image.load('art/environment/cleveland.png'),\
	pygame.image.load('art/environment/cleveland_mask.png').convert_alpha(),\
	pygame.image.load('art/environment/cleveland_loadzones.png'),\
	'sound/music/reslife.ogg',0,0,2000,500),

	"lehman":\
	location.Location(pygame.image.load('art/environment/lehman.png'),\
	pygame.image.load('art/environment/lehman_mask.png').convert_alpha(),\
	pygame.image.load('art/environment/lehman_loadzones.png'),\
	'sound/music/reslife.ogg',0,0,2000,500),

	"roosevelt":\
	location.Location(pygame.image.load('art/environment/roosevelt.png'),\
	pygame.image.load('art/environment/roosevelt_mask.png').convert_alpha(),\
	pygame.image.load('art/environment/roosevelt_loadzones.png'),\
	'sound/music/reslife.ogg',0,0,2000,500),

	"smith":\
	location.Location(pygame.image.load('art/environment/smith.png'),\
	pygame.image.load('art/environment/smith_mask.png').convert_alpha(),\
	pygame.image.load('art/environment/smith_loadzones.png'),\
	'sound/music/reslife.ogg',0,0,2000,500)
	}

writeToJSONFile(path, filename, data)