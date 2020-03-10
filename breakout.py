import pygame, sys

# pygame.init()
# screen = pygame.display.set_mode([500, 500])
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill((255, 255, 255))
#     pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
#
# pygame.quit()


class Breakout():
    def main(self):
        xspeed_init = 6
        yspeed_init = 6
        max_lives = 5
        bat_speed = 30
        score = 0
        bgcolour = 0x2F, 0x4F, 0x4F  # darkslategrey
        size = width, height = 640, 480

        pygame.init()
        screen = pygame.display.set_mode(size)
        #screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

        # bat = pygame.image.load("bat.png").convert()
        # batrect = bat.get_rect()
        # batrect = pygame.draw.rect(screen, (0, 0, 255), (250, 250), 75)
        bat = pygame.draw.rect(screen, (0, 0, 255), (100,200,100,20), 2)


        # ball = pygame.image.load("ball.png").convert()
        # ball.set_colorkey((255, 255, 255))
        # ballrect = ball.get_rect()
        ball = pygame.draw.circle(screen, (0, 0, 255), (25, 25), 75)

        # pong = pygame.mixer.Sound('Blip_1-Surround-147.wav')
        # pong.set_volume(10)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # screen.fill((255, 255, 255))
            # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        pygame.quit()

if __name__ == '__main__':
    br = Breakout()
    br.main()
