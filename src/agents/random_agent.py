import random

class RandomAgent():
    def generate_move(self, board):
        valid_moves = list(board.legal_moves)
        if valid_moves:
            return random.choice(valid_moves)
        return None