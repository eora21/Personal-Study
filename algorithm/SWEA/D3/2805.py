for case in range(int(input())):
    N = int(input())

    li = [list(map(int, list(input()))) for _ in range(N)]

    total = 0

    middle = N // 2

    for row in range(N):
        for col in range(N):
            if row < middle and col < middle:
                total += li[row][col] if row + col >= middle else 0
            elif row < middle and col > middle:
                total += li[row][col] if col - row <= middle else 0
            elif row > middle and col < middle:
                total += li[row][col] if row - col <= middle else 0
            elif row > middle and col > middle:
                total += li[row][col] if row + col <= middle * 3 else 0
            else:
                total += li[row][col]
    
    print("#{} {}".format(case+ 1, total))