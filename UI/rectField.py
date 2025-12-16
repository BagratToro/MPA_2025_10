import UI.rectangle


# Ist die Klasse für das Feld.
class RectField:
    def __init__(self, screen, numRows, numColumns, rectWidth, rectHeight, xReset, yReset, color):
        RectField.numRows = numRows
        RectField.numColumns = numColumns
        RectField.rectWidth = rectWidth
        RectField.rectHeight = rectHeight
        RectField.yReset = yReset
        RectField.xReset = xReset
        RectField.listOfRects = []
        self.screen = screen
        self.color = color
        self.drawField()


    # Zeichnet und fügt der Liste "listOfRects" alle Rechtecke als Objekte zu.
    def drawField(self):
        x = RectField.xReset
        y = RectField.yReset
        for row in range(1, RectField.numRows + 1):
            for column in range(1, RectField.numColumns + 1):
                self.listOfRects.append(UI.rectangle.Rectangle(self.screen, x, y, RectField.rectWidth - 1, RectField.rectHeight - 1, row - 1, column - 1, self.color))
                x += RectField.rectWidth
                # print(self.listOfRect)
                #print([row, column])
            y += RectField.rectHeight
            x = RectField.xReset
        y = RectField.yReset
