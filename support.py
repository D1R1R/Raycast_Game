import math
import pygame
import map


class RayCasting():
    def __init__(self,
                screen: pygame.surface.Surface,
                player: pygame.sprite.Sprite,
                mm: any) -> None:
        self._screen = screen
        self._player = player
        self._map = mm
        self.sc_height = 1080
        self.wall_height = 1920

    def draw_rays(self, delta: int, lenov: int, numof: float) -> None:
        start_coord = (self._player.rect.left, self._player.rect.top)
        angle = self._player.angle
        for ray in range(numof):
            cos_a = math.cos(angle)
            sin_a = math.sin(angle)
            for length in range(0, lenov):
                end_coord = (start_coord[0] + (cos_a * length), start_coord[1] + (sin_a * length))
                if not self._map.is_free(end_coord[0], end_coord[1]):
                    break
            # if length != 0:
                # self.draw_screen(length, ray)
            pygame.draw.aaline(self._screen, (0, 0, 255), start_coord, end_coord)
            angle += delta

    def draw_screen(self, leng: int, x: int):
        proection = 10
        color = 255 - round(int(leng) * 0.6)
        # 5 because of 1920 / 5 <-!!
        pygame.draw.line(
            self._screen,
            (color, 0, 0), [x * 5, (self.sc_height // 2 - ((self.wall_height * proection) // leng))],
            [x * 5, (self.sc_height //2 + ((self.wall_height * proection) // leng))],
            5
            )
