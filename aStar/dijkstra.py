#import copy
import utils
import UI.rectField
import UI.buttons
#from collections import deque
# Is a structur which storts a list automaticaly from smallest to biggest
import heapq


# def runDijkstraRekursive():
#     path = dijkstraRekursive(utils.getStart(UI.rectField.RectField.listOfRects, utils.BLUE), utils.RED, utils.YELLOW)
#     print(path[1])
#     drawPath(path[0])

def runDijkstra():
    numDest = 0
    numStart = 0
    for button in UI.buttons.listOfButtons:
        button.pressed = False
    utils.clearPath()
    for rect in UI.rectField.RectField.listOfRects:
        if rect.color == utils.BLUE:
            numStart += 1
        if rect.color == utils.YELLOW:
            numDest += 1
    #if (numDest == 1) and (numStart == 1):
        #path = dijkstra(utils.getStart(UI.rectField.RectField.listOfRects, utils.BLUE), utils.RED, utils.YELLOW, utils.BROWN)
        #utils.drawPath(path, utils.GREEN, utils.DARKGREEN)
    match numDest:
        case 1 if numStart == 1:
            path = dijkstra(utils.getStart(UI.rectField.RectField.listOfRects, utils.BLUE), utils.RED, utils.YELLOW, utils.BROWN)
            utils.drawPath(path, utils.GREEN, utils.DARKGREEN)
            utils.textboxDisplayedText='Sucessfully ran the Dijkstra algorithm'
        case 1 if numStart == 0:
            utils.textboxDisplayedText='You need to select a starting square to run the Dijkstra algorithm'
        case 0 if numStart == 1:
            utils.textboxDisplayedText='You need to select a destination square to run the Dijkstra algorithm'
        case 0 if numStart == 0:
            utils.textboxDisplayedText='You need to select a starting square and a destination square to run the Dijkstra algorithm'


# def dijkstraRekursive(rect, obstacleColor, destinationColor): # gives back the "path" and a boolean, if it reached the destination. Needs a starting rect
#     optimalPath = None
    
#     if rect == None:
#         return optimalPath
#     # print(rect.row, rect.column)
    
#     if rect.color == destinationColor:
#         return ([rect], True)
    
#     if (rect.color == obstacleColor):
#         return ([rect], False)
    
#     # The atribute of the rectangle is turned "True", so that in the rekursion, it will not be considered anymore.
#     rect.processing = True

#     pathLeft = getPathIfNotVisited(utils.connection(rect, utils.Neighbour.LEFT), obstacleColor, destinationColor)
#     pathUp = getPathIfNotVisited(utils.connection(rect, utils.Neighbour.UP), obstacleColor, destinationColor)
#     pathRight = getPathIfNotVisited(utils.connection(rect, utils.Neighbour.RIGHT), obstacleColor, destinationColor)
#     pathDown = getPathIfNotVisited(utils.connection(rect, utils.Neighbour.DOWN), obstacleColor, destinationColor)

#     rect.processing = False
#     # Here the atribute is again false, because in other rekursive calls, it doesn't have to be checked.
#     # If a rectangle is checked in the left rekursion, it does not have to be checked in the up rekursion.
    
#     optimalPath = getOptimalPath(pathLeft, optimalPath)
#     optimalPath = getOptimalPath(pathUp, optimalPath)
#     optimalPath = getOptimalPath(pathRight, optimalPath)
#     optimalPath = getOptimalPath(pathDown, optimalPath)
    
#     if optimalPath != None:
#         optimalPath[0].insert(0, rect)
    
#     return optimalPath

# def getPathIfNotVisited(rect, obstacleColor, destinationColor):
#     path = None
#     if (rect != None) and (not rect.processing):
#         path = dijkstraRekursive(rect, obstacleColor, destinationColor)
#     return path

# Compares a current path which is created by the rekursive call and the optimal path by that point, to find the shortest path.  
# def getOptimalPath(currentPath, optimalPath):
#     if currentPath == None:
#         return optimalPath
    
#     if currentPath[1] == False:
#         return optimalPath
    
#     if optimalPath == None:
#         return currentPath
    
#     if len(currentPath[0]) < len(optimalPath[0]):
#         return currentPath
    
#     return optimalPath

# Draws the shortest path by changing the color of every rect to green.


# A iterative approache.
# def dijkstraIterative(startRect, obstacleColor, destinationColor):
#     rectStack = deque()
#     rectStack.append((startRect, (set(), False)))
#     # optimalPath = None
#     listOfPaths = []

#     # currentPath = None
#     while len(rectStack) != 0: #or rect.color != destinationColor
#         currentItem = rectStack.popleft() #popleft()
#         rect = currentItem[0]
#         currentPath = currentItem[1]
#         # currentRect[0].processing = True
#         # print(rectStack)
#         if (rect == None) or (rect.color == obstacleColor):
#             continue

#         if rect.color == destinationColor:
#             # currentPath = (currentPath[0], True)
#             listOfPaths.append((copy.copy(currentPath[0]), True))
#             break
        
#         # elif (rect.color == obstacleColor):
#         #     currentPath = (currentPath[0], False)
#         #     continue
        
#         else:
#             currentPath[0].add(rect)
#             # listOfPaths.append(currentPath)

#         # rect.processing = True
#         leftRect = utils.connection(rect, utils.Neighbour.LEFT)
#         upRect = utils.connection(rect, utils.Neighbour.UP)
#         rightRect = utils.connection(rect, utils.Neighbour.RIGHT)
#         downRect = utils.connection(rect, utils.Neighbour.DOWN)
        
#         if (leftRect != None) and (not isInPath(leftRect, currentPath)):
#             rectStack.append((leftRect, (copy.copy(currentPath[0]), False)))
#         if (upRect != None) and (not isInPath(upRect, currentPath)):
#             rectStack.append((upRect, (copy.copy(currentPath[0]), False)))
#         if (rightRect != None) and (not isInPath(rightRect, currentPath)):
#             rectStack.append((rightRect, (copy.copy(currentPath[0]), False)))
#         if (downRect != None) and (not isInPath(downRect, currentPath)):
#             rectStack.append((downRect, (copy.copy(currentPath[0]), False)))
        
#         # rect.processing = False

#     optimalPath = None
#     # print(listOfPaths)
#     for path in listOfPaths:
#         optimalPath = getOptimalPath(path, optimalPath)

#     return optimalPath

# def isInPath(rect, path):
#     return rect in path
#     # for r in path[0]:
#     #     if (r.row == rect.row) and (r.column == rect.column):
#     #         return True
    
#     # return False

def rectCost(rect, slowColor):
    if rect.color == slowColor:
        return 5
    return 1

def dijkstra(startRect, obstacleColor, destinationColor, slowColor):
    counter = 0
    startRect.cost = 0
    priorityQueue = [(startRect.cost, counter, startRect)]
    checkedRect = []
    destination = utils.getDest(UI.rectField.RectField.listOfRects, utils.YELLOW)
    
    # These dictionaries hold the inforamtions to every rectangle.
    distance = {startRect: 0}
    previousRect = {startRect: None}
    
    # Goes over every node and takes every time that node, which takes the smallest value. 
    # That's why the algorythm uses heap and pops always from the beginning.
    while priorityQueue:
        currentItem = heapq.heappop(priorityQueue)
        (currentCost, placeHolder, rect) = currentItem

        # The while loop should end, whenever it gets to the destination -> *früh stopp* Dijkstra !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if rect.color == destinationColor:
            break
        # When it costs to much, to get to that node, it should ignore that path.
        
        if currentCost > distance[rect]:
            continue

        checkedRect.append(rect)

        # Now comparing all neighbours of that rectangle.
        listOfNeighbours = (utils.connection(rect, utils.Neighbour.LEFT), utils.connection(rect, utils.Neighbour.UP), utils.connection(rect, utils.Neighbour.RIGHT), utils.connection(rect, utils.Neighbour.DOWN))
        for neighbour in listOfNeighbours:
            if neighbour == None:
                continue
            if neighbour.color == obstacleColor:
                continue

            neighbour.cost = rectCost(neighbour, slowColor)
            neighbour.cost = currentCost + neighbour.cost

            if (neighbour not in distance) or (neighbour.cost < distance[neighbour]):
                distance[neighbour] = neighbour.cost
                previousRect[neighbour] = rect
                counter += 1
                heapq.heappush(priorityQueue, (neighbour.cost, counter, neighbour))
                
            utils.drawPath(checkedRect, utils.GREY, utils.DARKGREY)
        
    rect = utils.getRect(rect.row, rect.column)    
    path = []
    while rect != None:
        pathRect = rect
        path.append(pathRect)
        rect = previousRect[rect]
    path.reverse()

    return path

