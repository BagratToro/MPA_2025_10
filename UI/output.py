import pygame
import utils
pygame.init()

# Class for the Output Textbox.
class Output:
    def __init__(self, screen, leftX, topY, width, height, screenHeight):
        self.screen = screen
        self.leftX = leftX
        self.topY = topY
        self.width = width
        self.height = height
        self.screenHeight = screenHeight

        self.OutputSurface = pygame.Surface((self.width, self.height))
        self.OutputRectangle = pygame.Rect(self.leftX, self.topY, self.width, self.height)

        self.refreshText

    # Overrides old text and blits the current outputDisplayedText onto the OutputSurface, which is blited onto the screen afterwards.
    def refreshText(self):
        self.OutputText = pygame.font.SysFont('Courier New', 30).render(utils.outputDisplayedText, True, (utils.WHITE), (utils.BLACK))
        self.OutputSurface.fill(utils.BLACK)
        self.OutputSurface.blit(self.OutputText, [
            self.OutputRectangle.width/2 - self.OutputText.get_rect().width/2,
            self.OutputRectangle.height/2 - self.OutputText.get_rect().height/2
        ])
        self.screen.blit(self.OutputSurface, self.OutputRectangle)
