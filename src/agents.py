import random

def random_agent(board):
    valid_moves = list(board.legal_moves)
    if valid_moves:
        return random.choice(valid_moves)
    return None