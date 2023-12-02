
"""Draw text to the screen."""
import pygame
# from pygame.locals import *
import time

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# colors
navy = (43, 42, 76)   # 2b2a4c    rgb(43, 42, 76)
red = (179, 19, 18)  # b31312    rgb(179, 19, 18)
orange = (234, 144, 108)  # ea906C    rgb(234, 144, 108)
peach = (238, 226, 222)  # eee2de    rgb(238, 226, 222)


class App:

    def __init__(self):

        self._running = True
        self.flags = pygame.RESIZABLE
        self.size = self.weight, self.height = 640, 400
        self.mx, self.my = 0, 0

        pygame.init()
        pygame.display.set_caption('Cart Splitter')
        self.screen = pygame.display.set_mode(self.size, self.flags)

        # clock
        self.clock = pygame.time.Clock()

        # Fonts - I only want a few simple fonts
        self.font_size_default = 24
        font = pygame.font.SysFont(None, self.font_size_default)
        sysfont = pygame.font.get_default_font()
        font_names = {
            'sans': 'Arial',
            'monospace': 'Consolas',
            'serif': 'Cambria',
        }
        self.fonts = {
            'sans': pygame.font.SysFont(font_names['sans'], self.font_size_default),
            'monospace': pygame.font.SysFont(font_names['monospace'], self.font_size_default),
            # 'serif': None,
        }

        # freesansbold.ttf
        img = font.render(sysfont, True, RED)
        rect = img.get_rect()
        pygame.draw.rect(img, BLUE, rect, 1)
        self.img = img

        # font1 = pygame.font.SysFont(font_names['sans'], self.font_size_default)
        self.img1 = self.fonts['sans'].render(
            'sans serif text, regular text', True, GREEN)

        # font2 = pygame.font.SysFont(
        # font_names['monospace'], self.font_size_default)
        self.img2 = self.fonts['monospace'].render(
            'mono space text like code', True, BLUE)

    def run(self):
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

                if event.type == pygame.VIDEORESIZE:
                    self.size = self.weight, self.height = event.size
                    self.screen = pygame.display.set_mode(
                        self.size, self.flags)

                # mouse move
                if event.type == pygame.MOUSEMOTION:
                    # print('mouse move')
                    self.mx, self.my = event.pos

            self.screen.fill(BLACK)
            self.screen.blit(self.img, (20, 20))
            self.screen.blit(self.img1, (20, 50))
            self.screen.blit(self.img2, (20, 120))

            dt = self.clock.tick(99)
            # print('dt :', dt)
            # print('FPS :', self.clock.get_fps())

            # draw ui stuff
            self.draw_text(
                self.screen, f'mouse: {self.mx}, {self.my}', 30, 30, color=red)

            # update display
            pygame.display.update()

        pygame.quit()

    def draw_text(self, surface: pygame.Surface, text: str, x: int, y: int, font_size: int = 24, color=GRAY, font_type: str = 'sans'):
        font = self.fonts[font_type]
        img = font.render(text, True, color)
        surface.blit(img, (x, y))


if __name__ == "__main__":

    app = App()
    app.run()
