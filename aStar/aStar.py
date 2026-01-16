import heapq
import utils
import UI.rectField

def runAStar():
    numDest = 0
    numStart = 0
    # Resetting every button after starting the algorithm.
    for button in utils.listOfButtons:
        button.pressed = False
    utils.clearPath()
    # Looking for the number of starts and destinations.
    for rect in UI.rectField.RectField.listOfRects:
        if rect.color == utils.BLUE:
            numStart += 1
        if rect.color == utils.YELLOW:
            numDest += 1
    # Checking for every number of starts and destinations.
    match numDest:
        case 1 if numStart == 1:
            path = aStar(utils.getStart(UI.rectField.RectField.listOfRects, utils.BLUE), utils.RED, utils.YELLOW, utils.BROWN)
            if path[1] == False:
                utils.drawPath(path[0], utils.GREY, utils.DARKGREEN)
                utils.outputDisplayedText='There is no possible path'
            else:
                utils.drawPath(path[0], utils.GREEN, utils.DARKGREEN)
                utils.outputDisplayedText='Sucessfully ran the A* algorithm'
        case 1 if numStart == 0:
            utils.outputDisplayedText='You need to select a starting \nsquare to run the A* algorithm'
        case 0 if numStart == 1:
            utils.outputDisplayedText='You need to select a destination \nsquare to run the A* algorithm'
        case 0 if numStart == 0:
            utils.outputDisplayedText='You need to select a starting square and \na destination square to run the A* algorithm'

# Calculating the cost of a rectangle with a normal color and a slow color.
def rectCost(rect, slowColor):
    if rect.color == slowColor:
        return 7
    return 1

# This is the heuristik with the manhatten grid.
def heuristik(rect, destination):
    cost = 0
    cost = abs(rect.row - destination.row) + abs(rect.column - destination.column) 
    return cost

# The actual algorithm.
def aStar(startRect, obstacleColor, destinationColor, slowColor):
    counter = 0
    startRect.cost = 0
    # Creating the priorityQueue which will sort from the smallest item to the largest item.
    priorityQueue = [(startRect.cost, 0, counter, startRect)]
    # Creating a list of checked rectangles.
    checkedRect = []
    destination = utils.getDest(UI.rectField.RectField.listOfRects, utils.YELLOW)
    
    # These dictionaries hold the inforamtions to every rectangle.
    # cost holds the cost for every rect.
    # previousRect holds the rect, from which the algorithm reached the rect.
    cost = {startRect: 0}
    previousRect = {startRect: None}
    previousRect[destination] = None
    
    # Goes over every node and takes every time that node, which takes the smallest value. 
    # That's why the algorythm uses heap and pops always from the beginning.
    while priorityQueue:
        currentItem = heapq.heappop(priorityQueue)
        (currentCost, placeHolder1, placeHolder2, rect) = currentItem

        # The while loop should end, whenever it gets to the destination -> *früh stopp* Dijkstra !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if rect.color == destinationColor:
            break
        
        # When it costs more, to get to that node via a another path, the path should be ignored.
        if currentCost > cost[rect]:
            continue

        checkedRect.append(rect)

        # Now comparing all neighbours of that rectangle.
        listOfNeighbours = (utils.connection(rect, utils.Neighbour.LEFT), utils.connection(rect, utils.Neighbour.UP), utils.connection(rect, utils.Neighbour.RIGHT), utils.connection(rect, utils.Neighbour.DOWN))
        # Before calculating the cost for every neighbour, this for-loop checks if it's passable.
        for neighbour in listOfNeighbours:
            if neighbour == None:
                continue
            if neighbour.color == obstacleColor:
                continue

            # Calculating the cost for the neighbour.
            rectHeuristik = heuristik(neighbour, destination) * rectCost(neighbour, slowColor)
            neighbour.cost = 1
            neighbour.cost += rectHeuristik
            neighbour.cost += currentCost

            # Checking if the neighbour is in the cost or smaller than the value in stored in the cost.
            if (neighbour not in cost) or (neighbour.cost < cost[neighbour]):
                cost[neighbour] = neighbour.cost
                previousRect[neighbour] = rect
                counter += 1
                heapq.heappush(priorityQueue, (neighbour.cost, rectHeuristik, counter, neighbour))
        
        # Drawing all checked rectangles grey.
        utils.drawPath(checkedRect, utils.GREY, utils.DARKGREY)

    # This if-Statement is for the case, that the priorityQueue is empty without getting to the destination.
    if previousRect[destination] == None:
        return checkedRect, False
    else:
        # Calculating the path via going back with the previousRect.
        path = []
        while rect != None:
            pathRect = rect
            path.append(pathRect)
            rect = previousRect[rect]
        path.reverse()

        return path, True
