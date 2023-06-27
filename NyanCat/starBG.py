import pygame
import sys
import random
from data import star_frames

class Star:
    _PIXEL_WIDE = 9
    _PIXEL_HIGH = 9
    _WHITE = pygame.Color('White')
    
    def __init__(self, cellSize, speed):
        self._rect = pygame.Rect(0, 0, self.__class__._PIXEL_WIDE * cellSize[0], self.__class__._PIXEL_HIGH * cellSize[1])
        self._tileWidth = 0.0
        self._tileHight = 0.0
        self._frames = star_frames.frames
        self._currentFrame = random.randint(0, len(self._frames) - 1)
        self._configureSize()
        self._speed = speed
        self._frameCounter = 0
    
    def _configureSize(self):
        self._tileWidth = self._rect.width / float(self.__class__._PIXEL_WIDE)
        self._tileHight = self._rect.height / float(self.__class__._PIXEL_HIGH)
    
    def update(self):
        self._frameCounter += 1
        if self._frameCounter >= self._speed:
            self._frameCounter = 0
            self._currentFrame += 1
            if self._currentFrame >= len(self._frames):
                self._currentFrame = 0

        self._rect.move_ip(-3, 0)

        if self._rect.right < 0:
            self._rect.left = pygame.display.get_surface().get_width()
    
    def draw(self, surface):
        offsetX = self._rect.left
        offsetY = self._rect.top
        w = round(self._tileWidth)
        h = round(self._tileHight)
        stroke = 0
        if w <= 1 or h <= 1:
            stroke = 1
        for pos in self._frames[self._currentFrame]:
            x = round(offsetX + self._tileWidth * pos[0])
            y = round(offsetY + self._tileHight * pos[1])
            pygame.draw.rect(surface, self.__class__._WHITE, pygame.Rect(int(x), int(y), int(w), int(h)), stroke)
    
    def rect(self):
        return self._rect
    rect = property(rect, None, None, None)
    
    def getCurrentFrame(self):
        return self._currentFrame
    
    def setCurrentFrame(self, value):
        self._currentFrame = value
    currentFrame = property(getCurrentFrame, setCurrentFrame, None, None)


if __name__ == "__main__":
    pygame.init()
    DISPLAY_SURFACE = pygame.display.set_mode((1400, 800))
    BACKGROUND_COLOR = pygame.Color(0, 0, 0)
    DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
    FPS = 30
    CLOCK = pygame.time.Clock()
    
    stars = []
    for _ in range(20):  # Adjust the number of stars here
        speed = 10
        star = Star((3, 3), speed)
        star.rect.center = (
            random.randint(0, DISPLAY_SURFACE.get_width()),
            random.randint(0, DISPLAY_SURFACE.get_height())
        )
        stars.append(star)
    
    while True:
        DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
                    
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        for star in stars:
            star.draw(DISPLAY_SURFACE)
            star.update()
        
        pygame.display.update()
        CLOCK.tick(FPS)
