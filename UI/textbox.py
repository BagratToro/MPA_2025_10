import pygame
import utils
pygame.init()


class TextBox:
    def __init__(self, rect, screen, leftX, topY, width, height, font):
        self.rect = rect
        self.screen = screen
        self.leftX = leftX
        self.topY = topY
        self.widht = width
        self.height = height
        self.font = font

        self.line_height = font.get_height()
        self.lines = []
        self.start = 0
        self.gap = 5

    def add_text(self, text):
        for line in text.split("\n"):
            self.lines.append(line)

    def scroll(self, event):
        if event.type == pygame.MOUSEWHEEL:
            self.start -= event.y
            self.start = max(0, min(self.start, max(0, len(self.lines) - self.visible_lines())))

    def visible_lines(self):
        return (self.rect.height - 2 * self.gap) // self.line_height

    def draw(self, surface, topY):
        pygame.draw.rect(surface, utils.BLACK, self.rect)
        pygame.draw.rect(surface, utils.GREY, self.rect, 2)

        start = self.start
        end = start + self.visible_lines()
        y = topY + self.gap

        for line in self.lines[start:end]:
            txt_surf = pygame.font.SysFont('Arial', 20).render(line, True, utils.BLACK)
            surface.blit(txt_surf, (self.rect.x + self.gap, y))
            y += self.line_height

textbox = TextBox(pygame.Rect(50, 50, 600, 300), font)

for i in range(1, 31):
     textbox.add_text(f"Log-Eintrag Nummer {i}")

clock = pygame.time.Clock()
running = True
counter = 31

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        textbox.handle_event(event)

        # Taste drücken → Text ändern
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                textbox.add_text(f"Neuer Eintrag {counter}")
                counter += 1

    screen.fill(WHITE)
    textbox.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()