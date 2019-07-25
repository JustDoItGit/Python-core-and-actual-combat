from unittest.mock import MagicMock


def side_effect(arg):
    if arg < 0:
        return 1
    else:
        return 2


mock = MagicMock()
mock.side_effect = side_effect

print(mock(-1))
print(mock(1))
