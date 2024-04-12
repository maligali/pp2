import pygame
import sys # Library to use font
from pygame.locals import * # To use files
import random, time

# Initialzing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Color palette
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Important values
width = 400
height = 600
speed = 5
score = 0
score2 = 0

# Background music
pygame.mixer.Sound('bgsound.wav').play()

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Times New Roman", 20)
game_over = font.render("Game Over", True, black)

background = pygame.image.load("AnimatedStreet.png")

# Creating a display
screen = pygame.display.set_mode((400, 600))
screen.fill(white)
# Caption
pygame.display.set_caption("Racer Game")

# Sprites, creating Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 100)) # Size of enemy
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0) # To make enemy appear out of nowhere
# To make move
    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        global score2
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)

# creating Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 500)

# Main function
while True:

    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.5
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    scores = font_small.render(str(score), True, black)
    coinscore = font_small.render("Coins: " + str(score2), True, black)
    screen.blit(scores, (10, 10))
    screen.blit(coinscore, (width - 200, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        screen.fill(red)
        screen.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Check for collision with coins
    coin_collisions = pygame.sprite.spritecollide(P1, coins, True)
    for coin in coin_collisions:
        score2 += 1

    pygame.display.update()
    FramePerSec.tick(FPS)