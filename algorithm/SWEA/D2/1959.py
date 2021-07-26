T = int(input())

for case in range(T):
    ABnum = input().split(" ")

    if int(ABnum[0]) >= int(ABnum[1]): #A가 무조건 작은 사이즈로 통일
        B = list(map(int, input().split(" ")))
        A = list(map(int, input().split(" ")))
    else:
        A = list(map(int, input().split(" ")))
        B = list(map(int, input().split(" ")))

    max_total = 0

    for i in range(len(B) - len(A) + 1):
        total = 0
        j = 0
        for A_value in A:
            total += A_value * B[i + j]
            j += 1
        if max_total < total: max_total = total
    
    print(f"#{case + 1} {max_total}")