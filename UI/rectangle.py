import pygame
#import aStar.dijkstra
#import aStar.aStar
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
        self.cost = float("inf")


    # Changes the color of a rectangle based on the input of the user. (Verändert die Farbe eines Rechtecks anhand von Eingaben des Users.)
    def changeColor(self, event, mouseInputs, type):
        if self.objectRect.collidepoint(self.mousePos):
            if mouseInputs[0]:
                match type:
                    case utils.RectType.Start:
                        utils.exclusiveStart()
                        self.color = utils.BLUE #blue
                    case utils.RectType.Finish:
                        utils.exclusiveFinish()
                        self.color = utils.YELLOW #yellow
                    case utils.RectType.Obstacle:
                        self.color = utils.RED #red
                    case utils.RectType.Mud:
                        self.color = utils.BROWN #brown
                    case utils.RectType.Blank:
                        self.color = utils.WHITE #white

        self.objectRect = pygame.draw.rect(self.screen, self.color, self.rect)


