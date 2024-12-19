
def test_hello_world():
    assert True

def test_move():
    initial_board_status = 'o.xox..x.'
    best_move_result = 'o.xox.ox.'
    # Initialize board to a certain test state
    test_board = Board('x', initial_board_status)
    # Call the move function
    test_board.move()
    # Check best result
    assert(initial_board_status == best_move_result)