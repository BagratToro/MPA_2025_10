import pygame

pygame.init()



x = 0
y = 0
mouse_pos = pygame.mouse.get_pos()
height = 100
width = 100
last_key_pressed = None
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        last_key_pressed = event.key


class rect:
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color
        self.objectRect = pygame.Rect(x, y, self.width, self.height)
    
    def changeColor(self):
        if last_key_pressed == pygame.K_a:
            self.color = "red"
        if last_key_pressed == pygame.K_h:
            self.color = "black"
        else:
            self.color = "white"
        print(mouse_pos)
        print(last_key_pressed)
        print(self.color)
        return self.color
        # if self.objectRect.collidepoint(mouse_pos):
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



while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
             last_key_pressed = pygame.key.name(event.key)
        # keys = pygame.key.get_pressed()
        # print(keys)
        mouse_pos = pygame.mouse.get_pos()
        myRectField.drawField()
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit
