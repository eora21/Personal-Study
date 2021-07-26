T = int(input())

for case in range(T):
    N = int(input())
    
    li = []
    for n in range(N):
        li.append([0] * N)
    
    """
    row 고정, col 증가
    col 고정, row 증가
    row 고정, col 감소
    col 고정, row 감소
    """

    mode = 3
    cnt = 1
    row = N - 1
    col = 0

    for i in range(N):
        li[0][i] = cnt
        cnt += 1
    for j in range(1, N):
        li[j][i] = cnt
        cnt += 1
    for k in range(N - 2, -1, -1):
        li[j][k] = cnt
        cnt += 1

    while(cnt <= N ** 2):
        if mode == 0:
            col += 1
            if li[row][col + 1] != 0:
                mode = 1
        elif mode == 1:
            row += 1
            if li[row + 1][col] != 0:
                mode = 2
        elif mode == 2:
            col -= 1
            if li[row][col - 1] != 0:
                mode = 3
        else:
            row -= 1
            if li[row - 1][col] != 0:
                mode = 0
        li[row][col] = cnt
        cnt += 1

    print(f"#{case + 1}")
    for line in li:
        print(" ".join(map(str, line)))
    