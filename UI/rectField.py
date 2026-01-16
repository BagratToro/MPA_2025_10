import UI.rectangle


#The class for the whole grid/field. (Ist die Klasse für das Feld.)
class RectField:
    def __init__(self, screen, numRows, numColumns, rectWidth, rectHeight, xReset, yReset, color, mousePos):
        RectField.numRows = numRows
        RectField.numColumns = numColumns
        RectField.rectWidth = rectWidth
        RectField.rectHeight = rectHeight
        RectField.yReset = yReset
        RectField.xReset = xReset
        RectField.listOfRects = []
        RectField.screen = screen
        self.color = color
        self.mousePos = mousePos
        self.drawField()


    # Draws all rectangles and adds them to the "listofRects"as objects.
    def drawField(self):
        x = RectField.xReset
        y = RectField.yReset
        for row in range(1, RectField.numRows + 1):
            for column in range(1, RectField.numColumns + 1):
                self.listOfRects.append(UI.rectangle.Rectangle(self.screen, x, y, RectField.rectWidth - 1, RectField.rectHeight - 1, row - 1, column - 1, self.color, self.mousePos))
                x += RectField.rectWidth
            y += RectField.rectHeight
            x = RectField.xReset
        y = RectField.yReset

    # Updating the mousePosition for every rectangle.
    def updateMousePos(self):
        for rect in self.listOfRects:
            rect.mousePos = self.mousePos