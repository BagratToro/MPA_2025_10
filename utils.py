import UI.rectField
import pygame
from enum import Enum

GREY = (128, 128, 128)
DARKGREY = (55, 55, 55)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
DARKBLUE = (0, 0, 139)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARKGREEN = (0, 100, 0)
BROWN = (150, 75, 0)

# An Enum (or enumeration) is a special class used to create a set of named constants.
# Here it represends every neighbour of a rectangle.
class Neighbour(Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4

class RectType(Enum):
    Start = 1
    Finish = 2
    Obstacle = 3
    Mud = 4
    Blank = 5

# This function calculates every neighbour of a rectangle.
# A neighbour of a rectangle must touch the rectangle and be either straight left, up, right or under the rectangle.
def connection(rect, neighbour):
    index = -1
    match neighbour:
        case Neighbour.LEFT:
            if rect.column > 0:
                index = rect.row * UI.rectField.RectField.numColumns + rect.column - 1
        case Neighbour.UP:
            if rect.row > 0:
                index = (rect.row - 1) * UI.rectField.RectField.numColumns + rect.column
        case Neighbour.RIGHT:
            if rect.column < UI.rectField.RectField.numColumns - 1:
                index = rect.row * UI.rectField.RectField.numColumns + rect.column + 1
        case Neighbour.DOWN:
            if rect.row < UI.rectField.RectField.numRows - 1:
                index = (rect.row + 1) * UI.rectField.RectField.numColumns + rect.column

    # print(rect.row, rect.column, neighbour, index)
    if index != -1:
        # print(aa.row, aa.column)
        return UI.rectField.RectField.listOfRects[index]
    else:
        return None

# def upConnection(rect):
#     if rect.row > 0:
#         print((rect.row - 1) * UI.rectField.RectField.numColumns + rect.column)
#         return UI.rectField.RectField.listOfRects[(rect.row - 1) * UI.rectField.RectField.numColumns + rect.column]
#     else:
#         return None
    
# # Gibt den unteren Nachbarn eines beliebigen Rechtecks zurück.
# def downConnection(rect):
#     if rect.row < UI.rectField.RectField.numRows - 1:
#         print((rect.row + 1) * UI.rectField.RectField.numColumns + rect.column)
#         return UI.rectField.RectField.listOfRects[(rect.row + 1) * UI.rectField.RectField.numColumns + rect.column]
#     else:
#         return None

# # Gibt den linken Nachbarn eines beliebigen Rechtecks zurück.
# def leftConnection(rect):
#     if rect.column > 0:
#         print(rect.row * UI.rectField.RectField.numColumns + rect.column - 1)
#         return UI.rectField.RectField.listOfRects[rect.row * UI.rectField.RectField.numColumns + rect.column - 1]
#     else:
#         return None

# # Gibt den rechten Nachbarn eines beliebigen Rechtecks zurück.
# def rightConnection(rect):
#     if rect.column < UI.rectField.RectField.numColumns - 1:
#         print(rect.row * UI.rectField.RectField.numColumns + rect.column + 1)
#         return UI.rectField.RectField.listOfRects[rect.row * UI.rectField.RectField.numColumns + rect.column + 1]
#     else:
#         return None

# Searches for the start of the path with the color attribute of the rect. 
def getStart(listOfRects, startColor):
    for rect in listOfRects:
        if rect.color == startColor:
            return rect
        
def getDest(listOfRects, destColor):
    for rect in listOfRects:
        if rect.color == destColor:
            return rect    

def getRect(row, column):
    index = row * UI.rectField.RectField.numColumns + column
    return UI.rectField.RectField.listOfRects[index]

def drawPath(path, color, mudColor):
    if path != None:
        for rect in path:
            if rect.color == BROWN or rect.color == DARKGREY:
                rect.color = mudColor
            elif not rect.color in [YELLOW, BLUE, RED, DARKGREY, DARKGREEN]:
                rect.color = color
            rect.objectRect = pygame.draw.rect(rect.screen, rect.color, rect.rect)

def exclusiveStart():
    for rect in UI.rectField.RectField.listOfRects:
        if rect.color == BLUE:
            rect.color = WHITE
        rect.objectRect = pygame.draw.rect(rect.screen, rect.color, rect.rect)

def exclusiveFinish():
    for rect in UI.rectField.RectField.listOfRects:
        if rect.color == YELLOW:
            rect.color = WHITE
        rect.objectRect = pygame.draw.rect(rect.screen, rect.color, rect.rect)

def clearPath():
    for rect in UI.rectField.RectField.listOfRects:
        if rect.color == GREEN or rect.color == GREY:
            rect.color = WHITE
        elif rect.color == DARKGREEN or rect.color == DARKGREY:
            rect.color = BROWN
        rect.objectRect = pygame.draw.rect(rect.screen, rect.color, rect.rect)


def reset():
    for rect in UI.rectField.RectField.listOfRects:
        rect.color = WHITE
        rect.objectRect = pygame.draw.rect(rect.screen, rect.color, rect.rect)