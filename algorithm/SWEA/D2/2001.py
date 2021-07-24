T = int(input())

for i in range(T):
    NandM = input()
    NandM = NandM.split(" ")
    N = int(NandM[0])
    M = int(NandM[1])

    array = [[]]*N
    

    for row in range(N):
        array[row] = list(map(int, input().split(" ")))

    Max_fly = 0

    for row in range(N - M + 1):
        for col in range(N - M + 1):
            fly = 0
            for cnt in range(row, row + M):
                fly += sum(array[cnt][col:col + M])
            print(fly, row, col)
            if Max_fly < fly:
                Max_fly = fly
    
    print(f"#{i + 1} {Max_fly}")
