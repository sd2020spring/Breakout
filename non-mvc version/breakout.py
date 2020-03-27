import pygame
from ball import Ball
from paddle import Paddle
from wall import Wall

# Izumi: if you want to edit anything or ask me questions about things I added please
# do! I wrote a lot and I know I'm not the best at documenting/explaining everything.
# Also I'm sure we can add a lot more cool features to make the game better! -Lilo

class Breakout():
    def main(self):
        """ A game of Breakout contains variables of:
            size: list/tuple of length 2, containing integer values of the width
                    and height respectively of the game window in pixels
            background_color: tuple of length 3 of R, G, and B color components
                    for the background color of the window
            speed: integer number of milliseconds to delay between frames,
                    perceived as how fast the game is going
            wait_time: time in milliseconds to wait after winning/losing before
                    resetting and starting again
            ball: a ball object. This game piece is controlled by the program
            paddle: a paddle object. This game piece is controlled by the user
            wall: a wall object. This game piece is controlled by the program
        """
        self.size = (640, 480)
        self.background_color = (0, 0, 0)
        self.speed = 15
        self.wait_time = 2000

        self.ball = self.make_ball()
        self.paddle = self.make_paddle()
        self.wall = self.make_wall()

        pygame.init()
        screen = pygame.display.set_mode(self.size)
        self.play_game(screen)

    def make_ball(self):
        ball_radius = 10
        ball_xy = [int(.5*(self.size[0]-ball_radius)), int(.5*(self.size[1]-ball_radius))]
        ball_color = (255, 255, 0)
        ball_speed_xy = [3, 5]
        return Ball(self.size, ball_radius, ball_xy, ball_color, ball_speed_xy)

    def make_paddle(self):
        paddle_wh = [100, 10]
        paddle_xy = [int(.5*(self.size[0]-paddle_wh[0])), int(.9*(self.size[1]-paddle_wh[1]))]
        paddle_color = (128, 128, 128)
        paddle_speed = int(self.size[0]/20)
        return  Paddle(self.size, paddle_wh, paddle_xy, paddle_color, paddle_speed)

    def make_wall(self):
        wall_wh = [self.size[0], int(self.size[1]*.4)] # what area of screen to build wall in
        wall_dims = [6, 4] # num of bricks along x & y axes
        wall_space = [10, 10] # space between bricks on x & y axes

        # bricks 2D array. Each column in a row is the same and each row increases as it goes up the screen
        wall_bricks = [[(wall_dims[1]-j-1)*2+1 for j in range(wall_dims[1])] for i in range(wall_dims[0])]

        # creating a gradient color function for all possible brick numbers
        max_number = (wall_dims[1]-1)*2+1
        wall_colors = [((255/(max_number-1))*j,255-(255/(max_number-1))*j,255) for j in range(max_number)]

        return Wall(wall_wh, wall_dims, wall_space, wall_colors, wall_bricks)

    def play_game(self, screen):
        running = True
        timer = None
        while running:
            for event in pygame.event.get():
                # two different modes to move the paddle with.
                # can use both modes at same time, only it is more confusing
                self.paddle.move_by_arrow(event) # allows player to move the paddle using arrow keys
                self.paddle.move_by_mouse(event) # allows player to move the paddle using mouse

                # add in escape key incase x button inaccessible (ex. fullscreen mode)
                escape = (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)
                if event.type == pygame.QUIT or escape:
                    running = False

            loser = self.check_paddle()
            winner = self.check_wall()

            if not winner and not loser:
                self.ball.move()
                screen.fill(self.background_color)
                self.paddle.draw(screen)
                self.ball.draw(screen)
                self.wall.draw(screen)
            elif timer == None or pygame.time.get_ticks() - timer < self.wait_time:
                self.show_endscreen(screen, winner)
                if timer == None:
                    timer = pygame.time.get_ticks()
            else:
                self.paddle = self.make_paddle()
                self.ball = self.make_ball()
                self.wall = self.make_wall()
                timer = None

            pygame.time.delay(self.speed)
            pygame.display.flip()

        pygame.quit()

    def show_endscreen(self, screen, winner):
        """ Currently shows green for winner, red for loser.
        """
        if winner:
            screen.fill((0,255,0))
        else:
            screen.fill((255,0,0))

    def check_paddle(self):
        """ Makes the ball interact with the paddle.

            Returns:
                boolean whether ball is below paddle, meaning the player lost
        """
        over_paddle = (self.ball.xy[0] >= self.paddle.xy[0] and self.ball.xy[0] <= self.paddle.xy[0]+paddle.wh[0])
        inside_paddle = (self.paddle.xy[1] <= self.ball.xy[1] + self.ball.radius)
        under_paddle = (self.paddle.xy[1] + self.paddle.wh[1] <= self.ball.xy[1] + self.ball.radius)

        if under_paddle: # means you died; can't bounce ball back up
            return True # tells program to stop running
        elif over_paddle and inside_paddle:
            self.ball.speed_xy[1] = -1*abs(self.ball.speed_xy[1])
        return False # tells program to keep running

    def check_wall(self):
        """ Makes the ball interact with the brick wall.

            Returns:
                boolean whether all bricks are gone, meaning the player won
        """
        if self.wall.brick_count == 0: # checks if wall is gone
            return True # tells program to quit

        elif self.ball.xy[1] - self.ball.radius <= self.wall.wh[1]: # check if ball is near wall
            x = None

            for i in range(len(self.wall.x_coors)): # check if ball is under a brick vertically
                if self.ball.xy[0] >= self.wall.x_coors[i] and self.ball.xy[0] <= self.wall.x_coors[i] + self.wall.brick_wh[0]:
                    x = i # saves the wall's x index for that column of the wall

            if x != None:
                for j in range(len(self.wall.y_coors)): # check if ball is touching a brick
                    if self.ball.xy[1] - self.ball.radius <= self.wall.y_coors[j] + self.wall.brick_wh[1] and self.wall.bricks[x][j] > 0:
                        self.wall.remove_brick(x, j)
                        self.ball.speed_xy[1] = abs(self.ball.speed_xy[1])

        return False # tells program to keep going

if __name__ == '__main__':
    br = Breakout()
    br.main()
