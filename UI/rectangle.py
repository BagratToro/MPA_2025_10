import pygame
pygame.init()



# Ist die Klasse für jedes einzelne Rechteck.
class Rectangle:
    def __init__(self, screen, leftTopX, leftTopY, width, height, row, column, color):
        self.screen = screen
        self.rect = (leftTopX, leftTopY, width, height)
        self.color = color
        self.row = row
        self.column = column
        self.objectRect = pygame.draw.rect(screen, self.color, (leftTopX, leftTopY, width, height))


    # Verändert die Farbe eines Rechtecks anhand von Eingaben des Users.
    def changeColor(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                self.color = (255, 0, 0) #red
                print(self.color)
            elif event.key == pygame.K_s:
                self.color = (0, 0, 255) #blue
                print("Rechts")
            elif event.key == pygame.K_f:
                self.color = (255, 255, 0) #yellow
                print("ESC gedrückt")

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
