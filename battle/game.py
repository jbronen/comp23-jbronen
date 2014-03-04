# game.py
# Jared Bronen
# Comp 23 - Lab 4

import pygame, os, sys, random
from pygame.locals import *
from random import randint
from Battlecruiser import *
from enemy import *

if __name__ == "__main__":
    if not pygame.font:
        print "Warning, fonts disabled"
    if not pygame.mixer:
        print "Warning, sound disabled"

    FPS = 50
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    MAX_SPEED = 10
    BACKGROUND_IMAGE = "assets/ram_aras.png"

    try:
        background = pygame.image.load(BACKGROUND_IMAGE)
    except pygame.error, message:
        print "Cannot load image: " + BACKGROUND_IMAGE
        raise SystemExit, message

    NUM_ENEMIES = 10

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption("Battle for Ram Aras")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 28)
    score = 0

    enemy_sprites = []
    for i in range(NUM_ENEMIES):
        sprites.append(Enemy(screen, randint(1, SCREEN_WIDTH), randint(1,SCREEN_HEIGHT), randint(1, MAX_SPEED), randint(1, MAX_SPEED)))

    while True:
        time_passed = clock.tick(FPS)
		# Event handling here (to quit)
        for event in pygame.event.get():
       		if event.type == pygame.QUIT:
	       		pygame.quit()
	       		sys.exit()
       		elif event.type == KEYDOWN:
	       		if event.key == K_ESCAPE:
       				pygame.quit()
       				sys.exit()					
		
		# Redraw the background
       	screen.fill(BACKGROUND_COLOR)
		
		# Update and redraw all sprites
       	for sprite in sprites:
       		sprite.update()
       		sprite.draw()
		
		# Draw the sprites
        pygame.display.flip()
