import pygame

class Ball:
    def __init__(self, size, radius, xy, color, speed_xy):
        """
        Args:
            size: list/tuple of length 2, containing integer values of the width
                    and height respectively of the game window in pixels
            radius: integer of the radius of the ball in terms of number of pixels
            xy: list/tuple of length 2, containing integer x and y coordinates
                    respectively of the starting position of the ball in pixels
            color: list/tuple of length 3, containing the integer R, G, and B
                    components of the color to make the ball
            speed_xy: list/tuple of length 2, containing integer x and y speeds
                    respectively in pixels to move the ball per frame
        """
        self.size = size
        self.radius = radius
        self.xy = xy
        self.color = color
        self.speed_xy = speed_xy

    def move(self):
        """ Moves the ball, including bouncing it off of the game window edges.
        """
        for i in range(2):
            self.xy[i] += self.speed_xy[i]
            if self.xy[i] <= self.radius:
                self.xy[i] = self.radius
                self.speed_xy[i] *= -1
            elif self.xy[i] >= self.size[i]-self.radius:
                self.xy[i] = self.size[i]-self.radius
                self.speed_xy[i] *= -1

    def draw(self, screen):
        """ Draws the ball on the screen using saved information about it.
        """
        pygame.draw.circle(screen, self.color, self.xy, self.radius, 0)
