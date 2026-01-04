#This file serves the implementation of buttons, mainly to enhance the user experience.

import pygame
import utils

pygame.init()

#List of all buttons
listOfButtons=[]

#(ButtonTypeToggle = True) The button executes it's associated function until pressed again.
#(ButtonTypeToggle = False) The button executes it's associated function once.
class Button():
    def __init__(self, screen, leftX, topY, width, height, buttonTypeToggle, function = None, displayedText = 'test'):
        self.screen = screen
        self.leftX = leftX
        self.topY = topY
        self.width = width
        self.height = height
        self.buttonTypeToggle = buttonTypeToggle
        self.function = function
        self.pressed = False
          
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRectangle = pygame.Rect(self.leftX, self.topY, self.width, self.height)
        self.buttonText = pygame.font.SysFont('Arial', 40).render(displayedText, True, (30, 30, 30))
          
        listOfButtons.append(self)


    def check(self):
        self.buttonSurface.fill(utils.GREEN)
        if self.buttonRectangle.collidepoint(pygame.mouse.get_pos()):
            self.buttonSurface.fill(utils.YELLOW)
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(utils.RED)
                if self.buttonTypeToggle == False:
                    self.function()
                elif self.pressed == False:
                    self.pressed = True
                else:
                    self.pressed = False

        self.buttonSurface.blit(self.buttonText, [
            self.buttonRectangle.width/2 - self.buttonText.get_rect().width/2,
            self.buttonRectangle.height/2 - self.buttonText.get_rect().height/2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRectangle)