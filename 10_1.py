#
import pygame
import random
import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
ROWS = 3# по вертикали
COLS = 2# по горизонтали
MARGIN = 2#
pygame.init()
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
FPS = 60
clock = pygame.time.Clock()

pictures = os.listdir('pictures')
picture = random.choice(pictures)
image = pygame.image.load('pictures/' + picture)

image_width, image_height = image.get_size()
TILE_WIDTH = image_width // COLS
TILE_HEIGHT = image_height // ROWS

tiles = []
for i in range(ROWS):
    for j in range(COLS):
        rect = pygame.Rect(j * TILE_WIDTH,
                           i * TILE_HEIGHT,
                           TILE_WIDTH,
                           TILE_HEIGHT)
        tile = image.subsurface(rect)#поверхность под поверхностью
        tiles.append(tile)

origin_tiles = tiles.copy()
random.shuffle(tiles)#перемешиваем список фргментов
selected = None
swaps = 0

running = True
while running:
    #Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Основная логика игры
    # Отрисовка объектов
    screen.fill(BACKGROUND)#очистка экрана
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()