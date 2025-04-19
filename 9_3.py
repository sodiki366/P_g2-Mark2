#
from all_colors import *
import pygame
pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RISOVALKA")
BACKGROUND = (255, 255, 255)
brush_color = (0,0,0)
brush_width = 5

BORDER_COLOR = (0,0,0)
CUR_INDEX = 0

canvas = pygame.Surface(screen.get_size())
canvas.fill(BACKGROUND)

size = 50
palette_rect = pygame.Rect(10,10, size * 12, size)
palette = pygame.Surface(palette_rect.size)
palette.fill(BORDER_COLOR)

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    #Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()

    pygame.draw.circle(canvas, brush_color, mouse_pos, brush_width)


    screen.blit(canvas,(0,0))
    screen.blit(palette, (0,0))
    # Основная логика игры
    # Отрисовка объектов

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()