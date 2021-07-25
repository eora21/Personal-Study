T = int(input())

for i in range(T):
    ABnum = input().split(" ")

    if int(ABnum[0]) >= int(ABnum[1]): #A가 무조건 작은 사이즈로 통일
        B = input().split(" ")
        A = input().split(" ")
    else:
        A = input().split(" ")
        B = input().split(" ")

    max_total = 0

    for i in range(len(B) - len(A) + 1):
        total = 0
        j = 0
        for A_value in A:
            total += A_value * B[i + j]
            j += 1
        if max_total < total: max_total = total
    
    print(f"#{i + 1} {max_total}")