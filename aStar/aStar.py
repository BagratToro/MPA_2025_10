import heapq
import utils
import UI.rectField

def runAStar():
    numDest = 0
    numStart = 0
    for button in utils.listOfButtons:
        button.pressed = False
    utils.clearPath()
    for rect in UI.rectField.RectField.listOfRects:
        if rect.color == utils.BLUE:
            numStart += 1
        if rect.color == utils.YELLOW:
            numDest += 1
    match numDest:
        case 1 if numStart == 1:
            path = aStar(utils.getStart(UI.rectField.RectField.listOfRects, utils.BLUE), utils.RED, utils.YELLOW, utils.BROWN)
            if path[1] == False:
                utils.drawPath(path[0], utils.GREY, utils.DARKGREEN)
                utils.textboxDisplayedText='There is no possible path'
            else:
                utils.drawPath(path[0], utils.GREEN, utils.DARKGREEN)
                utils.textboxDisplayedText='Sucessfully ran the A* algorithm'
        case 1 if numStart == 0:
            utils.textboxDisplayedText='You need to select a starting \nsquare to run the A* algorithm'
        case 0 if numStart == 1:
            utils.textboxDisplayedText='You need to select a destination \nsquare to run the A* algorithm'
        case 0 if numStart == 0:
            utils.textboxDisplayedText='You need to select a starting square and \na destination square to run the A* algorithm'

def rectCost(rect, slowColor):
    if rect.color == slowColor:
        return 7
    return 1

def heuristik(rect, destination):
    cost = 0
    cost = abs(rect.row - destination.row) + abs(rect.column - destination.column) 
    return cost

def aStar(startRect, obstacleColor, destinationColor, slowColor):
    counter = 0
    startRect.cost = 0
    priorityQueue = [(startRect.cost, 0, counter, startRect)]
    checkedRect = []
    destination = utils.getDest(UI.rectField.RectField.listOfRects, utils.YELLOW)
    
    # These dictionaries hold the inforamtions to every rectangle.
    distance = {startRect: 0}
    previousRect = {startRect: None}
    
    # Goes over every node and takes every time that node, which takes the smallest value. 
    # That's why the algorythm uses heap and pops always from the beginning.
    while priorityQueue:
        currentItem = heapq.heappop(priorityQueue)
        (currentCost, placeHolder1, placeHolder2, rect) = currentItem

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

            rectHeuristik = heuristik(neighbour, destination) * rectCost(neighbour, slowColor)
            neighbour.cost = 1
            neighbour.cost += rectHeuristik
            neighbour.cost += currentCost

            if (neighbour not in distance) or (neighbour.cost < distance[neighbour]):
                distance[neighbour] = neighbour.cost
                previousRect[neighbour] = rect
                counter += 1
                heapq.heappush(priorityQueue, (neighbour.cost, rectHeuristik, counter, neighbour))
        
        
        utils.drawPath(checkedRect, utils.GREY, utils.DARKGREY)

    if len(priorityQueue) == 0:
        return checkedRect, False    
    else:  
        path = []
        while rect != None:
            pathRect = rect
            path.append(pathRect)
            rect = previousRect[rect]
        path.reverse()

        return path, True
