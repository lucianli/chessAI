import pygame

from const import *

class Load:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 60)

    def draw_button(self, rect, text):
        pygame.draw.rect(self.screen, WHITE, rect)
        text_surface = self.font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def show_load_screen(self):
        easy_button = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, 150, BUTTON_WIDTH, BUTTON_HEIGHT)
        medium_button = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, 150 + BUTTON_HEIGHT + BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT)
        hard_button = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, 150 + 2 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT)

        while True:
            self.screen.fill(BLACK)

            self.draw_button(easy_button, "Easy")
            self.draw_button(medium_button, "Medium")
            self.draw_button(hard_button, "Hard")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_button.collidepoint(event.pos):
                        return "Easy"
                    elif medium_button.collidepoint(event.pos):
                        return "Medium"
                    elif hard_button.collidepoint(event.pos):
                        return "Hard"

            pygame.display.update()