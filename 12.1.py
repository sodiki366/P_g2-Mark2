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
                exit()
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
        self.items = ['Играть','Выбрать имя игрока','Выйти']
        #self.text = "Menu"
        self.surface = [font.render(item, True, (255, 255, 255)) for item in self.items]
        self.selected = 0

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_UP:
                    self.prev()
                if event.key == pygame.KEYDOWN:
                    self.next()
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    return self.process_item()
        return self


    def update(self):
        pass

def draw(self, screen):
    screen.fill((0,0,0))

    for i, surface in enumerate(self.surfaces):
        rect = surface.get_rect()
        rect.centerx = screen.get_rect().centerx
        rect.top = screen.get_rect().top +  100 * (i + 1)

    if i == self.selected:
        surface = font.render(self.items[i], True, (255, 0, 0))
    screen.blit(surface, rect)

    def next(self):
        if self.selected < len(self.items) - 1:
            self.selected += 1

    def prev(self):
        if self.selected > 0:
            self.selected -= 1

    def process_item(self):
        if self.selected == 0:
            return Gamescreen()
        if self.selected == 1:
            return Namescreen()
        if self.selected == 2:
            pygame.quit()
            exit()



class Namescreen(State):
    def __init__(self):
        self.text = "Player Name"
        self.surface = font.render(self.text, True, (255, 255, 255))
        self.name = ""
        self.name_surface = None

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(self.name) > 0:
                        self.name = self.name[:-1]
                elif event.key == pygame.K_RETURN:
                    global player_name
                    player_name = self.name
                    return Menuscreen()
                else:
                    if event.unicode.isalnum() and len(self.name) < 10:
                        self.name += event.unicode
                        self.name_surface = font.render(self.name, True, (255, 255, 255))
        return self


    def update(self):
        pass


    def draw(self, screen):
        screen.fill(BACKGROUND)
        rect = self.surface.get_rect()
        rect.centerx = screen.get_rect().centerx
        rect.top = screen.get_rect().top + 100
        screen.blit(self.surface, rect)
        if self.name_surface is not None:
            name_rect = self.name_surface.get_rect()
            name_rect.centerx = screen.get_rect().centerx
            name_rect.top = screen.get_rect().top + 200
            screen.blit(self.name_surface, name_rect)

class Gamescreen(State):
    def __init__(self):
        self.text = "Game"
        self.surface = font.render(self.text, True, (255, 255, 255))
        self.name_surface = font.render(player_name, True, (255,255,255))

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
        rect.centerx = screen.get_rect().centerx
        rect.centery = screen.get_rect().centery
        screen.blit(self.surface, rect)
        name_rect = self.name_surface.get_rect()
        name_rect.left = screen.get_rect().left + 10
        name_rect.top = screen.get_rect().top + 10
        screen.blit(self.name_surface, name_rect)

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