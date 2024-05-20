import pygame
import time

from const import *

class Game:
    def __init__(self):
        self.pieces = {
            'p': pygame.image.load('images/black_pawn.png').convert_alpha(),
            'n': pygame.image.load('images/black_knight.png').convert_alpha(),
            'b': pygame.image.load('images/black_bishop.png').convert_alpha(),
            'r': pygame.image.load('images/black_rook.png').convert_alpha(),
            'q': pygame.image.load('images/black_queen.png').convert_alpha(),
            'k': pygame.image.load('images/black_king.png').convert_alpha(),
            'P': pygame.image.load('images/white_pawn.png').convert_alpha(),
            'N': pygame.image.load('images/white_knight.png').convert_alpha(),
            'B': pygame.image.load('images/white_bishop.png').convert_alpha(),
            'R': pygame.image.load('images/white_rook.png').convert_alpha(),
            'Q': pygame.image.load('images/white_queen.png').convert_alpha(),
            'K': pygame.image.load('images/white_king.png').convert_alpha(),
        }
        self.moving = False

    def show_background(self, screen):
        # draw squares on board
        for row in range(ROWS):
            for col in range(COLS):
                color = LIGHT_SQUARE if (row+col) % 2 == 0 else DARK_SQUARE
                rect = (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(screen, color, rect)

    def show_pieces(self, screen, board):
        # draw pieces on board
        for i in range(64):
            piece = board.piece_at(i)
            if piece != None:
                screen.blit(self.pieces[str(piece)], ((i%8) * SQUARE_SIZE, (HEIGHT-SQUARE_SIZE) - (i//8) * SQUARE_SIZE))

    def show_valid_moves(self, screen, moves):
        # highlight destination squares for each valid move
        for m in moves:
            dest = m.to_square
            row, col = 7 - dest//8, dest%8
            color = LIGHT_HIGHLIGHT if (row+col) % 2 == 0 else DARK_HIGHLIGHT
            rect = (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect)

    def show_game_over(self, screen, winner):
        font = pygame.font.Font(None, 64)
        message = "Game Over, " + winner + " Wins"
        text = font.render(message, True, (255, 255, 255))
        text_rect = text.get_rect(center=(HEIGHT/2, WIDTH/2))
        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)
        pygame.display.update()
        time.sleep(3)