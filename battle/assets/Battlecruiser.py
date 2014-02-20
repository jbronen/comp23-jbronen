# Battlecruiser.py
# Jared Bronen
# Comp 23 - Lab 3

import pygame, os, sys, random
from pygame.locals import *

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
        self.image = self.load_image("battlecruiser.gif")
        self.screen = screen
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.rect = self.image.get_rect()
        self.image_w, self.image_h = self.image.get_size()
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)
        self.active = True
    
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
    
    def update(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)
        
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
        screen.fill(BACKGROUND_COLOR)

        bcruiser.update()
        bcruiser.draw()

        pygame.display.update()
