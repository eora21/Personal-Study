adder = {0: (0, 1), 1: (1, 0), 2: (1, -1), 3: (1, 1)}

def check():
    for row in range(N):
        for col in range(N):
            for mode in range(4):
                if 0 <= row + 4 * adder[mode][0] < N and 0 <= col + 4 * adder[mode][1] < N:
                    for step in range(5):
                        if li[row + step * adder[mode][0]][col + step * adder[mode][1]] != 'o':
                            break
                    else:
                        return "YES"
    return "NO"

for case in range(int(input())):
    N = int(input())

    li = [input() for _ in range(N)]
    print("#{} {}".format(case + 1, check()))

