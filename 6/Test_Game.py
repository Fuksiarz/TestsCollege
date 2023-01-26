import Game
import pytest

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
