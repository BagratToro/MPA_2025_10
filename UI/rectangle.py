import pygame
import utils
pygame.init()


#The class for a single rectangle. (Ist die Klasse für jedes einzelne Rechteck.)
class Rectangle:
    def __init__(self, screen, leftTopX, leftTopY, width, height, row, column, color, mousePos):
        self.mousePos = mousePos
        self.screen = screen
        self.rect = (leftTopX, leftTopY, width, height)
        self.color = color
        self.row = row
        self.column = column
        self.objectRect = pygame.draw.rect(screen, self.color, (leftTopX, leftTopY, width, height))
        self.realCost = float("inf")
        self.cost = float("inf")


    # Changes the color of a rectangle based on the input of the user.
    def changeColor(self, mouseInputs, type):
        if self.objectRect.collidepoint(self.mousePos):
            if mouseInputs[0]:
                match type:
                    case utils.RectType.Start:
                        utils.exclusiveStart()
                        self.color = utils.BLUE
                    case utils.RectType.Finish:
                        utils.exclusiveFinish()
                        self.color = utils.YELLOW
                    case utils.RectType.Obstacle:
                        self.color = utils.RED
                    case utils.RectType.Mud:
                        self.color = utils.BROWN
                    case utils.RectType.Blank:
                        self.color = utils.WHITE

        self.objectRect = pygame.draw.rect(self.screen, self.color, self.rect)