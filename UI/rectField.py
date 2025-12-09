import UI.rectangle


class RectField:
    def __init__(self, screen, numRectVertical, numRectHorizontal, rectWidth, rectHeight, xReset, yReset, color):
        self.screen = screen
        self.numRectVertical = numRectVertical
        self.numRectHorizontal = numRectHorizontal
        self.rectWidth = rectWidth
        self.rectHeight = rectHeight
        self.yReset = yReset
        self.xReset = xReset
        self.color = color
        RectField.listOfRects = []

    def drawField(self):
        x = self.xReset
        y = self.yReset
        for row in range(1, self.numRectVertical + 1):
            for column in range(1, self.numRectHorizontal + 1):
                self.listOfRects.append(UI.rectangle.Rectangle(self.screen, x, y, self.rectWidth - 1, self.rectHeight - 1, self.color))
                x += self.rectWidth
                # print(self.listOfRect)
                # print([row, column])
            y += self.rectHeight
            x = self.xReset
        y = self.yReset
