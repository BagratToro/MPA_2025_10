import utils

# Returns the location of the destination in relation to the given rect
def orientation(rect, neighbour, destination):
    cost = 0
    if neighbour == None:
        return cost
    if rect.column > destination.column: # destination is left
        if neighbour == utils.connection(rect, utils.Neighbour.LEFT):
            cost = 0
        if neighbour == utils.connection(rect, utils.Neighbour.RIGHT):
            cost = 3
        if (neighbour == utils.connection(rect, utils.Neighbour.UP)) or (neighbour == utils.connection(rect, utils.Neighbour.DOWN)):
            cost = 2
        return cost
    
    if rect.column < destination.column: # destination is right
        if neighbour == utils.connection(rect, utils.Neighbour.RIGHT):
            cost = 0
        if neighbour == utils.connection(rect, utils.Neighbour.LEFT):
            cost = 3
        if (neighbour == utils.connection(rect, utils.Neighbour.UP)) or (neighbour == utils.connection(rect, utils.Neighbour.DOWN)):
            cost = 2
        return cost
                
    if rect.row > destination.row: # destination is up
        if neighbour == utils.connection(rect, utils.Neighbour.UP):
            cost = 0
        if neighbour == utils.connection(rect, utils.Neighbour.DOWN):
            cost = 3
        if (neighbour == utils.connection(rect, utils.Neighbour.RIGHT)) or (neighbour == utils.connection(rect, utils.Neighbour.LEFT)):
            cost = 2
        return cost

    if rect.row < destination.row: # destination is down
        if neighbour == utils.connection(rect, utils.Neighbour.DOWN):
            cost = 0
        if neighbour == utils.connection(rect, utils.Neighbour.UP):
            cost = 3
        if (neighbour == utils.connection(rect, utils.Neighbour.RIGHT)) or (neighbour == utils.connection(rect, utils.Neighbour.LEFT)):
            cost = 2
        return cost
    

def heuristik(rect, destination):
    cost = 0
    cost = abs(rect.row - destination.row) + abs(rect.column - destination.column) 
    return cost