import rectangle


class rectField:
    def __init__(self, screen, sizeHorizontal, sizeVertical):
        self.sizeHorizontal = sizeHorizontal
        self.sizeVertical = sizeVertical
        self.screen = screen

    def drawField(self, numRectVertical, numRectHorizontal, rectWidth, rectHeight, y, xReset, color):
        x = xReset
        listOfRect = []
        for k in range(1, numRectVertical + 1):
            for j in range(1, numRectHorizontal + 1):
                rectangle(self.screen, color, (x, y, rectWidth - 1, rectHeight - 1))
                listOfRect.append([x, y, rectWidth - 1, rectHeight - 1, color])
                x += rectWidth
            y += rectHeight
            x = xReset