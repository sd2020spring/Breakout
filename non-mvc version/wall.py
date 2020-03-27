import pygame

class Wall:
    def __init__(self, wh, dims, space, colors, bricks):
        self.wh = wh
        self.bricks = bricks
        self.colors = colors
        self.brick_count = 0
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
        self.bricks[row][col] -= 1
        self.brick_count -= 1

        if self.bricks[row][col] < 0:
            self.bricks[row][col] = 0
        if self.brick_count < 0:
            self.brick_count = 0

    def draw(self, screen):
        for i in range(len(self.bricks)):
            for j in range(len(self.bricks[i])):
                if self.bricks[i][j]:
                    pygame.draw.rect(screen, self.colors[self.bricks[i][j]-1], [self.x_coors[i],
                            self.y_coors[j], self.brick_wh[0], self.brick_wh[1]], 0)
