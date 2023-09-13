import pygame

from support import RayCasting
from player import MainPlayer
from map import MapSupport



WINDOW_SIZE = (1300, 700)
FPS = 45
RED = (255, 0, 0)


def main(size: tuple) -> None:
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    width, height = size
    players = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    bottom = pygame.sprite.Group()

    # pygame.display.set_caption("Gamee")
    # pygame.display.set_icon(pygame.image.load('icon.png'))
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    # PLAYER
    pl = MainPlayer(screen, r"D:\YandexLyseum2023\PyGameWith\Resourses\Player\test.jpg")
    players.add(pl)
    # MAP
    map = MapSupport(walls, bottom, r'D:\YandexLyseum2023\PyGameWith\Resourses\Map\map.txt')
    map.load_level()

    rc = RayCasting(screen, pl, map)

    running = True
    while running:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

        screen.fill((0, 0, 0))
        clock.tick(FPS)
        # PLAYER UPDATE
        players.draw(screen)
        players.update(walls)
        # MAP UPDATE
        # tiles
        # bottom.draw(screen)
        walls.draw(screen)

        rc.draw_rays(0.005, 425, 384) # 1920 / 5 <- pixels

        pygame.display.flip()


if __name__ == '__main__':
    main(WINDOW_SIZE)