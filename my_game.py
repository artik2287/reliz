

import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Визначення кольорів
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Встановлення розміру вікна
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Уникайте метеоритів!")

# Клас космічного корабля
class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x = -5
        if keys[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# Клас метеоритів
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 8)

# Створення списків для всіх спрайтів
all_sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()

# Створення космічного корабля
spaceship = Spaceship()
all_sprites.add(spaceship)

# Створення метеоритів
for i in range(8):
    meteor = Meteor()
    all_sprites.add(meteor)
    meteors.add(meteor)

# Головний цикл гри
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Оновлення
    all_sprites.update()

    # Виявлення зіткнень
    hits = pygame.sprite.spritecollide(spaceship, meteors, False)
    if hits:
        running = False

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Встановлення частоти кадрів
    clock.tick(60)

pygame.quit()

