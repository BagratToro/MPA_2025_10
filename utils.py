import UI.rectField

def connections(): # i is a object from rectangle
    i = UI.rectField.RectField.listOfRects[115]
    # print(i.row, i.column)
    rectNumList = []
    # connection = []
    # listOfConnections = []
    # for i in UI.rectField.RectField.listOfRects:
    #     if i.column != 20 and :
    #         listOfConnections.append([i.columnm, i.column + 1])
    #     if i.row
    # for j in UI.rectField.RectField.listOfRects:
        # if ((i.rectNum + 1) == j.rectNum) or ((i.rectNum - 1) == j.rectNum) or ((i.rectNum + UI.rectField.RectField.numRectHorizontal) == j.rectNum) or ((i.rectNum - UI.rectField.RectField.numRectHorizontal) == j.rectNum):
            # if j.color != (0, 0, 0):
                # rectNumList.append(j)
    if i.column > 0:
        rectNumList.append( UI.rectField.RectField.listOfRects[i.row * UI.rectField.RectField.numColumns + i.column - 1])

    if i.column < UI.rectField.RectField.numColumns - 1:
        rectNumList.append( UI.rectField.RectField.listOfRects[i.row * UI.rectField.RectField.numColumns + i.column + 1])

    if i.row > 0:
        rectNumList.append( UI.rectField.RectField.listOfRects[(i.row - 1) * UI.rectField.RectField.numColumns + i.column])

    if i.row < UI.rectField.RectField.numRows - 1:
        rectNumList.append( UI.rectField.RectField.listOfRects[(i.row + 1) * UI.rectField.RectField.numColumns + i.column])
    
    return rectNumList
