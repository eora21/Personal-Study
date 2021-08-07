T = int(input())

for case in range(T):
    L, U, X = map(int, input().split())
    out = None
    if X < L:
        out = L - X
    elif X <= U:
        out = 0
    else:
        out = -1
    
    print(f"#{case + 1} {out}")