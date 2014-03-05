# game.py
# Jared Bronen
# Comp 23 - Lab 4

import pygame, os, sys, random
from pygame.locals import *
from random import randint
from Battlecruiser import *
from enemy import *

class ScrollingBackground(pygame.sprite.Sprite):
    def __init__(self, screen, scroll_speed):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.scrolling = True
        
        try:
            self.image = pygame.image.load("assets/ram_aras.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.image_w, self.image_h = self.image.get_size()
            self.screen_w = self.screen.get_size()[0]
            self.screen_h = self.screen.get_size()[1]
            self.x = 0
            self.y = 0
            self.dx = scroll_speed
        except pygame.error, message:
            print "Cannot load background image"
            raise SystemExit, message
        
    def update(self):
        if ((self.x * -1) > self.image_w - self.screen_w) and self.scrolling == True:
                self.scrolling = False
        else:
                self.x -= self.dx

    def draw(self):
        if self.scrolling == True:
            draw_pos = self.image.get_rect().move(self.x, self.y)
            self.screen.blit(self.image, draw_pos)



def render_game_over(screen):
    font = pygame.font.Font(None, 72)
    game_over = font.render("GAME OVER",1,(0,0,0))
    screen.blit(game_over,(100,100))




if __name__ == "__main__":
    if not pygame.font:
        print "Warning, fonts disabled"
    if not pygame.mixer:
        print "Warning, sound disabled"

    FPS = 50
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    MAX_SPEED = 3
    NUM_ENEMIES = 5

    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Battle for Ram Aras")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 28)
    score = 0
    player = Battlecruiser(screen, 400, 400)

    enemy_sprites = []
    for i in range(NUM_ENEMIES):
        enemy_sprites.append(Enemy(screen, randint(1, SCREEN_WIDTH), randint(1,SCREEN_HEIGHT/2), randint(1, MAX_SPEED), randint(1, MAX_SPEED)))
    
    BACKGROUND_COLOR = (255, 255, 255)
    background = ScrollingBackground(screen, 0)
    points = 0


while True:
        time_passed = clock.tick(FPS)
        point_font = pygame.font.Font(None, 72)

		# Event handling here (to quit)
        for event in pygame.event.get():
       		if event.type == pygame.QUIT:
	       		pygame.quit()
	       		sys.exit()
       		elif event.type == KEYDOWN:
	       		if event.key == K_ESCAPE:
       				pygame.quit()
       				sys.exit()
                        if event.key == K_RIGHT:
                            player.x = player.x + 30
                        if event.key == K_LEFT:
                            player.x = player.x - 30
                        if event.key == K_UP:
                            player.y = player.y - 30
                        if event.key == K_DOWN:
                            player.y = player.y + 30
                        if event.key == K_SPACE:
                            player.fire()

		# Redraw the background
       	screen.fill(BACKGROUND_COLOR)
        player.update()
        if player.active:
            background.update()
            background.draw()
            player.draw()
            player.lasers.update()
            player.lasers.draw(screen)
		# Update and redraw all sprites
            for sprite in enemy_sprites:
                if pygame.sprite.collide_rect(sprite, player):
                    if sprite.active:
                        player.load_sound("assets/death_explode.wav")
                        player.active = False
                if pygame.sprite.spritecollideany(sprite, player.lasers):
                    sprite.die()
                    if not sprite.points_accounted:
                        points = points + 100
                    sprite.points_accounted = True
                if sprite.active:
                    sprite.update()
                    sprite.draw()
        if not player.active:
            render_game_over(screen)
		# Draw the sprites
        point_display = font.render(str(points), 1, (255,255,255))
        screen.blit(point_display,(700,50))
        pygame.display.update()
