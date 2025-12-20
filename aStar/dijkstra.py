import utils
import UI.rectField

path = []

def distance(rect):
    utils.connections(rect)

    # for rect in listOfUnvisitedRects:
    #     if rect.color == (255, 255, 0): #yellow
    #         return 
    #     if rect.color == (255, 165, 0): #orange
    #         endRect = rect
    #     if rect.color == (128, 128, 128): #grey
    #         return 
    #     listOfRects = UI.rectField.RectField.listOfRects
    # listOfVisitedRects = []
    # listOfUnvisitedRects = [listOfRects]

def dijkstra(rect, obstacleColor, destinationColor): # gives back the "path" and a boolean, if it reached the destination. Needs a starting rect
    optimalPath = None
    
    if rect == None:
        return optimalPath
    print(rect.row, rect.column)
    
    if rect.color == destinationColor:
        return ([rect], True)
    
    if (rect.color == obstacleColor) or (rect.visited):
        return ([rect], False)
    
    rect.visited = True
    pathLeft = dijkstra(utils.connection(rect, utils.Neighbour.LEFT), obstacleColor, destinationColor)
    pathUp = dijkstra(utils.connection(rect, utils.Neighbour.UP), obstacleColor, destinationColor)
    pathRight = dijkstra(utils.connection(rect, utils.Neighbour.RIGHT), obstacleColor, destinationColor)
    pathDown = dijkstra(utils.connection(rect, utils.Neighbour.DOWN), obstacleColor, destinationColor)
    

    optimalPath = getOptimalPath(pathLeft, optimalPath)
    optimalPath = getOptimalPath(pathUp, optimalPath)
    optimalPath = getOptimalPath(pathRight, optimalPath)
    optimalPath = getOptimalPath(pathDown, optimalPath)
    if optimalPath != None:
        optimalPath[0].insert(0, rect)
    # print(optimalPath)
    return optimalPath
        
def getOptimalPath(currentPath, optimalPath):
    if currentPath == None:
        return optimalPath
    
    if currentPath[1] == False:
        return optimalPath
    
    if optimalPath == None:
        return currentPath
    
    if len(currentPath[0]) < len(optimalPath[0]):
        return currentPath
    
    return optimalPath

# def getStart(listOfRects, startColor):
#     for rect in listOfRects:
#         if rect.color == startColor:
#             return rect

