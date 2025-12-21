from enum import Enum

class Orientation(Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4

def orientation(rect, destination):            #Returns the location of the destination in relation to the given rect
    if rect.column > destination.column:
        return Orientation.LEFT
    if rect.column < destination.column:
        return Orientation.RIGHT
    if rect.row > destination.row:
        return Orientation.UP
    if rect.row < destination.row:
        return Orientation.DOWN
