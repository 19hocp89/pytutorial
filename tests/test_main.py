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
