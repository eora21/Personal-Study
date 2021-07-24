li = [2, 3, 5, 7, 11]

T = int(input())

for i in range(T):
    print(f"#{i + 1}", end=" ")
    N = int(input())
    ans = [0] * 5
    for cnt in range(len(li)):
        while True:
            if not N % li[cnt]:
                N /= li[cnt]
                ans[cnt] += 1
            else:
                print(f"{ans[cnt]}", end=" ")
                break
    print()
