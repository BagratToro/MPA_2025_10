import pygame
import UI.rectField
#import UI.rectangle
import UI.buttons
import utils
import aStar.dijkstra
import aStar.aStar
import sys

pygame.init()

screenUpdate = True
buttonSpace = 180 # Must be divisible by 3
outputSpace = 80 # The sum outputSpace + buttonSpace must be equal to 240
monitor = pygame.display.Info()
squareScreenHeight = monitor.current_h - buttonSpace - outputSpace - 100
squareScreenWidth = monitor.current_h - buttonSpace - outputSpace - 100
numRows = 20
numColumns = 20
screenWidth = squareScreenWidth
screenHeight = squareScreenHeight + outputSpace + buttonSpace
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

mousePos = pygame.mouse.get_pos()

grid = UI.rectField.RectField(screen = screen, numColumns = numColumns, numRows = numRows, rectWidth = squareScreenHeight / numColumns, rectHeight = squareScreenHeight / numRows, 
                              xReset = 0, yReset = 0, color = utils.WHITE, mousePos = mousePos)

Start = UI.buttons.Button(screen = screen, leftX = 0, topY = squareScreenHeight + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = True, displayedText = 'Start', function = None)
Finish = UI.buttons.Button(screen = screen, leftX = squareScreenWidth / 2, topY = squareScreenHeight + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = True, displayedText = 'Finish', function = None)
Obstacle = UI.buttons.Button(screen = screen, leftX = 0, topY = squareScreenHeight + buttonSpace / 4 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = True, displayedText = 'Obstacle', function = None)
Mud = UI.buttons.Button(screen = screen, leftX = squareScreenWidth / 2, topY = squareScreenHeight + buttonSpace / 4 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = True, displayedText = 'Mud', function = None)
Delete = UI.buttons.Button(screen = screen, leftX = 0, topY = squareScreenHeight + buttonSpace / 4 * 2 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = True, displayedText = 'Delete', function = utils.clearPath)
Reset = UI.buttons.Button(screen = screen, leftX = squareScreenWidth / 2, topY = squareScreenHeight + buttonSpace / 4 * 2 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = False, displayedText= 'Reset', function = utils.reset)
AStar = UI.buttons.Button(screen = screen, leftX = 0, topY = squareScreenHeight + buttonSpace / 4 * 3 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = False, displayedText = 'AStar', function = aStar.aStar.runAStar)
Dijkstra = UI.buttons.Button(screen = screen, leftX = squareScreenWidth / 2, topY = squareScreenHeight + buttonSpace / 4 * 3 + outputSpace, width = squareScreenWidth / 2, height = buttonSpace / 4, buttonTypeToggle = False, displayedText = 'Dijkstra', function = aStar.dijkstra.runDijkstra)

running = True
while running:
    clock.tick(60)

    mousePos = pygame.mouse.get_pos()
    grid.mousePos = mousePos
    grid.updateMousePos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in UI.buttons.listOfButtons:
            button.check(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for rect in UI.rectField.RectField.listOfRects:
                if Start.getPressed() == True:
                    rect.changeColor(event, type = utils.RectType.Start)
                elif Finish.getPressed() == True:
                    rect.changeColor(event, type = utils.RectType.Finish)
                elif Obstacle.getPressed() == True:
                    rect.changeColor(event, type = utils.RectType.Obstacle)
                elif Mud.getPressed() == True:
                    rect.changeColor(event, type = utils.RectType.Mud)
                elif Delete.getPressed() == True:
                    rect.changeColor(event, type = utils.RectType.Blank)
            
            #if rect.changeColor(event) != None:
                #rect.changeColor(event)
                #clock.tick(5)

        # elif event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_RIGHT:
                # a += 1
     #screen.fill(WHITE)
    pygame.display.flip()
pygame.quit()
sys.exit()