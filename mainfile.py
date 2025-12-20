import pygame
import UI.rectField
import UI.rectangle
import utils
import aStar.dijkstra
pygame.init()
screenUpdate = True
squareScreenHeight = 700
squareScreenWidth = 700
numRows = 4
numColumns = 4
buttonSpace = 100
screenWidth = squareScreenWidth
screenHeight = squareScreenHeight + buttonSpace
screen = pygame.display.set_mode((screenWidth, screenHeight))
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
mousePos = pygame.mouse.get_pos()

grid = UI.rectField.RectField(screen = screen, numColumns = numColumns, numRows = numRows, rectWidth = squareScreenHeight / numColumns, rectHeight = squareScreenHeight / numRows, 
                              xReset = 0, yReset = 0, color = WHITE, mousePos = mousePos)


running = True
while running:
    mousePos = pygame.mouse.get_pos()
    grid.mousePos = mousePos
    grid.updateMousePos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for rect in UI.rectField.RectField.listOfRects:
                if rect.changeColor(event) != None:
                    rect.changeColor(event)
    

    startRect = UI.rectField.RectField.listOfRects[0]
    destRect = UI.rectField.RectField.listOfRects[15]
    obstacle1 = UI.rectField.RectField.listOfRects[5]
    obstacle2 = UI.rectField.RectField.listOfRects[7]
    obstacle1.color = GREY
    obstacle2.color = GREY
    # for obstacle in range(100, 119):
    #      UI.rectField.RectField.listOfRects[obstacle].color = GREY
    # for obstacle in range(150, 160):
    #      UI.rectField.RectField.listOfRects[obstacle].color = GREY
    # for obstacle in range(210, 220):
    #      UI.rectField.RectField.listOfRects[obstacle].color = GREY
    # for obstacle in range(220, 223):
    #      UI.rectField.RectField.listOfRects[obstacle].color = GREY
    # for obstacle in range(226, 229):
    #      UI.rectField.RectField.listOfRects[obstacle].color = GREY
    # for obstacle in range(250, 253):
    #      UI.rectField.RectField.listOfRects[obstacle].color = GREY
    startRect.color = BLUE
    destRect.color = YELLOW

    # for i in aStar.dijkstra.dijkstra(startRect, GREY, YELLOW):
    #      if i[1]:
    #           print(i)
    # print(aStar.dijkstra.dijkstra(startRect, GREY, YELLOW))
    aStar.dijkstra.dijkstra(startRect, GREY, YELLOW)
    
    # aStar.dijkstra.dijkstra(i)
    # connections = utils.connections(i)
    # for connection in connections:
    #     print([connection.row, connection.column])
    
        # elif event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_RIGHT:
                # a += 1
     #screen.fill(WHITE)
    pygame.display.flip()
pygame.quit()