def test_hello_world():
    assert True

def test_show(input):
    # Check type
    assert isinstance(input, 'something')
    # Check size
    if input.size == 9:
        show_board(input)