# enemy.py
# Jared Bronen
# COMP 23 - Lab 4

import pygame, os, sys
from pygame.locals import *
from random import randint


class Enemy(pygame.sprite.Sprite):
    def load_image(self, image_name):
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()
    
    def load_sound(self, sound_name):
        try:
            sound = pygame.mixer.Sound(sound_name)
        except pygame.error, message:
            print "Cannot load sound: " + sound_name
            raise SystemExit, message
        return sound

    def __init__(self, screen, x, y, init_x_speed, init_y_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image("assets/mutalisk.gif")
        self.screen = screen
        self.x = x
        self.y = y
        self.dx = init_x_speed
        self.dy = init_y_speed
        self.rect = self.image.get_rect()
        self.image_w, self.image_h = self.image.get_size()
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)
        self.active = True
        self.exploded = False
        self.points_accounted = False
    
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
    
    def update(self):
        if not self.exploded:
            if ((self.x + self.dx) <= 0):
       		self.dx = self.dx * -1
            if ((self.x + self.dx) >= self.screen.get_size()[0]):
                self.dx = self.dx * -1
            if ((self.y + self.dy) <= 0):
                self.dy = self.dy * -1
            if ((self.y + self.dy) >= self.screen.get_size()[1]):
                self.dy = self.dy * -1
            self.x = self.x + self.dx
            self.y = self.y + self.dy
            self.rect.move(self.x, self.y)
            self.rect.topleft = (self.x, self.y)
            self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

    def die(self):
        self.image = self.load_image("assets/laser_explosion.gif")
        self.exploded = True
        self.active = True

if __name__ == "__main__":
	# Check if sound and font are supported
	if not pygame.font:
		print "Warning, fonts disabled"
	if not pygame.mixer:
		print "Warning, sound disabled"
		
	# Constants
	FPS = 50
	SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
	MAX_SPEED = 10
	BACKGROUND_COLOR = (255, 255, 255)
	NUM_SPRITES = 10
	
	# Initialize Pygame, the clock (for FPS), and a simple counter
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
	pygame.display.set_caption('Enemy.py')
	clock = pygame.time.Clock()
	font = pygame.font.Font(None, 28)
	counter = 0
	
	# Create the sprites; choose random sprite image, starting location, and starting speed for each sprite
	sprites = []
	for i in range(NUM_SPRITES):
		sprites.append(Enemy(screen, randint(1, SCREEN_WIDTH), randint(1,SCREEN_HEIGHT), randint(1, MAX_SPEED), randint(1, MAX_SPEED)))
	
	# Game loop
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
