import unittest
from unittest import mock
import io

from game import Game
from unittest.mock import patch

game = Game


def test_set_map():
    game.createMap(5, 6)
    assert game.createMap(5, 6) == [[0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0]]


def test_set_start_and_stop():
    A = 5
    B = 5
    board = game.createMap(A, B)
    boardWithStartAndStop = game.createStartAndStop(board, A, B)
    x = any('W' and 'S' in sublist for sublist in boardWithStartAndStop)
    assert x == True


def test_set_obstacles():
    A = 5
    B = 5
    board = game.createMap(A, B)
    boardWithStartAndStop = game.createStartAndStop(board, A, B)
    boardWithObstacles = game.createObstacles(boardWithStartAndStop, A, B)
    x = any(1 in sublist for sublist in boardWithObstacles)
    assert x == True


def test_where_is_start_and_stop():
    A = 5
    B = 5
    board = game.createMap(A, B)
    boardWithStartAndStop = game.createStartAndStop(board, A, B)

    for i in range(B):
        for j in range(A):
            if boardWithStartAndStop[i][j] == 'W':
                koniecX = i
                koniecY = j
            if boardWithStartAndStop[i][j] == 'S':
                startX = i
                startY = j
                break
    whereIs = game.whereIsSAndW(boardWithStartAndStop, A, B)
    answer = (startX, startY, koniecX, koniecY)
    assert answer == whereIs


# @patch('builtins.input', lambda _: 'W')
def test_move_up_when_on_top_edge():
    A = 5
    B = 5
    board = [[0, 0, 1, 0, 'S'],  # 0,4
             ['W', 0, 0, 1, 0],  # 1,0
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0]]
    position = game.whereIsSAndW(board, A, B)
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
        with mock.patch('builtins.input', return_value="W"):
            game.move(A, B, board, position[0], position[1], position[2], position[3], 0)

            assert fake_out.getvalue() == "Nie mozna wyjsc za planszę!\n[0, 0, 1, 0, 'S']\n['W', 0, 0, 1, 0]\n[0, 0, 0, 0, 0]\n[0, 0, 0, 0, 0]\n[0, 0, 0, 1, 0]\n"

    # position = game.whereIsSAndW(board, A, B)
    # captured = capsys.readouterr()
    # assert game.move(A, B, board, position[0], position[1], position[2], position[3].readouterr == "ok"
    # print(captured)
    # monkeypatch.setattr('builtins.input', lambda _: "A")
    #
    # # with mock.patch('sys.stdout', new='W') as fake_stdout:
    # #     game.move(A, B, board, position[0], position[1], position[2], position[3])
    # #
    # # assert fake_stdout.getvalue() == 'Something\n'
    # assert game.move(A, B, board, position[0], position[1], position[2], position[3]) == "[0, 0, 1, 0, 'S']['W', 0, 0, 1, 0][0, 0, 0, 0, 0][0, 0, 0, 0, 0][0, 0, 0, 1, 0](0, 4, 1, 0)Nie mozna wyjsc za planszę!"


def test_move_down_when_on_bot_edge():
    A = 5
    B = 5
    board = [[0, 0, 1, 0, 0],  # 0,4
             ['W', 0, 0, 1, 0],  # 1,0
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 1, 'S']]
    position = game.whereIsSAndW(board, A, B)
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
        with mock.patch('builtins.input', return_value="S"):
            game.move(A, B, board, position[0], position[1], position[2], position[3], 0)

            assert fake_out.getvalue() == "Nie mozna wyjsc za planszę!\n[0, 0, 1, 0, 0]\n['W', 0, 0, 1, 0]\n[0, 0, 0, 0, 0]\n[0, 0, 0, 0, 0]\n[0, 0, 0, 1, 'S']\n"


def test_move_left_when_on_left_edge():
    A = 5
    B = 5
    board = [[0, 0, 1, 0, 0],  # 0,4
             ['W', 0, 0, 1, 0],  # 1,0
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             ['S', 0, 0, 1, 0]]
    position = game.whereIsSAndW(board, A, B)
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
        with mock.patch('builtins.input', return_value="A"):
            game.move(A, B, board, position[0], position[1], position[2], position[3], 0)

            assert fake_out.getvalue() == "Nie mozna wyjsc za planszę!\n[0, 0, 1, 0, 0]\n['W', 0, 0, 1, 0]\n[0, 0, 0, 0, 0]\n[0, 0, 0, 0, 0]\n['S', 0, 0, 1, 0]\n"


def test_move_right_when_on_right_edge():
    A = 5
    B = 5
    board = [[0, 0, 1, 0, 0],  # 0,4
             ['W', 0, 0, 1, 0],  # 1,0
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 1, 'S']]
    position = game.whereIsSAndW(board, A, B)
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
        with mock.patch('builtins.input', return_value="D"):
            game.move(A, B, board, position[0], position[1], position[2], position[3], 0)

            assert fake_out.getvalue() == "Nie mozna wyjsc za planszę!\n[0, 0, 1, 0, 0]\n['W', 0, 0, 1, 0]\n[0, 0, 0, 0, 0]\n[0, 0, 0, 0, 0]\n[0, 0, 0, 1, 'S']\n"


def test_move_up_when_there_is_obstacle():
    A = 5
    B = 5
    board = [[0, 0, 1, 0, 0],  # 0,4
             ['W', 0, 0, 1, 0],  # 1,0
             [0, 0, 0, 'S', 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0]]
    position = game.whereIsSAndW(board, A, B)
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
        with mock.patch('builtins.input', return_value="W"):
            game.move(A, B, board, position[0], position[1], position[2], position[3], 0)

            assert fake_out.getvalue() == 'Tam jest przeszkoda\n''[0, 0, 1, 0, 0]\n'"['W', 0, 0, 1, 0]\n""[0, 0, 0, 'S', 0]\n"'[0, 0, 0, 0, 0]\n''[0, 0, 0, 1, 0]\n'


def test_move_down_when_there_is_obstacle():
    A = 5
    B = 5
    board = [[0, 0, 1, 'S', 0],  # 0,4
             ['W', 0, 0, 1, 0],  # 1,0
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0]]
    position = game.whereIsSAndW(board, A, B)
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
        with mock.patch('builtins.input', return_value="S"):
            game.move(A, B, board, position[0], position[1], position[2], position[3], 0)

            assert fake_out.getvalue() == 'Tam jest przeszkoda\n'"[0, 0, 1, 'S', 0]\n""['W', 0, 0, 1, 0]\n"'[0, 0, 0, 0, 0]\n''[0, 0, 0, 0, 0]\n''[0, 0, 0, 1, 0]\n'


def test_move_left_when_there_is_obstacle():
    A = 5
    B = 5
    board = [[0, 0, 1, 'S', 0],  # 0,4
             ['W', 0, 0, 1, 0],  # 1,0
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0]]
    position = game.whereIsSAndW(board, A, B)
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
        with mock.patch('builtins.input', return_value="A"):
            game.move(A, B, board, position[0], position[1], position[2], position[3], 0)

            assert fake_out.getvalue() == 'Tam jest przeszkoda\n'"[0, 0, 1, 'S', 0]\n""['W', 0, 0, 1, 0]\n"'[0, 0, 0, 0, 0]\n''[0, 0, 0, 0, 0]\n''[0, 0, 0, 1, 0]\n'


def test_move_right_when_there_is_obstacle():
    A = 5
    B = 5
    board = [[0, 'S', 1, 0, 0],  # 0,4
             ['W', 0, 0, 1, 0],  # 1,0
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0]]
    position = game.whereIsSAndW(board, A, B)
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
        with mock.patch('builtins.input', return_value="D"):
            game.move(A, B, board, position[0], position[1], position[2], position[3], 0)

            assert fake_out.getvalue() == 'Tam jest przeszkoda\n'"[0, 'S', 1, 0, 0]\n""['W', 0, 0, 1, 0]\n"'[0, 0, 0, 0, 0]\n''[0, 0, 0, 0, 0]\n''[0, 0, 0, 1, 0]\n'

def test_move_to_win_spot():
    A = 5
    B = 5
    board = [[0, 0, 1, 0, 0],  # 0,4
             ['W', 'S', 0, 1, 0],  # 1,0
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0]]
    position = game.whereIsSAndW(board, A, B)
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
        with mock.patch('builtins.input', return_value="A"):
            game.move(A, B, board, position[0], position[1], position[2], position[3], 0)

            assert fake_out.getvalue() == "Brawo, znalazłeś wyjście!\n"
