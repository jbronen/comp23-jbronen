# enemy.py
# Jared Bronen
# COMP 23 - Lab 4

class Enemy(pygame.sprite.Sprite):
    def load_image(self, image_name):
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()
    
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image("mutalisk.gif")
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
        self.thePlayer = Battlecruiser(screen, 10, 10)
    
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
    
    def update(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

    def die(self):
        self.load_image("laser_explosion.gif")
        self.active = False
