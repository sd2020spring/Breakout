"""
BrickBreaker keyboard controller code
"""

import pygame.locals

class PyGameKeyboardController:
    """ Handles keyboard input for brick breaker """
    def __init__(self,model):
        self.model = model

    def handle_event(self,event):
        """ Makes paddle follow arrow key right/left presses """
        if event.type != pygame.locals.KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            self.model.paddle.move(dir='left')
        if event.key == pygame.K_RIGHT:
            self.model.paddle.move(dir='right')
