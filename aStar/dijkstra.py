import utils
import UI.rectField



def runDijkstraRekursive():
    path = dijkstraRekursive(getStart(UI.rectField.RectField.listOfRects, utils.BLUE), utils.RED, utils.YELLOW)
    print(path[1])
    drawPath(path[0])

def dijkstraRekursive(rect, obstacleColor, destinationColor): # gives back the "path" and a boolean, if it reached the destination. Needs a starting rect
    optimalPath = None
    
    if rect == None:
        return optimalPath
    # print(rect.row, rect.column)
    
    if rect.color == destinationColor:
        return ([rect], True)
    
    if (rect.color == obstacleColor):
        return ([rect], False)
    
    rect.processing = True

    pathLeft = getPathIfNotVisited(utils.connection(rect, utils.Neighbour.LEFT), obstacleColor, destinationColor)
    pathUp = getPathIfNotVisited(utils.connection(rect, utils.Neighbour.UP), obstacleColor, destinationColor)
    pathRight = getPathIfNotVisited(utils.connection(rect, utils.Neighbour.RIGHT), obstacleColor, destinationColor)
    pathDown = getPathIfNotVisited(utils.connection(rect, utils.Neighbour.DOWN), obstacleColor, destinationColor)

    rect.processing = False
    
    optimalPath = getOptimalPath(pathLeft, optimalPath)
    optimalPath = getOptimalPath(pathUp, optimalPath)
    optimalPath = getOptimalPath(pathRight, optimalPath)
    optimalPath = getOptimalPath(pathDown, optimalPath)
    
    if optimalPath != None:
        optimalPath[0].insert(0, rect)
    
    return optimalPath

def getPathIfNotVisited(rect, obstacleColor, destinationColor):
    path = None
    if (rect != None) and (not rect.processing):
        path = dijkstraRekursive(rect, obstacleColor, destinationColor)
    return path
        
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

def getStart(listOfRects, startColor):
    for rect in listOfRects:
        if rect.color == startColor:
            return rect
        
def drawPath(path):
    if path != None:
        for rect in path:
            rect.color = utils.GREEN



def dijkstraIterative(rect, obstacleColor, destinationColor):
    optimalPath = None
    currentPath = None
    while rect.color != destinationColor:
        if rect == None:
            continue
        if rect.color == obstacleColor:
            currentPath = None

        









