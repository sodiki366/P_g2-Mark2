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

canvas = pygame.Surface(screen.get_size())
canvas.fill(BACKGROUND)
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
    # Основная логика игры
    # Отрисовка объектов

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()