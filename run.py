from toolBox import *
from mqttFile import *
import pygame
def importerImages():
	for i in range(0,29):
		gifIm = pygame.image.load("./images/"+str(i+1)+".png")
		gif.append(gifIm)
	return

def definitionValeurs():
	global screen, gif, playing, element, horloge
	element = 0
	gif = []
	screen = screen(1280, 720)
	horloge = pygame.time.Clock()
	playing = True
	element =0
	return

def afficherElements():
	global element
	element = element+1
	if element == 29:
		element = 0
	screen.blit(gif[element], (0,0))
	screen.blit(text, (100, 100))
	return

def verificationDuTexte():
	global text
	text = texte(publicMessage, 60, blanc)
	return

## Prog Principal
definitionValeurs()
importerImages()
while playing:
	verificationDuTexte()
	afficherElements()
	clavier = pygame.key.get_pressed()
	if clavier[K_b]==1:
		from mqttFile import *
	getExit()
	pygame.display.update()
	horloge.tick(20)
