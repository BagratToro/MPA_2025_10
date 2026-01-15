#This file serves the implementation of buttons, mainly to enhance the user experience.

import pygame
import utils

pygame.init()

#List of all buttons
listOfButtons=[]

#(ButtonTypeToggle = True) The button executes it's associated function until pressed again.
#(ButtonTypeToggle = False) The button executes it's associated function once.
class Button():
    def __init__(self, screen, leftX, topY, width, height, buttonTypeToggle, displayedText = 'test', function = None, pressed = False):
        self.screen = screen
        self.leftX = leftX
        self.topY = topY
        self.width = width
        self.height = height
        self.buttonTypeToggle = buttonTypeToggle
        self.pressed = False
        self.function = function
          
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRectangle = pygame.Rect(self.leftX, self.topY, self.width, self.height)
        self.buttonText = pygame.font.SysFont('Arial', 40).render(displayedText, True, (utils.WHITE))
          
        listOfButtons.append(self)

    def getPressed(self):
        return self.pressed

    def check(self, event):
        self.event = event
        if self.pressed != True:
            self.buttonSurface.fill(utils.BLUE)
        else: 
            self.buttonSurface.fill(utils.DARKBLUE)
        if self.buttonRectangle.collidepoint(pygame.mouse.get_pos()):
            self.buttonSurface.fill(utils.GREEN)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.buttonSurface.fill(utils.DARKBLUE)
                if self.buttonTypeToggle == False:
                    self.function()
                elif self.pressed == False:
                    for button in listOfButtons:
                        button.pressed = False
                    self.pressed = True
                    self.function()
                else:
                    self.pressed = False
                    utils.textboxDisplayedText='Select a button'


        self.buttonSurface.blit(self.buttonText, [
            self.buttonRectangle.width/2 - self.buttonText.get_rect().width/2,
            self.buttonRectangle.height/2 - self.buttonText.get_rect().height/2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRectangle)

        pygame.draw.rect(self.screen, utils.BLACK, self.buttonRectangle, 1)
