def test_hello_world():
    assert True

def test_show(input):
    assert isinstance(input, 'something')
    if input.size == 9:
        show_board(input)