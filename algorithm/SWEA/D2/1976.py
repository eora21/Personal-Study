T = int(input())

for case in range(T):
    
    H1, M1, H2, M2 = map(int, input().split())

    M = (M1 + M2) % 60
    H = ((H1 + H2) + (M1 + M2) // 60) % 12
    if H == 0: H = 12

    print(f"#{case + 1} {H} {M}")