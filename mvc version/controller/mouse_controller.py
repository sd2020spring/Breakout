"""
BrickBreaker controller code
"""

import pygame.locals

class PyGameMouseController:
    """ A controller that uses the mouse to move the paddle """
    def __init__(self,model):
        self.model = model

    def handle_event(self,event):
        """ Makes paddle follow the mouse horizontally, stopping at edges of the screen.
        """
        if event.type == pygame.locals.MOUSEMOTION:
            self.model.paddle.move(pos=event.pos[0] - self.model.paddle.wh[0]/2)
