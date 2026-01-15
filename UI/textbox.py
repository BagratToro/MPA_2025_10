import pygame
import utils
pygame.init()


class TextBox:
    def __init__(self, screen, leftX, topY, width, height, font):
        self.screen = screen
        self.leftX = leftX
        self.topY = topY
        self.widht = width
        self.height = height
        self.font = font

        self.line_height = font.get_height()
        self.lines = []
        self.start = 0
        self.gap = 5
        self.draw

    # def add_text(self, text):
    #     for line in text.split("\n"):
    #         self.lines.append(line)

    # def scroll(self, event):
    #     if event.type == pygame.MOUSEWHEEL:
    #         self.start -= event.y
    #         self.start = max(0, min(self.start, max(0, len(self.lines) - self.visible_lines())))

    # def visible_lines(self):
    #     return (self.height - 2 * self.gap) // self.line_height

    def draw(self, surface):
        pygame.draw.rect(surface, utils.BLACK, (self.leftX - 2, self.topY - 2, self.widht- 2 , self.height- 2 ))
        pygame.draw.rect(surface, utils.YELLOW, (self.leftX, self.topY, self.widht, self.height), 2)

        # start = self.start
        # end = start + self.visible_lines()
        # y = self.topY + self.gap

        # for line in self.lines[start:end]:
        #     txt_surf = self.font.render(line, True, utils.WHITE)
        #     surface.blit(txt_surf, (self.leftX + self.gap, y))
        #     y += self.line_height