
from hochPi89 import Board

def test_hello_world():
    assert True

def test_Board_class_integrity():
    import Board

    assert True


def test_empty_Board_initialize():
    import Board

    board = Board("o", "ooo ooo ooo")
    assert board.rows[0] == [0, 0, 0]
    assert board.rows[1] == [0, 0, 0]
    assert board.rows[2] == [0, 0, 0]

def test_evaluate():

    board = ["XXX......"]
    assert evaluate(board) == "X"


def test_move():
    """ Test the move() method of the Board class.
    
    Given a specific board state the function tests for the best move to make given the current state.
    """
    initial_board_status = 'o.xox..x.'
    best_move_result = 'o.xox.ox.'
    # Initialize board to a certain test state
    test_board = Board('x', initial_board_status)
    # Call the move function
    test_board.move()
    # Check best result
    assert(initial_board_status == best_move_result)
