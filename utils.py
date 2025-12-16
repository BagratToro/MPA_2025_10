import UI.rectField

# def connections(rect): # i is a object from rectangle
#     # i = UI.rectField.RectField.listOfRects[115]
#     # print(i.row, i.column)
#     rectList = []
#     # connection = []
#     # listOfConnections = []
#     # for i in UI.rectField.RectField.listOfRects:
#     #     if i.column != 20 and :
#     #         listOfConnections.append([i.columnm, i.column + 1])
#     #     if i.row
#     # for j in UI.rectField.RectField.listOfRects:
#         # if ((i.rectNum + 1) == j.rectNum) or ((i.rectNum - 1) == j.rectNum) or ((i.rectNum + UI.rectField.RectField.numRectHorizontal) == j.rectNum) or ((i.rectNum - UI.rectField.RectField.numRectHorizontal) == j.rectNum):
#             # if j.color != (0, 0, 0):
#                 # rectNumList.append(j)
    
#     # For right and left neighbors.
#     if rect.column > 0:
#         rectList.append( UI.rectField.RectField.listOfRects[rect.row * UI.rectField.RectField.numColumns + rect.column - 1])

#     if rect.column < UI.rectField.RectField.numColumns - 1:
#         rectList.append( UI.rectField.RectField.listOfRects[rect.row * UI.rectField.RectField.numColumns + rect.column + 1])

#     # For up  and down neighbors.
#     if rect.row > 0:
#         rectList.append( UI.rectField.RectField.listOfRects[(rect.row - 1) * UI.rectField.RectField.numColumns + rect.column])

#     if rect.row < UI.rectField.RectField.numRows - 1:
#         rectList.append( UI.rectField.RectField.listOfRects[(rect.row + 1) * UI.rectField.RectField.numColumns + rect.column])
    
#     return rectList


# Gibt den oberen Nachbarn eines beliebigen Rechtecks zurück.
def upConnection(rect):
    if rect.row > 0:
        return UI.rectField.RectField.listOfRects[(rect.row - 1) * UI.rectField.RectField.numColumns + rect.column]
    else:
        return None
    
# Gibt den unteren Nachbarn eines beliebigen Rechtecks zurück.
def downConnection(rect):
    if rect.row < UI.rectField.RectField.numRows - 1:
        return UI.rectField.RectField.listOfRects[(rect.row + 1) * UI.rectField.RectField.numColumns + rect.column]
    else:
        return None

# Gibt den linken Nachbarn eines beliebigen Rechtecks zurück.
def leftConnection(rect):
    if rect.column > 0:
        return UI.rectField.RectField.listOfRects[rect.row * UI.rectField.RectField.numColumns + rect.column - 1]
    else:
        return None

# Gibt den rechten Nachbarn eines beliebigen Rechtecks zurück.
def rightConnection(rect):
    if rect.column < UI.rectField.RectField.numColumns - 1:
        return UI.rectField.RectField.listOfRects[rect.row * UI.rectField.RectField.numColumns + rect.column + 1]
    else:
        return None

