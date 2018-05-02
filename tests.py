import pygame
import time
from src import hinmanmon
from src import player
from src import hinman
from src import location
from src import baldman
from src import trainer
from src import menu
from src import gui

def test_hinmanmon():
	print("##Testing Hinmanmon Model##")
	test = hinmanmon.Hinmanmon()
	assert test.status == "normal"
	assert test.hp == 10

def test_menu():
	print("##Testing Menu Model##")
	pygame.init()
	pygame.mixer.init()
	WIDTH = 640
	HEIGHT = 480
	window = gui.GUI(WIDTH,HEIGHT)
	test_menu = menu.SplashScreen(window)
	test_menu.pauseClouds()
	assert test_menu.bg_clouds_v == 0
	assert test_menu.bg_clouds_x == -WIDTH
	assert test_menu.bg_clouds_y == 0
	assert test_menu.fg_clouds_v == 0
	assert test_menu.fg_clouds_x == -WIDTH
	assert test_menu.fg_clouds_y == 0

def test_hinman():
	print("##Testing Hinman Model##")
	test_hinman = hinman.Hinman()
	WIDTH = 640
	HEIGHT = 480
	window = gui.GUI(WIDTH,HEIGHT)
	test_hinman.current_loc = "cleveland"
	assert test_hinman.isNotCollided(960, 300) == True

def test_Baldman():
	print("##Testing Baldman Model##")
	test = baldman.Baldman()
	assert test.name == "baldman"
	assert test.type == "Harpur"

def test_trainer():
	print("##Testing Trainer Model##")
	trainee = trainer.Trainer(\
			"Social VP Isaac and Abby",None,pygame.image.load('art/character_portraits/smith_social.png'),\
			"Testing",())
	assert trainee.name == "Social VP Isaac and Abby"
	assert trainee.file == None
	assert trainee.portrait == pygame.image.load('art/character_portraits/smith_social.png')
	assert trainee.dialogue == "Testing" + " "

def main():
	test_hinmanmon()
	test_hinman()
	test_Baldman()
	test_menu()

main()