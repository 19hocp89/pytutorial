def hello_world():
    print("Hello World!")

def evaluate(board):

    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontale Linien
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertikale Linien
        [0, 4, 8], [2, 4, 6]  # diagonale Linien
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ".":
            return True 
    
    return False
