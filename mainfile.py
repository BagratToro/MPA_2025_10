import pygame
import UI.rectField
import UI.buttons
import UI.output
import utils
import aStar.dijkstra
import aStar.aStar
import sys

pygame.init()

# Getting the width and height of the monitor.
monitor = pygame.display.Info()

# Creating all the fields in terms of the outputSpace.
outputSpace = monitor.current_h / 12
buttonSpace = 2 * outputSpace
squareScreenHeight = monitor.current_h - buttonSpace - 2 * outputSpace
squareScreenWidth = monitor.current_h - buttonSpace - 2 * outputSpace
numRows = 20
numColumns = 20
screenWidth = monitor.current_h - 2 * outputSpace - buttonSpace
screenHeight = monitor.current_h - outputSpace
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

# Getting the coordinates of the mouse.
mousePos = pygame.mouse.get_pos()

# The grid for rectangles.
grid = UI.rectField.RectField(screen = screen, numColumns = numColumns, numRows = numRows, rectWidth = squareScreenHeight / numColumns, rectHeight = squareScreenHeight / numRows, 
                              xReset = 0, yReset = 0, color = utils.WHITE, mousePos = mousePos)

# Here are all button objects.
Start = UI.buttons.Button(screen = screen, leftX = 0, topY = squareScreenHeight + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = True, displayedText = 'Start', function = utils.clearPath)
Finish = UI.buttons.Button(screen = screen, leftX = squareScreenWidth / 2, topY = squareScreenHeight + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = True, displayedText = 'Finish', function = utils.clearPath)

Obstacle = UI.buttons.Button(screen = screen, leftX = 0, topY = squareScreenHeight + buttonSpace / 4 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = True, displayedText = 'Obstacle', function = utils.clearPath)
Mud = UI.buttons.Button(screen = screen, leftX = squareScreenWidth / 2, topY = squareScreenHeight + buttonSpace / 4 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = True, displayedText = 'Mud', function = utils.clearPath)

Delete = UI.buttons.Button(screen = screen, leftX = 0, topY = squareScreenHeight + buttonSpace / 4 * 2 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = True, displayedText = 'Delete', function = utils.clearPath)
Reset = UI.buttons.Button(screen = screen, leftX = squareScreenWidth / 2, topY = squareScreenHeight + buttonSpace / 4 * 2 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = False, displayedText= 'Reset', function = utils.reset)

AStar = UI.buttons.Button(screen = screen, leftX = 0, topY = squareScreenHeight + buttonSpace / 4 * 3 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = False, displayedText = 'AStar', function = aStar.aStar.runAStar)
Dijkstra = UI.buttons.Button(screen = screen, leftX = squareScreenWidth / 2, topY = squareScreenHeight + buttonSpace / 4 * 3 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = False, displayedText = 'Dijkstra', function = aStar.dijkstra.runDijkstra)

# This is the output object.
output = UI.output.Output(screen = screen, leftX = 0, topY = squareScreenHeight, width = screenWidth, height = outputSpace, screenHeight = monitor.current_h)



running = True
while running:
    clock.tick(60)
    mouseInputs = pygame.mouse.get_pressed()

    # Updating the mouse position in the while loop.
    mousePos = pygame.mouse.get_pos()
    grid.mousePos = mousePos
    grid.updateMousePos()
    output.refreshText()
    level = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for button in utils.listOfButtons:
            button.check(event)

        # Checking for all buttons whether a button is pressed/clicked.
        for rect in UI.rectField.RectField.listOfRects:
            if Start.getPressed() == True:
                rect.changeColor(mouseInputs, type = utils.RectType.Start)
                utils.outputDisplayedText='Allows you to select a starting square'
            elif Finish.getPressed() == True:
                rect.changeColor(mouseInputs, type = utils.RectType.Finish)
                utils.outputDisplayedText='Allows you to select a destination square'
            elif Obstacle.getPressed() == True:
                rect.changeColor(mouseInputs, type = utils.RectType.Obstacle)
                utils.outputDisplayedText='Allows you to declare a square as non tresspassable'
            elif Mud.getPressed() == True:
                rect.changeColor(mouseInputs, type = utils.RectType.Mud)
                utils.outputDisplayedText='Allows you to declare a square as a worse path \n(One mud tile is equivalent to five normal tiles)'
            elif Delete.getPressed() == True:
                rect.changeColor(mouseInputs, type = utils.RectType.Blank)
                utils.outputDisplayedText='Allows you to clear a square'
        
    pygame.display.flip()
pygame.quit()
sys.exit()