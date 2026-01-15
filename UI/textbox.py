import pygame
import utils
pygame.init()


class TextBox:
    def __init__(self, screen, leftX, topY, width, height, screenHeight):
        self.screen = screen
        self.leftX = leftX
        self.topY = topY
        self.width = width
        self.height = height
        self.screenHeight = screenHeight

        self.TextboxSurface = pygame.Surface((self.width, self.height))
        self.TextboxRectangle = pygame.Rect(self.leftX, self.topY, self.width, self.height)

        self.drawsurface

    def drawsurface(self):
        self.TextboxText = pygame.font.SysFont('Courier New', 30).render(utils.textboxDisplayedText, True, (utils.WHITE))
        self.TextboxSurface.fill(utils.BLACK)
        self.TextboxSurface.blit(self.TextboxText, [
            self.TextboxRectangle.width/2 - self.TextboxText.get_rect().width/2,
            self.TextboxRectangle.height/2 - self.TextboxText.get_rect().height/2
        ])
        self.screen.blit(self.TextboxSurface, self.TextboxRectangle)
