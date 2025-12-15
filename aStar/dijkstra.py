import utils
import UI.rectField


def distance(rect):
    utils.connections(rect)





def dijkstra():
    listOfRects = UI.rectField.RectField.listOfRects
    listOfVisitedRects = []
    listOfUnvisitedRects = [listOfRects]

    for rect in listOfUnvisitedRects:
        if rect.color == (255, 255, 0): #yellow
            return 
        if rect.color == (255, 165, 0): #orange
            endRect = rect
        if rect.color == (128, 128, 128): #grey
            return 
    
    

            

