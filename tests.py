import pygame
import hinmanmon
import player
import hinman
import location
import baldman
import trainer

def test_hinmanmon():
	print("##Testing Hinmanmon Model##")
	test = hinmanmon.Hinmanmon()
	assert test.status == "normal"
	assert test.hp == 10

def test_controller():

def test_menu():

def test_hinman():
	print("##Testing Hinman Model##")

def test_Baldman():
	print("##Testing Baldman Model##")
	test = baldman.Baldman()
	assert test.name == "baldman"
	assert test.type == "Harpur"

def test_trainer():
	print("##Testing Trainer Model##")

def main():
	test_hinmanmon()
	test_hinman()
	test_Baldman()

main()



	