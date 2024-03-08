from square import get_square

def test_get_square():
    a = 4
    result = get_square(a)
    assert result == 16
#
# if __name__ == '__main__':
#     print(test_get_square())