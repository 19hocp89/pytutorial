def test_hello_world():
    assert True


def test_Board_class_integrity():
    import Board

    assert True


def test_empty_Board_initialize():
    import Board

    board = Board("o", "ooooooooo")
    assert board.positions == ["o", "o", "o", "o", "o", "o", "o", "o", "o"]
