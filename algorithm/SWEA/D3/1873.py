T = int(input())

for case in range(T):
    H, W = map(int, input().split())
    li = [[None]] * H
    
    X, Y = 0, 0

    for row in range(H):
        li[row] = input()
        tank =  max(li[row].find("^"), li[row].find("<"), li[row].find(">"), li[row].find("v"))
        if tank != -1:
            X = tank
            Y = row
        li[row] = list(li[row])

    N = int(input())
    act = input()
    for i in range(N):
        Bomb = False
        _Y = Y
        _X = X
        if act[i] == "U":
            li[Y][X] = "^"
            if Y != 0:
                _Y = Y - 1
        elif act[i] == "D":
            li[Y][X] = "v"
            if Y != H - 1:
                _Y = Y + 1
        elif act[i] == "L":
            li[Y][X] = "<"
            if X != 0:
                _X = X - 1
        elif act[i] == "R":
            li[Y][X] = ">"
            if X != W - 1:
                _X = X + 1
        else:
            Bomb = True
            add_Y = 0
            add_X = 0
            if li[Y][X] == "^":
                add_Y = -1
            elif li[Y][X] == "v":
                add_Y = 1
            elif li[Y][X] == "<":
                add_X = -1
            else:
                add_X = 1
            while 0 <= _Y + add_Y < H and 0 <= _X + add_X < W:
                if li[_Y + add_Y][_X + add_X] == "*":
                    li[_Y + add_Y][_X + add_X] = "."
                    break
                elif li[_Y + add_Y][_X + add_X] == "#":
                    break
                _Y += add_Y
                _X += add_X

        if not Bomb:
            if li[_Y][_X] == ".":
                li[Y][X], li[_Y][_X] = li[_Y][_X], li[Y][X]
                Y = _Y
                X = _X

        # print(act[i])
        # for li_row in li:
        #     print(*li_row)
        # try:
        #     print(act[i+1])
        # except:
        #     print("None")
        # print()

    print(f"#{case + 1} ",end="")
    for r in range(H):
        for c in range(W):
            print(li[r][c], end="")
        print()