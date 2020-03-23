import pygame

class Paddle:
    def __init__(self, size, wh, xy, color, speed):
        """
        Args:
            size: list/tuple of length 2, containing integer values of the width
                    and height respectively of the game window in pixels
            wh: list/tuple of length 2, containing integer values of the width
                    and height respectively of the paddle in pixels
            xy: list/tuple of length 2, containing integer x and y coordinates
                    respectively of the starting position of the paddle in pixels
            color: list/tuple of length 3, containing the integer R, G, and B
                    components of the color to make the paddle
            speed: integer amount of pixels for the paddle to move right/left per
                    press of right/left arrow keys (if using arrow key control)
        """
        self.size = size
        self.wh = wh
        self.xy = xy
        self.color = color
        self.speed = speed

    def move_by_arrow(self, event):
        """ Moves the paddle to follow arrow key right/left presses.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.xy[0] -= self.speed
                if (self.xy[0] < 0):
                    self.xy[0] = 0
            if event.key == pygame.K_RIGHT:
                self.xy[0] += self.speed
                if (self.xy[0] > self.size[0] - self.wh[0]):
                    self.xy[0] = self.size[0] - self.wh[0]

    def move_by_mouse(self, event):
        """ Moves the paddle to follow the mouse horizontally.
        """
        if event.type == pygame.MOUSEMOTION:
            coordinates = pygame.mouse.get_pos() # gives (x,y) coordinates
            self.xy[0] = coordinates[0] - self.wh[0]//2
            if self.xy[0] < 0:
                self.xy[0] = 0
            if self.xy[0] > self.size[0] - self.wh[0]:
                self.xy[0] = self.size[0] - self.wh[0]

    def draw(self, screen):
        """ Draws the paddle on the screen using saved information about it.
        """
        pygame.draw.rect(screen, self.color, [self.xy[0],
                self.xy[1], self.wh[0], self.wh[1]], 0)
