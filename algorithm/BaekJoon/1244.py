N = int(input())
swich = list(map(int, input().split()))

for _ in range(int(input())):
    S, V = map(int, input().split())

    if S - 1:  # Woman
        swich[V - 1] = not swich[V - 1]
        for w in range(1, N):
            if 0 <= V - 1 + w < N and 0 <= V - 1 - w < N and swich[V - 1 + w] == swich[V - 1 - w]:
                swich[V - 1 + w] = swich[V - 1 - w] = not swich[V - 1 + w]
            else:
                break
    else:  # Man
        for m in range(V, N + 1, V):
            swich[m - 1] = not swich[m - 1]

for i in range(1, N // 20 + 2):
    print(*map(int, swich[20 * (i - 1): 20 * i]))