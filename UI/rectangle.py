import pygame
#import aStar.dijkstra
#import aStar.aStar
import utils
pygame.init()


#The class for a single rectangle. (Ist die Klasse für jedes einzelne Rechteck.)
class Rectangle:
    def __init__(self, screen, leftTopX, leftTopY, width, height, row, column, color, mousePos):
        self.mousePos = mousePos
        self.screen = screen
        self.rect = (leftTopX, leftTopY, width, height)
        self.color = color
        self.row = row
        self.column = column
        self.objectRect = pygame.draw.rect(screen, self.color, (leftTopX, leftTopY, width, height))
        self.cost = float("inf")
        # self.processing = False
        # self.visited = False

    # def __eq__(self, other):
    #     return isinstance(other, Rectangle) and self.row == other.row and self.column == other.column
    
    # def __hash__(self):
    #     return hash((self.row, self.column))


    #Changes the color of a rectangle based on the input of the user. (Verändert die Farbe eines Rechtecks anhand von Eingaben des Users.)
    def changeColor(self, event, type):
        if self.objectRect.collidepoint(self.mousePos):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                match type:
                    case utils.RectType.Start:
                        self.color = utils.BLUE #blue
                    case utils.RectType.Finish:
                        self.color = utils.YELLOW #yellow
                    case utils.RectType.Obstacle:
                        self.color = utils.RED #red
                    case utils.RectType.Mud:
                        self.color = utils.BROWN #brown
                    case utils.RectType.Blank:
                        self.color = utils.WHITE #white
                #elif event.key == pygame.K_m:
                    #self.color = utils.BROWN

        self.objectRect = pygame.draw.rect(self.screen, self.color, self.rect)


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
