import utils
import UI.rectField
# Is a structure which sorts a list automatically from smallest to biggest.
import heapq

def runDijkstra():
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
            path = dijkstra(utils.getStart(UI.rectField.RectField.listOfRects, utils.BLUE), utils.RED, utils.YELLOW, utils.BROWN)
            if path[1] == False:
                utils.drawPath(path[0], utils.GREY, utils.DARKGREEN)
                utils.outputDisplayedText='There is no possible path'
            else:
                utils.drawPath(path[0], utils.GREEN, utils.DARKGREEN)
                utils.outputDisplayedText='Sucessfully ran the Dijkstra algorithm'
        case 1 if numStart == 0:
            utils.outputDisplayedText='You need to select a starting \nsquare to run the Dijkstra algorithm'
        case 0 if numStart == 1:
            utils.outputDisplayedText='You need to select a destination \nsquare to run the Dijkstra algorithm'
        case 0 if numStart == 0:
            utils.outputDisplayedText='You need to select a starting square and \na destination square to run the Dijkstra algorithm'

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
        
    
    if len(priorityQueue) == 0:
        return checkedRect, False
    else:
        rect = utils.getRect(rect.row, rect.column)    
        path = []
        while rect != None:
            pathRect = rect
            path.append(pathRect)
            rect = previousRect[rect]
        path.reverse()

        return path, True

