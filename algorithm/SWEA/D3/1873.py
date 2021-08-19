class Game:
    def __init__(self, H, W):
        self.li = []
        self.H = H
        self.W = W
        for row in range(H):
            string = input()
            tank =  max(string.find("^"), string.find("<"), string.find(">"), string.find("v"))
            if tank != -1:
                self.X = tank
                self.Y = row
            self.li.append(list(string))

    def Command(self, N, act, t):
        def Up():
            self.li[Y][X] = "^"
            if Y != 0:
                _Y = Y - 1
                Move(_Y, X)
            
        def Down():
            self.li[Y][X] = "v"
            if Y != H - 1:
                _Y = Y + 1
                Move(_Y, X)

        def Left():
            self.li[Y][X] = "<"
            if X != 0:
                _X = X - 1
                Move(Y, _X)

        def Right():
            self.li[Y][X] = ">"
            if X != W - 1:
                _X = X + 1
                Move(Y, _X)

        def Move(_Y, _X):
            if self.li[_Y][_X] == ".":
                self.li[Y][X], self.li[_Y][_X] = self.li[_Y][_X], self.li[Y][X]
                self.Y = _Y
                self.X = _X

        def Shoot():
            _Y = Y
            _X = X

            arrow = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

            add_Y, add_X = arrow[self.li[Y][X]]

            while 0 <= _Y + add_Y < H and 0 <= _X + add_X < W:
                if self.li[_Y + add_Y][_X + add_X] == "*":
                    self.li[_Y + add_Y][_X + add_X] = "."
                    break
                elif self.li[_Y + add_Y][_X + add_X] == "#":
                    break
                _Y += add_Y
                _X += add_X

        mode = {"U": Up, "D": Down, "L": Left, "R": Right, "S": Shoot}

        H = self.H
        W = self.W

        for i in range(N):
            X = self.X
            Y = self.Y
            mode[act[i]]()

            # print(act[i])
            # for li_row in self.li:
            #     print(*li_row)
            # try:
            #     print(act[i+1])
            # except:
            #     print("None")
            # print()

        print(f"#{t + 1} ",end="")
        for r in range(H):
            for c in range(W):
                print(game.li[r][c], end="")
            print()
    
    

T = int(input())

for case in range(T):
    Height, Width = map(int, input().split())
    game = Game(Height, Width)

    Num = int(input())
    acting = input()
    
    game.Command(Num, acting, case)