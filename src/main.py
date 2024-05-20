import pygame
import chess
import math

from const import *
from game import Game
from agents import random_agent

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.init()
        pygame.display.set_caption("Chess.ai")
        self.status = True
        self.board = chess.Board()
        self.game = Game()

    def mainloop(self, agent):
        game = self.game
        screen = self.screen
        board = self.board

        while self.status:
            game.show_background(screen)
            if game.moving:
                game.show_valid_moves(screen, valid_moves)
            game.show_pieces(screen, board)

            # check if AI's turn:
            if board.turn == chess.BLACK:
                agent_move = agent(board)
                if agent_move:
                    board.push(agent_move)
                else:
                    game.show_game_over(screen, 'White')
                    self.status = False
                    break

            all_moves = list(board.legal_moves)
            if len(all_moves) == 0:
                game.show_game_over(screen, 'Black')
                self.status = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.status = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    board_pos = (math.floor(mouse_pos[0]/SQUARE_SIZE), math.floor(mouse_pos[1]/SQUARE_SIZE))
                    # index of square, with the bottom left square being index 0
                    square = (7 - board_pos[1]) * 8 + board_pos[0]

                    # show valid moves 
                    if not game.moving:
                        if board.piece_at(square):
                            valid_moves = [m for m in all_moves if m.from_square == square]
                            game.show_valid_moves(screen, valid_moves)
                            game.moving = True
                    # moving a piece
                    else:
                        i = 0
                        while i < len(valid_moves):
                            if valid_moves[i].to_square == square:
                                move = valid_moves[i]
                                break
                            i += 1
                        if i == len(valid_moves):
                            continue
                        board.push(move)
                        square = None
                        game.moving = False
            pygame.display.update()

        pygame.quit()

main = Main()
main.mainloop(random_agent)