from const import WEIGHTS
from copy import deepcopy

class SimpleMinMaxAgent:
    def generate_move(self, board):
        N = 2
        return self.min_max(board, N)

    def eval_board(self, board):
        score = 0
        for _, piece in board.piece_map().items():
            score += WEIGHTS[str(piece)]
        return score

    # generates the best move using the minmax algorithm and a maximum depth of N
    def min_max(self, board, N):
        valid_moves = list(board.legal_moves)
        if not valid_moves:
            return None

        min_score, max_score = float('inf'), float('-inf')
        min_score_index, max_score_index = 0, 0
        for i in range(len(valid_moves)):
            temp_board = deepcopy(board)
            temp_board.push(valid_moves[i])

            if N > 1:
                temp_best_move = self.min_max(temp_board, N-1)
                if temp_best_move:
                    temp_board.push(temp_best_move)

            temp_score = self.eval_board(temp_board)
            if board.turn == True and temp_score >= max_score:
                max_score = temp_score
                max_score_index = i
            elif board.turn == False and temp_score <= min_score:
                min_score = temp_score
                min_score_index = i
            
        if board.turn == True:
            best_move = valid_moves[max_score_index]
        else:
            best_move = valid_moves[min_score_index]

        return best_move