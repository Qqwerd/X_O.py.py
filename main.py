maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

win =  [[0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]]

def game_map():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])

    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])

    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])

def move_map(move,xo):
    ind = maps.index(move)
    maps[ind] = xo

def results():
    vic = ""
    for i in win:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            vic = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            vic = "O"
    return vic

game_over = False
player1 = True

while game_over == False:
    game_map()
    if player1 == True:
        xo = "X"
        move = int(input("Play1,your move"))
    else:
        xo = "O"
        move = int(input("Play2,your move"))

    move_map(move, xo)
    vic = results()
    if vic != "":
        game_over = True
    else:
        game_over = False
    player1 = not(player1)

game_map()
print("Win",vic)