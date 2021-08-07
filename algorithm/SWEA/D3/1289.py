T = int(input())

for case in range(T):
    answer = input()
    li = [0] * len(answer)

    cnt = 0
    for i in range(len(li)):
        if int(answer[i]) != li[i]:
            li[i:] = [int(answer[i])] * len(li[i:])
            cnt += 1

    print(f"#{case + 1} {cnt}")