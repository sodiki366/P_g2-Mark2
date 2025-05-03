#
import pygame
import random
import os

def draw_tiles():


    for i in range(len(tiles)):
        tile = tiles[i]
        row = i // ROWS
        col = i % COLS
        x = col * (TILE_WIDTH + MARGIN) + MARGIN
        y = row * (TILE_HEIGHT + MARGIN) + MARGIN
        screen.blit(tile,(x,y))

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
ROWS = 10# по вертикали
COLS = 200# по горизонтали
MARGIN = 2#
pygame.init()
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
BACKGROUND = (0,0,0)
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
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            for i in range(len(tiles)):
                tile = tiles[i]
                row = i // ROWS
                col = i % COLS
                x = col * (TILE_WIDTH + MARGIN) + MARGIN
                y = row * (TILE_HEIGHT + MARGIN) + MARGIN

                if x <= mouse_x <= x + TILE_WIDTH and y <= mouse_y <= y + TILE_HEIGHT:
                    print('jhgfkuyt')
                    if selected is not None and selected != i:
                        tiles[i], tiles[selected] = tiles[selected] , tiles[i]
                        selected = None
                        swaps += 1
                    elif selected == i:
                        selected = None
                    else:
                        selected = i
    # Основная логика игры
    # Отрисовка объектов
    screen.fill(BACKGROUND)#очистка экрана

    draw_tiles()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()