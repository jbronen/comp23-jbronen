# Battlecruiser.py
# Jared Bronen
# Comp 23 - Lab 3

import pygame, os, sys, random 
from pygame.locals import *
from random import randint

class Battlecruiser(pygame.sprite.Sprite):
    def load_image(self, image_name):
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()
    
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image("/assets/battlecruiser.gif")
        self.screen = screen
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.lasers = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.image_w, self.image_h = self.image.get_size()
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)
        self.active = True

    def fire(self):
        new_laser = Laser(self.x + 50, self.y, -10)
        self.lasers.add(new_laser)
    
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
    
    def update(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

class Laser(pygame.sprite.Sprite):
	''' A simple sprite that bounces off the walls '''
	
	def load_image(self, image_name):
		''' The proper way to load an image '''
		try:
			image = pygame.image.load(image_name)
		except pygame.error, message:
			print "Cannot load image: " + image_name
			raise SystemExit, message
		return image.convert_alpha()

	def __init__(self, init_x, init_y, init_y_speed):
		''' Create the LaserBolt at (x, y) moving up at a given speed '''
		pygame.sprite.Sprite.__init__(self) #call Sprite intializer
		
		# Load the image
		self.image = self.load_image('laser.gif')

		# Create a moving collision box
		self.rect = self.image.get_rect()
		self.rect.x = init_x
		self.rect.y = init_y
				
		# Set the default speed (dx, dy)
		self.dy = init_y_speed
				
	def update(self):
		''' Move the sprite '''
		self.rect.y += self.dy
		self.rect.move(self.rect.x, self.rect.y)
		
		# Remove sprite from group if it goes off the screen...
		if self.rect.y <= 0:
			self.kill() # see http://pygame.org/docs/ref/sprite.html#Sprite.kill

        
if __name__ == "__main__":
    if not pygame.font:
        print "warning, fonts disabled"
    if not pygame.mixer:
        print "warning, sounds disabled"
    
    FPS = 50
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    BACKGROUND_COLOR = (0, 0, 0)

    pygame.init()
    pygame.display.set_caption('Battlecruiser')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    clock = pygame.time.Clock()
    bcruiser = Battlecruiser(screen, 10, 10)

    while True:
        time_passed = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RIGHT:
                    bcruiser.x = bcruiser.x + 10
                if event.key == K_LEFT:
                    bcruiser.x = bcruiser.x - 10
                if event.key == K_UP:
                    bcruiser.y = bcruiser.y - 10
                if event.key == K_DOWN:
                    bcruiser.y = bcruiser.y + 10
                if event.key == K_SPACE:
                    bcruiser.fire()
        screen.fill(BACKGROUND_COLOR)

        bcruiser.update()
        bcruiser.lasers.update()
        bcruiser.draw()
        bcruiser.lasers.draw(screen)

        pygame.display.update()
