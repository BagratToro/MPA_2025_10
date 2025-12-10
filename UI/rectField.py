import UI.rectangle


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

    def drawField(self):
        x = RectField.xReset
        y = RectField.yReset
        rectNum = 0
        for row in range(1, RectField.numRows + 1):
            for column in range(1, RectField.numColumns + 1):
                self.listOfRects.append(UI.rectangle.Rectangle(self.screen, x, y, RectField.rectWidth - 1, RectField.rectHeight - 1, rectNum, row - 1, column - 1, self.color))
                rectNum += 1
                x += RectField.rectWidth
                # print(self.listOfRect)
                #print([row, column])
            y += RectField.rectHeight
            x = RectField.xReset
        y = RectField.yReset
