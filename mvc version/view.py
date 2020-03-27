"""
Breakout view code
"""

import pygame

class PyGameWindowView:
    """ A view of breakout rendered in a Pygame window """
    def __init__(self, model, size):
        """ Initialize the view with a reference to the model and the
            specified game screen dimensions (represented as a tuple
            containing the width and height) """
        self.model = model
        self.screen = pygame.display.set_mode(size)

    def draw(self):
        """ Draw the current game state to the screen """
        self.screen.fill(self.model.background_color)

        # draw paddle
        pygame.draw.rect(self.screen, self.model.paddle.color,
                [self.model.paddle.xy[0], self.model.paddle.xy[1],
                self.model.paddle.wh[0], self.model.paddle.wh[1]], 0)

        # draw ball
        pygame.draw.circle(self.screen, self.model.ball.color,
                self.model.ball.xy, self.model.ball.radius, 0)

        # draw wall
        for i in range(len(self.model.wall.bricks)):
            for j in range(len(self.model.wall.bricks[i])):
                if self.model.wall.bricks[i][j]:
                    pygame.draw.rect(self.screen,
                            self.model.wall.colors[self.model.wall.bricks[i][j]-1],
                            [self.model.wall.x_coors[i], self.model.wall.y_coors[j],
                            self.model.wall.brick_wh[0], self.model.wall.brick_wh[1]], 0)
        pygame.display.update()
