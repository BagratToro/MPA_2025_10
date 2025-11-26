import pygame
import UI
pygame.init()

screenUpdate = True
squareScreenHeight = 700
squareScreenWidth = 700
numRows = 20
numColumns = 20
buttonSpace = 100
screenWidth = squareScreenWidth
screenHeight = squareScreenHeight + buttonSpace
screen = pygame.display.set_mode((screenWidth, screenHeight))
WHITE = (255, 255, 255)
mousePos = pygame.mouse.get_pos()

grid = UI.Grid(screen = screen, rectHeight = squareScreenWidth / numRows, rectWidth = squareScreenHeight / numColumns, 
                     numRows = numRows, numColumns = numColumns, startX = 0, startY = 0, color = WHITE, mousePos = mousePos)

running = True
while running:
    mousePos = pygame.mouse.get_pos()
    # rect = UI.Rects(screen = screen, rectHeight = squareScreenWidth / numRectHeight, rectWidth = squareScreenHeight / numRectWidth, 
    #                 numRectWidth = numRectWidth, numRectHeight = numRectHeight, startX = 0, startY = 0, color = WHITE, mousePos = mousePos)
    grid.mousePos = mousePos
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if screenUpdate:
        screenUpdate = False
    
    grid.render()
    
        # elif event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_RIGHT:
                # a += 1
     # screen.fill(WHITE)
    pygame.display.flip()
pygame.quit()