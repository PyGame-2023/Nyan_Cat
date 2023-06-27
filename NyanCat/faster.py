import pygame
import sys
import random

class Star:
    _LINE_LENGTH = 40
    _LINE_WIDTH = 3
    _WHITE = pygame.Color(255, 255, 255)
    _SPEED = 7
    
    def __init__(self, x_position, y_position):
        self._x_position = x_position
        self._y_position = y_position
    
    def update(self):
        self._x_position -= self._SPEED
        if self._x_position < -self._LINE_LENGTH:
            self._x_position = pygame.display.get_surface().get_width()
    
    def draw(self, surface):
        start_pos = (self._x_position, self._y_position)
        end_pos = (self._x_position + self._LINE_LENGTH, self._y_position)
        pygame.draw.line(surface, self._WHITE, start_pos, end_pos, self._LINE_WIDTH)


if __name__ == "__main__":
    pygame.init()
    DISPLAY_SURFACE = pygame.display.set_mode((1400, 800))
    BACKGROUND_COLOR = pygame.Color(0, 0, 0)
    DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
    FPS = 60
    CLOCK = pygame.time.Clock()
    
    stars = []
    max_stars = 20
    
    while True:
        DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
                    
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        while len(stars) < max_stars:
            x_position = random.randint(0, pygame.display.get_surface().get_width())
            y_position = random.randint(0, DISPLAY_SURFACE.get_height())
            star = Star(x_position, y_position)
            stars.append(star)
        
        for star in stars:
            star.draw(DISPLAY_SURFACE)
            star.update()
        
        pygame.display.update()
        CLOCK.tick(FPS)
