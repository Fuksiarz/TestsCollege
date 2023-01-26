import random


def createMap(A, B):
    mapa = [[0 for i in range(A)] for j in range(B)]
    return mapa


def randomGenerator(A, B):
    generated = random.randint(A, B)

    return random.randint(A, B)


def lower(A, B):
    if A <= B:
        return A
    else:
        return B


def createStartAndStop(x, A, B):
    start = randomGenerator(1, A - 1)
    stop = randomGenerator(1, B - 1)

    x[0][start] = 'S'
    x[stop][0] = 'W'

    return x


def whereIsSAndW(x, A, B):

    # if A>=B:
    #     C=B
    #     D=A
    # else:
    #     C=A
    #     D=B

    for i in x:
        print(i)

    for i in range(B):
        for j in range(A):
            if x[i][j] == 'W':
                koniecX = i
                koniecY = j
            if x[i][j] == 'S':
                startX = i
                startY = j
                break
    # print(startX,"i:",startY, "W: ", koniecX,"i: ", koniecY)
    return startX, startY, koniecX, koniecY


def move(A, B, board, xs, ys, xw, yw):
    playerChoose = input("gdzie mam isc: ")
    match playerChoose:
        case "W":
            if xs == 0:
                print("Nie mozna wyjsc za planszę!")
            elif board[xs - 1][ys] == 1:
                print("Tam jest przeszkoda")
            elif xs - 1 == xw and ys == yw:
                print("Brawo, znalazłeś wyjście!")
                return 0
            else:
                board[xs][ys] = 0
                board[xs - 1][ys] = 'S'
        case "S":
            if xs == B - 1:
                print("Nie mozna wyjsc za planszę!")
            elif board[xs + 1][ys] == 1:
                print("Tam jest przeszkoda")

            elif xs + 1 == xw and ys == yw:
                print("Brawo, znalazłeś wyjście!")
                return 0
            else:
                board[xs][ys] = 0
                board[xs + 1][ys] = 'S'
        case "A":
            if ys == 0:
                print("Nie mozna wyjsc za planszę!")
            elif board[xs][ys - 1] == 1:
                print("Tam jest przeszkoda")
            elif xs == xw and ys - 1 == yw:
                print("Brawo, znalazłeś wyjście!")
                return 0
            else:
                board[xs][ys] = 0
                board[xs][ys - 1] = 'S'
        case "D":
            if ys == A-1:
                print("Nie mozna wyjsc za planszę!")

            elif board[xs][ys + 1] == 1:
                print("Tam jest przeszkoda")

            elif xs == xw and ys + 1 == yw:
                print("Brawo, znalazłeś wyjście!")
                return 0
            else:
                board[xs][ys] = 0
                board[xs][ys + 1] = 'S'
        # for i in board:
        #     print(i)
    position = whereIsSAndW(board, A, B)
    print(position)
    if position[0] == position[2] and position[1] == position[3]:
        print("Brawo, znalazłeś wyjście!")
        return 0
    else:
        return (move(A, B, board, position[0], position[1], position[2], position[3]))


def createObstacles(x, A, B):

    if A>B:
        roznica=A-B
    else:
        roznica= B-A

    for i in range(random.randint(3, lower(A, B) * 2)):
        first = random.randint(0, B -1)
        second = random.randint(0, A - 1)

        if x[first][second] != 'S' and x[first][second] != 'W':
            x[first][second] = 1

    c = random.randint(4, 10)

    return x


if __name__ == '__main__':
    A = 6
    B = 8

    Z = createMap(A, B)
    start = createStartAndStop(Z, A, B)
    obs = createObstacles(start, A, B)
    position = whereIsSAndW(obs, A, B)
    move(A, B, obs, position[0], position[1], position[2], position[3])
