import chess.polyglot

from const import WEIGHTS
from copy import deepcopy

class MinMaxAgent:
    def __init__(self, max_depth):
        self.max_depth = max_depth
        self.opening_book = chess.polyglot.open_reader('/Users/lucianli/Desktop/chess_ai/src/baron30.bin')

    def generate_move(self, board):
        return self.min_max(board, self.max_depth)

    def eval_board(self, board):
        score = 0
        for _, piece in board.piece_map().items():
            score += WEIGHTS[str(piece)]
        return score
    
    # secondary evaluation function, will add a weight between 0 and 1 to final score
    def eval_space(self, board):
        number_of_moves = len(list(board.legal_moves))
        score = number_of_moves / (20 + number_of_moves)
        return score if board.turn else -score

    # generates the best move using the minmax algorithm (max depth of N), 
    # the opening book, a secondary evaluation function, and win conditions
    def min_max(self, board, depth):
        opening_move = self.opening_book.get(board)
        if opening_move is not None:
            return opening_move.move
        
        valid_moves = list(board.legal_moves)
        if not valid_moves:
            return None

        min_score, max_score = float('inf'), float('-inf')
        min_score_index, max_score_index = 0, 0
        for i in range(len(valid_moves)):
            temp_board = deepcopy(board)
            temp_board.push(valid_moves[i])

            # check win conditions
            outcome = temp_board.outcome()

            # no checkmate
            if outcome is None:
                if depth > 1:
                    temp_best_move = self.min_max(temp_board, depth-1)
                    if temp_best_move:
                        temp_board.push(temp_best_move)
                score = self.eval_board(temp_board)
            # checkmate
            elif temp_board.is_checkmate():
                return valid_moves[i]
            # stalemate
            else:
                score = 1000 if self.board.turn == True else -1000

            # secondary evaluation function
            score += self.eval_space(temp_board)
            if board.turn == True and score > max_score:
                max_score, max_score_index = score, i
            elif board.turn == False and score < min_score:
                min_score, min_score_index = score, i
        
        if board.turn == True:
            best_move = valid_moves[max_score_index]
        else:
            best_move = valid_moves[min_score_index]
        
        return best_move
