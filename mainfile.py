import pygame
import UI.rectField
import UI.rectangle
import UI.buttons
import utils
import aStar.dijkstra
import sys
pygame.init()
screenUpdate = True
squareScreenHeight = 700
squareScreenWidth = 700
numRows = 20
numColumns = 20
buttonSpace = 200
screenWidth = squareScreenWidth
screenHeight = squareScreenHeight + buttonSpace
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

mousePos = pygame.mouse.get_pos()

def testFunction():
    print('HelloWorld!')

grid = UI.rectField.RectField(screen = screen, numColumns = numColumns, numRows = numRows, rectWidth = squareScreenHeight / numColumns, rectHeight = squareScreenHeight / numRows, 
                              xReset = 0, yReset = 0, color = utils.WHITE, mousePos = mousePos)

button1 = UI.buttons.Button(screen = screen, leftX = 0, topY = 700, width = 300, height = 100, buttonTypeToggle = False, function = testFunction, displayedText = 'button1')
button2 = UI.buttons.Button(screen = screen, leftX = 300, topY = 700, width = 300, height = 100, buttonTypeToggle = False, function = testFunction, displayedText = 'button2')

running = True
while running:
    clock.tick(30)

    mousePos = pygame.mouse.get_pos()
    grid.mousePos = mousePos
    grid.updateMousePos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in UI.buttons.listOfButtons:
            button.check()
        for rect in UI.rectField.RectField.listOfRects:
            if rect.changeColor(event) != None:
                rect.changeColor(event)
                clock.tick(5)
    
        # elif event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_RIGHT:
                # a += 1
     #screen.fill(WHITE)
    pygame.display.flip()
pygame.quit()
sys.exit()