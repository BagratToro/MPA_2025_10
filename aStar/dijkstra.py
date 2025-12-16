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

def dijkstra(rect): # gives back the "path" and a boolean, if it reached the destination. Needs a starting rect
    optimalPath = None
    if rect == None:
        return optimalPath
    
    if rect.color == (255, 255, 0): #yellow, destination
        return ((rect), True)
    
    if rect.color == (128, 128, 128): #grey, obstacle
        return ((rect), False)

    pathLeft = dijkstra(utils.leftConnection(rect))
    pathUp = dijkstra(utils.upConnection(rect))
    pathRight = dijkstra(utils.rightConnection(rect))
    pathDown = dijkstra(utils.downConnection(rect))

    optimalPath = getOptimalPath(pathLeft, optimalPath)
    optimalPath = getOptimalPath(pathUp, optimalPath)
    optimalPath = getOptimalPath(pathRight, optimalPath)
    optimalPath = getOptimalPath(pathDown, optimalPath)
    optimalPath[0].prepend(rect)
    return optimalPath
        
def getOptimalPath(currentPath, optimalPath):
    if currentPath[1] == False:
        return optimalPath
    
    if optimalPath == None:
        return currentPath
    
    if len(currentPath[0]) < len(optimalPath[0]):
        return currentPath
    
    return optimalPath





    
    
    

            

