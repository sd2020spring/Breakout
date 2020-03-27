"""
Breakout model code
"""
import random
import math

class Wall:
    def __init__(self, wh, dims, space, colors, bricks):
        """
        Args:
            wh: tuple of length 2, the width and height of the wall in pixels
            dims: tuple of length 2, the number of rows and columns of bricks on the wall
            space: tuple of length 2, (x, y) pixels of space to place between bricks on the x & y axes
            color: tuple of length 3, (R, G, B) color of the wall
            bricks: array of size 'dims' with an integer value of the number of layers on each brick
        """
        self.wh = wh
        self.bricks = bricks
        self.colors = colors
        self.brick_count = 0 # tracks the number of layers of bricks on the wall
        for i in range(dims[0]):
            for j in range(dims[1]):
                self.brick_count += self.bricks[i][j]

        # calculates width & height of bricks to be able to fit x times y number
        # of them with the specified spacing between them
        self.brick_wh = [int((wh[0]-(dims[0]+1)*space[0])/dims[0]),
                int((wh[1]-(dims[1]+1)*space[1])/dims[1])]

        self.x_coors = []
        self.y_coors = []
        for i in range(dims[0]):
            self.x_coors.append(int(space[0]*(i+1)+self.brick_wh[0]*i))
        for j in range(dims[1]):
            self.y_coors.append(int(space[1]*(j+1)+self.brick_wh[1]*j))

    def remove_brick(self, row, col):
        """ Removes one layer from the brick at the specified row and column
        number of the bricks array.

        Args:
            row: integer index of the row number on the brick wall
            col: integer index of the column number on the brick wall
        """
        self.bricks[row][col] -= 1
        self.brick_count -= 1

        if self.bricks[row][col] < 0:
            self.bricks[row][col] = 0
        if self.brick_count < 0:
            self.brick_count = 0

class Ball:
    def __init__(self, size, radius, xy, color, speed_xy):
        """
        Args:
            size: tuple of length 2, the width and height of the game window in pixels
            radius: radius of the ball in pixels
            xy: tuple of length 2, (x, y) starting position of the ball in pixels
            color: tuple of length 3, (R, G, B) color of the ball
            speed_xy: tuple of length 2, x and y speeds in pixels to move the ball per frame
        """
        self.size = size
        self.radius = radius
        self.xy = xy
        self.color = color
        self.speed_xy = speed_xy

    def move(self):
        """ Moves the ball, including bouncing it off of the game window edges """
        for i in range(2):
            self.xy[i] += self.speed_xy[i]
            if self.xy[i] <= self.radius:
                self.xy[i] = self.radius
                self.speed_xy[i] *= -1
            elif self.xy[i] >= self.size[i]-self.radius:
                self.xy[i] = self.size[i]-self.radius
                self.speed_xy[i] *= -1

class Paddle:
    def __init__(self, size, wh, xy, color, speed):
        """
        Args:
            size: tuple of length 2, the width and height of the game window in pixels
            wh: tuple of length 2, the width and height of the paddle in pixels
            xy: tuple of length 2, (x, y) starting position of the paddle in pixels
            color: tuple of length 3, (R, G, B) color of the paddle
            speed: integer amount of pixels for the paddle to move right/left per
                    press of right/left arrow keys (if using arrow key control)
        """
        self.size = size
        self.wh = wh
        self.xy = xy
        self.color = color
        self.speed = speed

    def move(self, pos=None, dir=None):
        """ Moves the paddle in either the direction or to the position specified """
        if pos != None:
            self.xy[0] = pos
        if dir != None:
            if dir == 'right':
                self.xy[0] += self.speed
            elif dir == 'left':
                self.xy[0] -= self.speed

        # make paddle stay fully onscreen, capped at edges of the screen
        if self.xy[0] < 0:
            self.xy[0] = 0
        if self.xy[0] > self.size[0] - self.wh[0]:
            self.xy[0] = self.size[0] - self.wh[0]

class BreakoutModel:
    """ Encodes a model of the game state """
    def __init__(self, size):
        # window info
        self.size = size
        self.background_color = (0, 0, 0)
        self.wait_time = 1000 # ms to show endscreen before restarting

        # ball info
        ball_radius = int(size[0]/60)
        ball_xy = [int(.5*(self.size[0]-ball_radius)),
                int(.5*(self.size[1]-ball_radius))] # center of screen
        ball_color = (255, 255, 0)
        ball_speed_xy = [random.randint(4,8), random.randint(4,8)]
        self.speed = int(math.sqrt(ball_speed_xy[0]**2 + ball_speed_xy[1]**2)*3)
        self.ball = Ball(self.size, ball_radius, ball_xy,
                ball_color, ball_speed_xy)

        # paddle info
        paddle_wh = [int(size[0]/8), int(size[0]/60)]
        paddle_xy = [int(.5*(self.size[0]-paddle_wh[0])),
                int(.9*(self.size[1]-paddle_wh[1]))] # bottom middle of screen
        paddle_color = (128, 128, 128)
        paddle_speed = int(self.size[0]/15)
        self.paddle = Paddle(self.size, paddle_wh, paddle_xy,
                paddle_color, paddle_speed)

        # wall info
        wall_wh = [self.size[0], int(self.size[1]*.4)] # where build wall
        wall_dims = [6, 5] # num of bricks along x & y axes
        wall_space = [10, 10] # space between bricks on x & y axes

        # bricks 2D array. Each column in a row is the same and each row increases as it goes up the screen
        wall_bricks = [[(wall_dims[1]-j-1)+1 for j in range(wall_dims[1])] for i in range(wall_dims[0])]

        # creating a gradient color function for all possible brick numbers
        max_number = (wall_dims[1]-1)+1
        wall_colors = [((255/(max_number-1))*j,255-(255/(max_number-1))*j,255) for j in range(max_number)]

        self.wall = Wall(wall_wh, wall_dims, wall_space, wall_colors, wall_bricks)

    def update(self):
        """ Update the game state by running the movement of the ball and
        interactions of the ball with the wall and paddle. """
        self.ball.move()
        self.loser = self.check_paddle()
        self.winner = self.check_wall()

    def check_paddle(self):
        """ Makes the ball interact with the paddle by checking whether the ball
        has hit the paddleand whether it went below the paddle.

        Returns:
            boolean whether ball is below paddle, meaning the player lost
        """
        over_paddle = (self.ball.xy[0] >= self.paddle.xy[0]
                and self.ball.xy[0] <= self.paddle.xy[0] + self.paddle.wh[0])
        inside_paddle = (self.paddle.xy[1] <= self.ball.xy[1] + self.ball.radius)
        under_paddle = (self.paddle.xy[1] + self.paddle.wh[1]
                <= self.ball.xy[1] + self.ball.radius)

        if under_paddle: # means you died; can't bounce ball back up
            return True # player lost
        elif over_paddle and inside_paddle:
            self.ball.speed_xy[1] = -1*abs(self.ball.speed_xy[1])
        return False # game still going

    def check_wall(self):
        """ Makes the ball interact with the brick wall by checking whether the
        ball has hit the wall and which brick, then reversing the direction of
        the ball and removing a layer from the brick.

        Returns:
            boolean whether all bricks are gone, meaning the player won
        """
        if self.wall.brick_count == 0: # checks if wall is gone
            return True # player won

        elif self.ball.xy[1] - self.ball.radius <= self.wall.wh[1]: # check if ball is near wall
            x = None

            for i in range(len(self.wall.x_coors)): # check if ball is under a brick vertically
                if (self.ball.xy[0] >= self.wall.x_coors[i] and self.ball.xy[0]
                        <= self.wall.x_coors[i] + self.wall.brick_wh[0]):
                    x = i # saves the wall's x index (column #)

            if x != None:
                for j in range(len(self.wall.y_coors)): # check if ball is touching a brick
                    if (self.ball.xy[1] - self.ball.radius <= self.wall.y_coors[j]
                            + self.wall.brick_wh[1] and self.wall.bricks[x][j] > 0):
                        self.wall.remove_brick(x, j)
                        self.ball.speed_xy[1] = abs(self.ball.speed_xy[1])

        return False # game still going
