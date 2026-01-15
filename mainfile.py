import pygame
import UI.rectField
import UI.buttons
import UI.textbox
import utils
import aStar.dijkstra
import aStar.aStar
import sys

pygame.init()

screenUpdate = True
monitor = pygame.display.Info()
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

mousePos = pygame.mouse.get_pos()

grid = UI.rectField.RectField(screen = screen, numColumns = numColumns, numRows = numRows, rectWidth = squareScreenHeight / numColumns, rectHeight = squareScreenHeight / numRows, 
                              xReset = 0, yReset = 0, color = utils.WHITE, mousePos = mousePos)

Start = UI.buttons.Button(screen = screen, leftX = 0, topY = squareScreenHeight + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = True, displayedText = 'Start', function = utils.clearPath)
Finish = UI.buttons.Button(screen = screen, leftX = squareScreenWidth / 2, topY = squareScreenHeight + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = True, displayedText = 'Finish', function = utils.clearPath)

Obstacle = UI.buttons.Button(screen = screen, leftX = 0, topY = squareScreenHeight + buttonSpace / 4 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = True, displayedText = 'Obstacle', function = utils.clearPath)
Mud = UI.buttons.Button(screen = screen, leftX = squareScreenWidth / 2, topY = squareScreenHeight + buttonSpace / 4 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = True, displayedText = 'Mud', function = utils.clearPath)
Delete = UI.buttons.Button(screen = screen, leftX = 0, topY = squareScreenHeight + buttonSpace / 4 * 2 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = True, displayedText = 'Delete', function = utils.clearPath)

Reset = UI.buttons.Button(screen = screen, leftX = squareScreenWidth / 2, topY = squareScreenHeight + buttonSpace / 4 * 2 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = False, displayedText= 'Reset', function = utils.reset)
AStar = UI.buttons.Button(screen = screen, leftX = 0, topY = squareScreenHeight + buttonSpace / 4 * 3 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = False, displayedText = 'AStar', function = aStar.aStar.runAStar)
Dijkstra = UI.buttons.Button(screen = screen, leftX = squareScreenWidth / 2, topY = squareScreenHeight + buttonSpace / 4 * 3 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = False, displayedText = 'Dijkstra', function = aStar.dijkstra.runDijkstra)

textbox = UI.textbox.TextBox(screen = screen, leftX = 0, topY = squareScreenHeight, width = screenWidth, height = outputSpace, screenHeight = monitor.current_h)



running = True
while running:
    clock.tick(60)
    mouseInputs = pygame.mouse.get_pressed()

    mousePos = pygame.mouse.get_pos()
    grid.mousePos = mousePos
    grid.updateMousePos()
    textbox.drawsurface()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in utils.listOfButtons:
            button.check(event)
        
        for rect in UI.rectField.RectField.listOfRects:
            if Start.getPressed() == True:
                rect.changeColor(event, mouseInputs, type = utils.RectType.Start)
                utils.textboxDisplayedText='Allows you to select a starting square'
            elif Finish.getPressed() == True:
                rect.changeColor(event, mouseInputs, type = utils.RectType.Finish)
                utils.textboxDisplayedText='Allows you to select a destination square'
            elif Obstacle.getPressed() == True:
                rect.changeColor(event, mouseInputs, type = utils.RectType.Obstacle)
                utils.textboxDisplayedText='Allows you to declare a square as non tresspassable'
            elif Mud.getPressed() == True:
                rect.changeColor(event, mouseInputs, type = utils.RectType.Mud)
                utils.textboxDisplayedText='Allows you to declare a square as a worse path \n(One mud tile is equivalent to five normal tiles)'
            elif Delete.getPressed() == True:
                rect.changeColor(event, mouseInputs, type = utils.RectType.Blank)
                utils.textboxDisplayedText='Allows you to clear a square'

    pygame.display.flip()
pygame.quit()
sys.exit()