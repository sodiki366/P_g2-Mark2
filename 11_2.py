#
import pygame
import sys
import abc

from pygame.constants import KEYDOWN


class State(abc.ABC):
    @abc.abstractmethod
    def handle_events(self, canvas):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def draw(self, screen):
        pass

class SplashScreen(State):
    def __init__(self):
        self.text = "Zastavka"
        self.surface = font.render(self.text, True, (255, 255, 255))
        self.hint = "Нажмите для продолжения"
        self.hint_surface = font.render(self.hint, True, (255, 255, 255))
        self.hint_visible = True
        self.hint_time  =pygame.time.get_ticks()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return Menuscreen()

        return self


    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.hint_time > 800:
            self.hint_visible = not self.hint_visible
            self.hint_time = current_time


    def draw(self, screen):
        screen.fill(BACKGROUND)
        rect = self.surface.get_rect()
        # rect.center = (size[0] // 2, size[1] // 2)
        rect.centerx = screen.get_rect().centerx
        rect.centery = screen.get_rect().centery - 100
        screen.blit(self.surface, rect)

        if self.hint_visible:
            hint_rect = self.hint_surface.get_rect()
            hint_rect.centerx = screen.get_rect().centerx
            hint_rect.centery = screen.get_rect().centery + 100
            screen.blit(self.hint_surface, hint_rect)

class Menuscreen(State):
    def __init__(self):
        self.text = "Menu"
        self.surface = font.render(self.text, True, (255, 255, 255))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return SplashScreen()
        return self


    def update(self):
        pass


    def draw(self, screen):
        screen.fill(BACKGROUND)
        rect = self.surface.get_rect()
        rect.center = (size[0] // 2, size[1] // 2)
        screen.blit(self.surface, rect)

class Namescreen(State):
    def __init__(self):
        self.text = "Player Name"
        self.surface = font.render(self.text, True, (255, 255, 255))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return Menuscreen()
        return self


    def update(self):
        pass


    def draw(self, screen):
        screen.fill(BACKGROUND)
        rect = self.surface.get_rect()
        rect.center = (size[0] // 2, size[1] // 2)
        screen.blit(self.surface, rect)

class Gamescreen(State):
    def __init__(self):
        self.text = "Game"
        self.surface = font.render(self.text, True, (255, 255, 255))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return Namescreen()
        return self


    def update(self):
        pass


    def draw(self, screen):
        screen.fill(BACKGROUND)
        rect = self.surface.get_rect()
        rect.center = (size[0] // 2, size[1] // 2)
        screen.blit(self.surface, rect)

pygame.init()
pygame.font.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
BACKGROUND = (0, 0, 0)
screen.fill(BACKGROUND)
FPS = 60
clock = pygame.time.Clock()

player_name = "Anonim Tusk"
font = pygame.font.SysFont(None, 64)

# state = SplashScreen()
state = SplashScreen()
while True:
    events = pygame.event.get()
    state = state.handle_events(events)
    state.update()
    state.draw(screen)


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()