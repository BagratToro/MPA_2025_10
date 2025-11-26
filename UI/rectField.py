import pygame

pygame.init()


class rectField:
    def __init__(self, screen, sizeHorizontal, sizeVertical):
        self.sizeHorizontal = sizeHorizontal
        self.sizeVertical = sizeVertical
        self.color = color
        self.screen = screen

    def drawField(self):
        self.rect.changeColor()
        pygame.draw.rect(self.screen, self.color, self.rect.objectRect)



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
