#
import pygame
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Risovanie linii")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

point = []

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    #Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            points.append(event.pos)

    # Основная логика игры
    # Отрисовка объектов
    screen.fill(BACKGROUND)#очистка экрана

    for i in range(len(points)-1):
        start_point = points[i]
        end_point = points[1]

        draw.line
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()