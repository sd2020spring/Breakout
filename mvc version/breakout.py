"""
This project uses the Model-View-Controller (MVC) design pattern to create the
arcade game Breakout.

@author: Lilo & Izumi
"""

import pygame
from model import BreakoutModel
from view import PyGameWindowView
from controller.keyboard_controller import PyGameKeyboardController
from controller.mouse_controller import PyGameMouseController

def play_game(size):
    """
    Given screen 'size' as (x,y) tuple, start Breakout game
    """
    pygame.init()
    model = BreakoutModel(size)
    view = PyGameWindowView(model, size)
    controller = PyGameMouseController(model)
    # controller = PyGameKeyboardController(model)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                running = False
            controller.handle_event(event)
        model.update()

        if not model.loser and not model.winner:
            view.draw()
            pygame.time.delay(model.speed)
        else:
            running = False
    pygame.quit()

if __name__ == '__main__':
    size = (640, 480)
    play_game(size)
