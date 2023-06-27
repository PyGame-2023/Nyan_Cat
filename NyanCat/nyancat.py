# Copyright 2012 Hajime Hikida
# Licensed under the Apache License 2.0

import sys
import pygame
from data import nyancat_frame1
from data import nyancat_frame2
from data import nyancat_frame3
from data import nyancat_frame4
from data import nyancat_frame5
from data import nyancat_frame6

class Nyancat:
	#Pixel wide for the original image.
	_PIXEL_WIDE = 35
	
	#Pixel high for the original image.
	_PIXEL_HIGH = 25
	
	#Pixel colors
	_WHITE 	= pygame.Color(255, 255, 255)	#FFFFFF
	_BLACK 	= pygame.Color(0, 0, 0)			#000000
	_GRAY 	= pygame.Color(153, 153, 153)	#999999
	_PINK1 	= pygame.Color(255, 204, 153)	#FFCC99
	_PINK2 	= pygame.Color(255, 153, 255)	#FF99FF
	_PINK3 	= pygame.Color(255, 51, 153)	#FF3399
	_PINK4 	= pygame.Color(255, 153, 153)	#FF9999
	
	def __init__(self, rect=pygame.Rect(0, 0, _PIXEL_WIDE, _PIXEL_HIGH)):
		#Rectangle area of the cat image (subject to change).
		self._rect = rect
		
		#Width of a pixelerated area of the image (i.e., dots' width)
		self._tileWidth = 0.0
		
		#height of a pixelerated area of the image (i.e., dots' height)
		self._tileHeight = 0.0
		
		#Animation frames from external modules.
		self._frames = (
						nyancat_frame1.pixeldata,
						nyancat_frame2.pixeldata,
						nyancat_frame3.pixeldata,
						nyancat_frame4.pixeldata,
						nyancat_frame5.pixeldata,
						nyancat_frame6.pixeldata)
		
		#Index of the current animation frame.
		self._currentFrame = 0
		
		self._configureSize()
	
	#Private method. Calculate the maximum image size in a given rectangle area without breaking the image's aspect ratio.
	def _configureSize(self):
		w = self._rect.width
		h = self._rect.height
		
		if (w <= h):
			imageWidth = w
			imageHeight = w * self.__class__._PIXEL_HIGH / float(self.__class__._PIXEL_WIDE)
		else:
			imageWidth = h * self.__class__._PIXEL_WIDE / float(self.__class__._PIXEL_HIGH)
			imageHeight = h
		
		#Make sure the image size is always smaller than the rectangle.
		if imageWidth > self._rect.width or imageHeight > self._rect.height:
			raise ArithmeticError
		
		self._tileWidth = imageWidth / float(self.__class__._PIXEL_WIDE)
		self._tileHeight = imageHeight / float(self.__class__._PIXEL_HIGH)
		
		#Set a newer size.
		self._rect.size = (int(round(imageWidth)), int(round(imageHeight)))
	
	#Set the next animation frame.
	def update(self):
		self._currentFrame += 1

		if (self._currentFrame > len(self._frames) - 1):
			self._currentFrame = 0
	
	#Draw pixel data on the surface.
	def draw(self, surface):
		self._draw(surface, self._frames[self._currentFrame][0], self.__class__._WHITE)
		self._draw(surface, self._frames[self._currentFrame][1], self.__class__._BLACK)
		self._draw(surface, self._frames[self._currentFrame][2], self.__class__._GRAY)
		self._draw(surface, self._frames[self._currentFrame][3], self.__class__._PINK1)
		self._draw(surface, self._frames[self._currentFrame][4], self.__class__._PINK2)
		self._draw(surface, self._frames[self._currentFrame][5], self.__class__._PINK3)
		self._draw(surface, self._frames[self._currentFrame][6], self.__class__._PINK4)
		
	#Private method. Fill rectangles with a given color on the surface object.
	def _draw(self, surface, positions, color):
		offsetX = self._rect.left;
		offsetY = self._rect.top;
		
		#Fill each rectangle area specified by a position array.
		for pos in positions:
			#No stroke by default (i.e., fill the rectangle).
			stroke = 0
					
			x = round(offsetX + pos[0] * self._tileWidth)
			y = round(offsetY + pos[1] * self._tileHeight)
			w = round(self._tileWidth)
			h = round(self._tileHeight)
					
			#If the rectangle is too small to be filled, stroke it.
			if w <= 1 or h <= 1:
				stroke = 1
						
			rect = pygame.Rect(int(x), int(y), int(w), int(h))
			pygame.draw.rect(surface, color, rect, stroke)	
	#Return the rectangle area of the surface object.
	def rect(self):
		return self._rect
	rect = property(rect, None, None, None)
	
	#Return a pixelerated rectangle area (i.e., dot size) for the image.
	def cellSize(self):
		return (int(round(self._tileWidth)), int(round(self._tileHeight)))
	cellSize = property(cellSize, None, None, None)
	
if __name__ == "__main__":
	pygame.init()
	DISPLAY_SURFACE = pygame.display.set_mode((320, 240))
	BACKGROUND_COLOR = pygame.Color(15, 77, 143)
	DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
	FPS = 12
	CLOCK = pygame.time.Clock()
		
	cat = Nyancat(pygame.Rect(0, 0, 100, 100))
	cat.rect.center = DISPLAY_SURFACE.get_rect().center
		
	while True:
		DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
			
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
					
		cat.draw(DISPLAY_SURFACE)
		cat.update()		
					
		pygame.display.update()
		CLOCK.tick(FPS)