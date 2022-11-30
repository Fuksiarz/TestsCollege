from unittest import mock

import pytest

from app.sample import guess_number


@pytest.mark.parametrize("_input,expected", [(3, "You won!"), (4, "You lost!")])
@mock.patch("siema.app.sample.roll_dice")
def test_guess_number(mock_roll_dice, _input, expected):
    mock_roll_dice.return_value = 3
    assert guess_number(_input) == expected
    mock_roll_dice.assert_called_once()
