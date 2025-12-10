import pygame
pygame.init()

color = "white"

class Rectangle:
    def __init__(self, screen, leftTopX, leftTopY, width, height, rectNum, row, column, color):
        self.color = color
        self.rectNum = rectNum
        self.row = row
        self.column = column
        self.objectRect = pygame.draw.rect(screen, self.color, (leftTopX, leftTopY, width, height))
        
    
    def changeColor(self, letter):
        match letter:
            case "a":
                self.color = "red"
            case "h":
                self.color = "black"
            case _:
                self.color = "white" # Would use (255, 255, 0) for yellow, that is the color for the starting block. I would in general use (a, b, c) for colors

        #if self.objectRect.collidepoint(mouse_pos):
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_RIGHT:
        #             self.color = "red"
            #elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_G:
            #         self.color = "yellow"
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == -pygame.K_LEFT:
            #         self.color = "black"
            # else:
            #     self.color = "white"

#running = True

#WIDTH, HEIGHT = 800, 600

#screen = pygame.display.set_mode((WIDTH, HEIGHT))

#myRectField = rectField(screen, 600, 600, "white")

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#              last_key_pressed = pygame.key.name(event.key)
#         # keys = pygame.key.get_pressed()
#         # print(keys)
#         mouse_pos = pygame.mouse.get_pos()
#         #myRectField.drawField()
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.display.flip()
# pygame.quit
